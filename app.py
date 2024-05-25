import streamlit as st 
from langchain_community.llms import HuggingFaceEndpoint


# give huggingface access token to use the endpoint
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets['HF_TOKEN']

#function to return response
def load_answer(question):
    
    # loading inference endpoint for any model
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

    llm = HuggingFaceEndpoint(repo_id=repo_id)
    result = llm.invoke(question)
    return result

#App UI here
st.set_page_config(page_title='QA using Langchain', page_icon = ":robot:")
st.header('Question Answer Demo')

# Get user input question
def get_text():
    input_text = st.text_input("Enter your question: ",key = 'input')
    return input_text

user_input = get_text()
submit = st.button('Generate')

if submit:
    try: 
        st.subheader('Answer')
        response = load_answer(user_input)
        st.write(response)

    # Don't allow null input
    except:
        st.write('Input cannot be null')