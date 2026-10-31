from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict  

load_dotenv()

model = ChatOllama(
    model="gemma3:1b"
)


class student(TypedDict):
    Name : str
    Surname : str
    RollNo : str
    Class : str
    Year : str
    Degree : str
    College : str
    Location : str
    Interests : str


structured_output = model.with_structured_output(student)  

result = structured_output.invoke("""
My name is Rahul Sharma. My roll number is 42. I am currently studying in Third Year B.E. Electronics and Telecommunication at JSPM BSIOTR, Pune. I am interested in Artificial Intelligence, Android Development, Cricket and Web Development.
""")

print(result)