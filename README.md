# Diagnosis Assistant — Setup Guide

A clinical diagnostic assistant that transcribes doctor-patient audio and generates AI-powered diagnostic insights.

---

## Prerequisites

- Python 3.13 recommendend
- A Groq account and API key — [console.groq.com](https://console.groq.com)
- A Supabase account and project — [supabase.com](https://supabase.com)
- A `C:/Temp` folder on your machine (create it manually in File Explorer)

---

## Installation

### 1. Clone or download the project
Place all files in a folder, e.g. `C:/Users/username/Documents/diagnosis.py`

### 2. Install dependencies
Open a terminal and run:
```bash
pip install groq openai-whisper streamlit supabase torch
```

### 3. Install ffmpeg (required by Whisper)
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your system PATH.

---

## Supabase Setup

1. Go to your Supabase project dashboard
2. Open the **Table Editor** and create a new table called `encounters` with the following columns:
---

## Running the App

In your terminal, navigate to the project folder and run:

```bash
python -m streamlit run "c:/Users/whizzbang/Documents/SMART EMR/diagnosis.py"
```

The app will open in your browser at `http://localhost:8501`

---

## How to Use

1. Open the app in your browser
2. Upload an MP3 audio file of a patient consultation
3. Click **Analyze**
4. Wait for transcription to complete (this may take a moment depending on audio length)
5. View the transcript and AI-generated diagnostic insights
6. The encounter is automatically saved to Supabase

---

## Project Structure

```
SMART EMR/
│
├── diagnosis.py        # Main app — transcription, AI diagnosis, Supabase, Streamlit UI
└── README.md           # This file
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Speech-to-Text | OpenAI Whisper (runs locally) |
| AI Diagnostic Engine | Groq API + LLaMA 3.1 8B |
| Database | Supabase (PostgreSQL) |
| Frontend | Streamlit |
| Language | Python 3 |

---

## Troubleshooting

**`streamlit` is not recognized** — use `python -m streamlit run` instead of `streamlit run`

**Error code 123** — make sure `C:/Temp` exists on your machine

**Whisper takes too long** — the `base` model is a balance of speed and accuracy. For faster results use `tiny`, for better accuracy use `small` or `medium`

**Empty data in Supabase** — check that RLS is disabled or a policy is set on the `encounters` table