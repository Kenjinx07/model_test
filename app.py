import streamlit as st
import requests
from PIL import Image

st.title("ID Verification System")

uploaded_file = st.file_uploader("Upload Your ID", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded ID", use_column_width=True)

    if st.button("Verify ID"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://your-fastapi-url.com/predict/", files=files)

        if response.status_code == 200:
            data = response.json()
            if data["verified"]:
                st.success("✅ Verification Successful!")
                st.write("Extracted Text:", data["extracted_text"])
            else:
                st.error("❌ Verification Failed!")
        else:
            st.error("Error in API request!")
