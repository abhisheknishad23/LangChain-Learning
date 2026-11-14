from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

#schema
class Review(TypedDict):
    summary: str
    sentiment: str

result = model.invoke(""" review """)

print(result)
print(result['summary'])
print(result['sentiment'])