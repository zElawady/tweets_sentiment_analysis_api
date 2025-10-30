import streamlit as st
import requests
import os
import subprocess
import time
from src.utils.config import get_settings

# Get settings
settings = get_settings()

# Streamlit app title
st.title("Sentiment Analysis API Frontend")

# Ensure the backend is running
def start_backend():
    try:
        # Start the backend process
        backend_process = subprocess.Popen(
            ["uvicorn", "src.Core.backend:app", "--host", settings.HOST, "--port", str(settings.PORT), "--reload"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time.sleep(5) 
        return backend_process
    except Exception as e:
        st.error(f"Failed to start the backend: {e}")
        return None

# Check if the backend is already running
backend_running = os.system(f"netstat -ano | findstr :{settings.PORT}") == 0
if backend_running:
    st.info("Backend is already running.")
else:
    backend_process = start_backend()
    if backend_process:
        st.success("Backend started successfully.")

input_text = st.text_area("Enter text for sentiment analysis:")

# Get the absolute path to the images directory
image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "images", "Blog_DA_Sentiment_Customer_08052022.png")

with st.sidebar:
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    st.header("API Key")
    API_KEY = st.text_input("Enter your API Key", type="password")
    st.markdown("**Note:** This API key is used to authenticate your requests.")
    
    # Dropdown for model type
    model_type = st.selectbox("Select Model Type", ["tfidf", "bow", "glove"])
    
    # Dropdown for model name
    model_name = st.selectbox("Select Model Name", ["svm", "rf"])

if st.button("Analyze Sentiment"):
    with st.spinner("Analyzing..."):
        if input_text.strip():
            try:
                sentences = [s.strip() for s in input_text.split("\n") if s.strip()]

                # Send request to the backend API with the API key and model details in headers
                response = requests.post(
                    f"http://{settings.HOST}:{settings.PORT}/predict",
                    json={"texts": sentences, "model_type": model_type, "model_name": model_name},
                    headers={"X-API-Key": API_KEY}
                )

                # Handle response
                if response.status_code == 200:
                    result = response.json()
                    predictions = result.get("predictions", [])
                    if predictions:
                        for prediction in predictions:
                            if prediction['sentiment'] == "Negative":
                                st.success(f"'💬Text': {prediction['text']}\n >>>> '✅Sentiment': {prediction['sentiment']} 😢")
                            elif prediction['sentiment'] == "Positive":
                                st.success(f"'💬Text': {prediction['text']}\n >>>> '✅Sentiment': {prediction['sentiment']} 😊")
                            else:
                                st.success(f"'💬Text': {prediction['text']}\n >>>> '✅Sentiment': {prediction['sentiment']} 😐")
                    else:    
                        st.warning("No predictions returned from the API.")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text for analysis.")