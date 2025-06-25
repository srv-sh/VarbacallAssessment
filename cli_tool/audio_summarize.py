import argparse
import uuid
import json
import requests
from pathlib import Path
from datetime import datetime
import mimetypes
import openai

# ========== FASTAPI STT TRANSCRIBE ========== #
def fastapi_stt_transcribe(audio_path, is_bn=False, endpoint="http://192.168.10.38:5959/asr/"):
    mime_type, _ = mimetypes.guess_type(audio_path.name)

    if mime_type not in ["audio/wav", "audio/x-wav", "audio/mpeg"]:
        raise ValueError(f"[ERROR] Unsupported audio format: {mime_type}")

    with open(audio_path, "rb") as f:
        files = {"file": (audio_path.name, f, mime_type)}
        data = {"is_bn": str(is_bn).lower()}
        response = requests.post(endpoint, files=files, data=data)

    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        raise Exception(f"[ERROR] STT API failed: {response.status_code} - {response.text}")

# ========== GPT SUMMARIZER ========== #
def summarize_with_gpt(transcript, openai_key):
    openai.api_key = openai_key

    print("[GPT] Summarizing transcript...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes phone call transcripts."},
            {"role": "user", "content": f"Summarize the following transcript:\n\n{transcript}"}
        ]
    )
    return response.choices[0].message.content.strip()

# ========== JSON LOG SAVER ========== #
def save_session_log(session_id, transcript, summary, out_dir="logs"):
    log = {
        "session_id": session_id,
        "timestamp": datetime.utcnow().isoformat(),
        "transcript": transcript,
        "summary": summary
    }
    Path(out_dir).mkdir(exist_ok=True)
    out_path = Path(out_dir) / f"{session_id}.json"
    with open(out_path, "w") as f:
        json.dump(log, f, indent=2)
    print(f"[LOG] Saved summary to {out_path}")

# ========== MAIN CLI ========== #
def main():
    parser = argparse.ArgumentParser(description="CLI Tool: WAV/MP3 → STT → GPT Summary → JSON Log")
    parser.add_argument("audio_file", help="Path to .wav or .mp3 audio file")
    parser.add_argument("--fastapi-url", default="http://192.168.10.38:5959/asr/", help="FastAPI ASR endpoint URL")
    parser.add_argument("--openai-api-key", required=True, help="OpenAI API key")
    parser.add_argument("--is-bn", action="store_true", help="Set if the audio is Bangla")

    args = parser.parse_args()

    session_id = str(uuid.uuid4())[:8]
    audio_path = Path(args.audio_file)

    if not audio_path.exists():
        print(f"[ERROR] File {audio_path} does not exist.")
        return

    try:
        transcript = fastapi_stt_transcribe(audio_path, is_bn=args.is_bn, endpoint=args.fastapi_url)
    except Exception as e:
        print(str(e))
        return

    print(f"[STT] Transcript:\n{transcript}")

    summary = summarize_with_gpt(transcript, args.openai_api_key)
    print(f"[GPT] Summary:\n{summary}")

    save_session_log(session_id, transcript, summary)

if __name__ == "__main__":
    main()
