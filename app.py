import streamlit as st
import requests

st.title("ID Verification System with Cloudinary")

uploaded_file = st.file_uploader("Upload your ID for verification", type=["jpg", "png"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("https://huggingface.co/spaces/Kenjinx07/Fast-api/verify", files=files)

    if response.status_code == 200:
        result = response.json()
        st.write("Verification Score:", result["verification_score"])
    else:
        st.write("Verification failed")
