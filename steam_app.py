import streamlit as st
import requests
import requests

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>

@font-face {
    font-family: 'Carla';
    src: local('Carla');
}

.stApp {
    background: linear-gradient(135deg, #f9fff9, #e8f5e9, #d0f0e0);
    font-family: 'Poppins', sans-serif;
}

.block-container {
    background-color: white;
    padding: 3rem;
    border-radius: 25px;
    box-shadow: 0px 15px 50px rgba(0, 120, 80, 0.08);
}

.main-title {
    font-family: 'Carla', serif;
    font-size: 52px;
    font-weight: 600;
    text-align: center;
    background: linear-gradient(90deg, #1b5e20, #43a047);
    -webkit-background-clip: text;
    -webkit-text-fill-color: pink;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    color: #4e7d4e;
    font-size: 18px;
    margin-bottom: 45px;
}

.textarea {
    border-radius: 18px !important;
    border: 1px solid #c8e6c9 !important;
    background-color: #fafffa !important;
    font-family: 'Poppins', sans-serif !important;
    padding: 15px !important;
}

.stButton > button {
    background: linear-gradient(90deg, #43a047, #66bb6a);
    color: white;
    border-radius: 30px;
    font-weight: 500;
    padding: 0.7rem 2rem;
    border: none;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #2e7d32, #388e3c);
    transform: scale(1.06);
}

.stSlider label {
    font-weight: 500;
    color: #2e7d32;
}

</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="AI Code Reviewer")

st.markdown('<div class="main-title">AI-Powered Code Reviewer</div>', unsafe_allow_html=True)
st.write("Upload your code file and get AI feedback instantly.")

uploaded_file = st.file_uploader("Upload a code file", type=["py", "js", "java", "cpp"])

if uploaded_file is not None:
    with st.spinner("Reviewing code..."):
        files = {"file": uploaded_file}
        response = requests.post(
            "http://127.0.0.1:8000/review",
            files=files
        )

        if response.status_code == 200:
            st.markdown(response.json()["review"], unsafe_allow_html=True)
        else:
            st.error(f"Error {response.status_code}")
            st.write(response.text)


