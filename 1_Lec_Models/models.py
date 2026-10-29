from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv

llm = ChatOllama(
    model='gemma3:1b'
    )

user_input = input("User : ")

result = llm.invoke(user_input)

print("AI :",result.content)