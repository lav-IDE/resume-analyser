import streamlit as st 


st.title("Resume Analyser AI")
st.write("Upload your resume (in PDF format) and the AI will analyse and present to you the moderations it requires")

resume_file = st.file_uploader("Select your resume PDF", type="pdf")

if resume_file is not None:
    st.success("Congo! Your file has been uploaded successfully")
    