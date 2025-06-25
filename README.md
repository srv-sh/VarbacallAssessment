# VarbaCallAssessment

A multi-part technical assessment for building a reliable, voice-based virtual assistant system tailored for healthcare use cases, particularly optimized for elderly users and call reliability.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Structure](#structure)
- [Part 1: Prompt Optimization & Reliability](#part-1-prompt-optimization--reliability)
- [Part 2: STT/TTS Pipeline Design](#part-2-stttts-pipeline-design)
- [Part 3: Backend Reliability (System Integration)](#part-3-backend-reliability-system-integration)
- [How to Run](#how-to-run)
- [Author](#author)

---

## 🧩 Overview

This repository contains a comprehensive solution to the VarbaCall technical assessment. The system is designed to ensure:

- Empathetic and efficient handling of patient calls
- Robust handling of noisy audio and foreign accents
- Seamless recovery from dropped calls
- Scalable backend design with real-time state tracking

---

## 🗂️ Structure

```
VarbaCallAssessment/
|
├── cli_tool/
│   ├── audio/
|   |   ├── harvard.mp3
│   ├── logs/
|   |   ├── 0e752527.json   
│   └── audio_summarize.py
|
├── diagrams/
│   ├── solution_architecture.png
│   ├── stt_pipeline.jpg   
│   └── backend_architecture.png
│
├── markdowns/
│   ├── part_1_1.md   
│   ├── part_1_2.md     
│   ├── part_2_1.md     
│   └── part_3_1.md     
│
├── README.md           
```

---

## 🧠 Part 1: Prompt Optimization & Reliability

### 1. **Prompt Compression Challenge**
- Rewrites base prompt with >30% token reduction
- Retains empathy, clarity, and functional reliability  
📄 See [part_1_1.md](markdowns/part_1_1.md)

### 2. **Robust Prompt Logic (Adversarial Inputs)**
- Handles ambiguous, vague, or adversarial speech
- Avoids hallucination or misinterpretation using layered fallback  
📄 See [part_1_2.md](markdowns/part_1_2.md)

---

## 🔊 Part 2: STT/TTS Pipeline Design

### 3. **Accent & Noise Handling Strategy**
- Optimized for elderly users with Bengali/Spanish accents
- Uses denoising, bandpass filtering, Whisper STT, and semantic validation
- Evaluation via SNR, WER, BLEU, and human QA  
📄 See [part_2_1.md](markdowns/part_2_1.md)

---

## 🔁 Part 3: Backend Reliability (System Integration)

### 4. **Call Session Recovery**
- System resumes interrupted calls using:
  - Redis-backed session cache
  - GPT context tracking
  - CRM data sync
- Includes architectural diagrams for end-to-end clarity  
📄 See [part_3_1.md](markdowns/part_3_1.md)

---

## 🧪 Bonus: CLI Tool (Optional)

### 5. **Command Line Tool**

A stretch feature to test local `.wav` files and generate JSON summaries via STT + GPT.

#### 🛠 Features:
- Accepts a `.wav` file from CLI
- Streams audio using google ASR through local api
- Uses GPT via API to summarize the transcript
- Saves result in `/cli_tool/logs/session_<id>.json`

#### ▶️ Usage:

```bash
cd cli_tool
python audio_summarize.py audio/harvard.mp3 --openai-api-key sk-xxx
```

Example output:

```json
{
  "session_id": "0e752527",
  "timestamp": "2025-06-25T19:03:04.852575",
  "transcript": "The stale smell of old beer, lingers it takes heat to bring out the odor. A cold? Dip restores health and zest. A salt pickle taste fine with ham tacos. Al Pastore are my favorite vegetable. Food is the hot cross bun.",
  "summary": "The transcript discusses various food-related topics, mentioning the smell of old beer, the importance of heat in bringing out odors, the health benefits of a cold dip, the enjoyment of a salt pickle with ham tacos, a preference for Al Pastor vegetables, and the appeal of hot cross buns as a type of food."
}
```




## ▶️ How to Run

This repository is documentation-focused. However, to simulate or deploy:

1. **Clone Repo**
   ```bash
   git clone https://github.com/yourusername/VarbaCallAssessment.git
   cd VarbaCallAssessment
   ```
---

## 👤 Author

**Sourav Saha**  
AI/ML Engineer  
📧 [contact.srv.sh@gmail.com]  
🌐 [LinkedIn](https://www.linkedin.com/in/srv-sh/)


