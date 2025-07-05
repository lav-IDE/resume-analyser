import streamlit as st 
import PyPDF2 as pyd

# extracting text
def extracted_text(file):
    reader = pyd.PdfReader(file)
    text = ""
    for page in reader.pages:
        text+=page.extract_text()
    return text

# building a web app using streamlit    
st.title("Resume Analyser AI")
st.write("Upload your resume (in PDF format) and the AI will analyse and present to you the moderations it requires")

resume_file = st.file_uploader("Select your resume PDF", type="pdf")

if resume_file is not None:
    st.success("Congo! Your file has been uploaded successfully")
    resume_text = extracted_text(resume_file)
    st.subheader("📜Extracted Resume Text")
    st.write(resume_text)
    