from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOllama(
    model="gemma3:1b"
)

schema = [
    ResponseSchema(name="Fact_1", description='Fact_1 about topic'),
    ResponseSchema(name="Fact_2", description='Fact_2 about topic'),
    ResponseSchema(name="Fact_3", description='Fact_3 about topic'),
    ResponseSchema(name="Fact_4", description='Fact_4 about topic'),
    ResponseSchema(name="Fact_5", description='Fact_5 about topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me 5 Facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instruction()}
)


# prompt = template.invoke({'topic':'Magnetar'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

result = chain.invoke({'topic':'magnetar'})

print(result)