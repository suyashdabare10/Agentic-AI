from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOllama(
    model="gemma3:1b"
)

parser = JsonOutputParser()


template = PromptTemplate(
    template= "Give me a Name, Age, Movie and City of the Fictional Character \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions}
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser 

result = chain.invoke({})

print(result)

