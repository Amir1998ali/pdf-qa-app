import streamlit as st
import requests


# API Endpoint
BACKEND_URL = "http://127.0.0.1:8000/process_pdf/"

st.title("📄 AI-Powered PDF Q&A (No Storage)")
st.write("Upload a PDF, ask a question, and get instant answers!")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
query = st.text_input("Enter your question:")

if uploaded_file and query:
    with st.spinner("Processing..."):
        files = {"file": uploaded_file.getvalue()}
        params = {"query": query}
        response = requests.post(BACKEND_URL, files=files, params=params)

        if response.status_code == 200:
            st.success("✅ Answer: " + response.json()["answer"])
        else:
            st.error(f"❌ API Error: {response.text}")

