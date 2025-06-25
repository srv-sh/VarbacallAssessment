# Part 2: Robust STT Pipeline for Elderly Callers with Accents & Background Noise

![Figure 1: STT/TTS system architectur](../diagrams/stt_pipeline.jpg)
*Figure 1: STT/TTS system architecture*

A layered architecture to handle challenges in real-time voice interaction with elderly callers, especially those with foreign accents and noisy environments.


## High-Level Strategy

- **Voice Activity Detection (VAD)**
- **Grace-based speaker completion logic**
- **Audio preprocessing** (denoising, normalization, etc.)
- **Post-STT correction** (accent correction, sentence segmentation)
- **Semantic validation** before intent parsing


## Step-by-Step Breakdown

### 1. Audio Stream Input
Captures incoming live audio (from landline or mobile).

---

### 2. Voice Activity Detection (VAD)
- Uses `webrtcvad` or `silero-vad`.
- Triggers after **>1s of silence**, assuming sentence end.

---

### 3. Grace Period Wait (300 ms)
- Prevents early cutoff for elderly speakers with long pauses.
- Configurable based on age/demographics.

---

### 4. Still Talking Check
- If speech **resumes**, keep streaming.
- If not, move to **preprocessing**.

---

### 5. Audio Preprocessing

| Step                | Purpose                                        | Tools/Models                                      |
|---------------------|------------------------------------------------|---------------------------------------------------|
| Noise Reduction     | Remove static, hum from landlines              | `noisereduce`, `RNNoise`                          |
| Bandpass Filtering  | Retain human voice freq (300–3400 Hz)          | `scipy.signal.butter`, `librosa.effects.bandpass` |
| Volume Normalization| Equalize loud/soft voices                      | `pydub`, `librosa`, `SoX`                         |
| Silence Trimming    | Trim silence before/after speech               | `librosa.effects.trim`, `pydub.silence`           |
| Resampling & Format | Standardize to 16kHz mono WAV                  | `ffmpeg`, `torchaudio.transforms.Resample`        |

---

### 6.  STT & Post-Processing

| Step                   | Purpose                                         | Tools/Models                                   |
|------------------------|--------------------------------------------------|------------------------------------------------|
| STT                    | Transcribe speech                               | **Whisper Large v3** / **Google STT**         |
| Punctuation Restoration| Add missing punctuation                         | `punctuator2`, `DeepSegment`, `T5-small`       |
| Accent Correction      | Fix phonetic quirks (e.g., Bengali/Spanish)     | Rule-based + fine-tuned `BERT` or adapters     |
| Sentence Segmentation  | Break into logical units                        | `spaCy`, `nltk.sent_tokenize`                  |
| Confidence Filtering   | Remove low-confidence output                    | `Whisper` tokens' `avg_logprob`, `no_speech_prob` |

---

### 7. Semantic Validation

- Checks if transcription **matches a valid intent** (e.g., booking, canceling).
- If **YES** → pass to Dialogue Manager.
- If **NO** → **re-prompt** without restarting session.

---

## Common Challenges & How They’re Handled

| Challenge                              | How It’s Handled                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------------|
| Elderly speech with long pauses        | Grace period + still-talking logic prevents early cutoff                         |
| Strong accents (e.g., Bengali/Spanish) | Accent correction + Whisper multilingual robustness                              |
| Noisy static from landlines            | Noise reduction + bandpass filtering                                             |
| Soft/inconsistent volume               | Volume normalization ensures clarity                                             |
| Mispronunciation / unclear phrasing    | Semantic fallback + live context flushing allows clarification without restart   |

---

## Concrete STT Setup

### VAD
- `webrtcvad`, `silero-vad`  
→ Real-time lightweight VAD models

### STT
- `Whisper Large v3`, `Google STT`  
→ Handles accents and noisy environments

---

## Evaluation of Each Stage

| Metric                 | Purpose                            | Toolset                                  |
|------------------------|------------------------------------|------------------------------------------|
| Signal-to-Noise Ratio  | Evaluate denoising effectiveness   | `librosa`, `soundfile`                   |
| Word Error Rate (WER)  | STT accuracy vs ground truth       | `jiwer`, `asr_evaluation`                |
| BLEU / ROUGE           | Match post-processed text to gold  | `nltk`, `rouge_score`                    |
| Human Validation Score | Accent correction, grammar review  | Manual/crowd-sourced validation          |

---