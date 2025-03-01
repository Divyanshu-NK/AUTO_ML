import streamlit as st
import pandas as pd
import requests

# Streamlit UI
st.title("Machine Learning Web App")
st.subheader("Upload and View Your Dataset")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    # Read CSV into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the first few rows
    st.subheader("Preview of Uploaded Data")
    st.write(df.head())

    # Send file to Flask backend
    files = {"file": uploaded_file}  # Fixing the key to match Flask
    response = requests.post("http://127.0.0.1:5000/uploads", files=files)  # Ensure endpoint matches Flask

    if response.status_code == 200:
        st.success("File successfully sent to backend!")
    else:
        st.error(f"Error uploading file: {response.text}")
