from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOllama(
    model="gemma3:1b"
)

class person(BaseModel):
    name : str = Field(description="Name of the Character")
    age : int = Field(description="Age of the Character")
    city : str = Field(description="City of the Character")

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template="Generate name, age and city of fictional {place} Character \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'place':'Indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

########### Getting Error with Chain ###########

# chain = template | model | parser

# result = chain.invoke({'place' : 'Nepalian'})

# print(result)