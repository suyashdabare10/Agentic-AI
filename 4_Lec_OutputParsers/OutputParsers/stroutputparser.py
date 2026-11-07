from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOllama(
    model="gemma3:1b"
)

template1 = PromptTemplate(
    template="Explain me in the detail about the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Give me the only 5 line Summary of the {text}",
    input_variables=['text']
)

outputparser = StrOutputParser()


chain = template1 | model | outputparser | template2 | model | outputparser

result = chain.invoke({'topic':'Pulsar'})

print(result)



