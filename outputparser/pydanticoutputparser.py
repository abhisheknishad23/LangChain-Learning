from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputparser, ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-geneation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to ')

parser = PydanticOutPutParser(pydantic_object = Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {formate_instruction}',
    input_variables=['place'],
    partial_variables={'formate_instruction':parser.get_formate_instruction()}
)

prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

