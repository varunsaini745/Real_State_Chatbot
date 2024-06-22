from qa_processor import QAProcessor
from dotenv import load_dotenv
import streamlit as st
from dotenv import load_dotenv
st.set_page_config(
    page_title="QA Processor",
    page_icon=":robot:"
)
load_dotenv()
st.header("Real state Based Question Answering System")

with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        answer = QAProcessor().ask_question(question=text)
        print(answer)
        st.write(answer['answer'])



