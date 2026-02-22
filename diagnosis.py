from groq import Groq
from torch import save
import whisper
import supabase
from supabase import create_client, Client 
import streamlit as st
import os
import tempfile

# speech-to-text section
def transcribe():
    model = whisper.load_model("base")
    transcription = model.transcribe(r"C:\Users\whizzbang\Downloads\MSK0006.mp3")
    transcript_text = (transcription["text"])
    return(transcript_text)

# groq for the diagnosis brain
client = Groq(api_key = "groq API key")

# diagnosis report
def diagnosis(transcript_text):
    responses = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages = [
        {"role": "system", "content": "You are a clinical diagnostic assistant that supports the expert's(doctor) diagnosis..."},
        {"role": "user", "content": transcript_text}
        ]
    )
    return(responses.choices[0].message.content)


# supabase connection
url = "supabase url"
key = "supabase key"

supabase = create_client(url, key)

response = (supabase.table("encounters").select("*").execute())

print(response.data)

# streamlip web app

st.set_page_config(page_title="Diagnosis Assistant")
st.title("Diagnosis Assistant")

uploaded_file = st.file_uploader("Upload Consultation Audio", type="mp3")

if uploaded_file and st.button("Analyze"):
    try:
        with st.spinner("Transcribing..."):
            suffix = os.path.splitext(uploaded_file.name)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix, dir="C:/Temp") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        transcript_text = transcribe()

        st.subheader("Transcript")
        st.write(transcript_text)

        with st.spinner("Generating diagnosis..."):
            final_result = diagnosis(transcript_text)

            st.subheader("Diagnosis & Insights")
            st.markdown(final_result)

            save(transcript_text, final_result)
            st.success("Saved to Supabase!")
    
    except Exception as e:
        st.error("THANK YOU!")