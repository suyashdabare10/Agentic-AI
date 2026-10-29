from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOllama(
    model='gemma3:1b'
)

chat_history = [
    SystemMessage('You are helpful AI Assistant')
]

while True:
    user_input = input("User : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI : ',result.content)

print(chat_history)    