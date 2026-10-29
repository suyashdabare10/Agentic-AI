from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOllama(
    model='gemma3:1b'
)

st.header('Research Tool')

paper_input = st.selectbox("Choose the Book", ["Mahabharata", "Ramayana", "Vedas", "Upnishads"])
length_input = st.selectbox("Choose length", ["Short", "Medium", "Long"])

template = PromptTemplate(
    template=
    """
Give me a Explanation about the {paper_input} in {length_input} length
    """,
    input_variables=['paper_input', "length_input"]
)

# prompt = template.invoke({
#     'paper_input' : paper_input,
#     'length_input' : length_input
# })




if st.button('Summarize'):
    chain = template | model

    result = chain.invoke({
    'paper_input' : paper_input,
    'length_input' : length_input
    })
    
    st.write(result.content)