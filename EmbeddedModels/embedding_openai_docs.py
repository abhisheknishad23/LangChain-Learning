from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

document = [
    "delhi is tha capital of india",
    "paris is the capital of france",
    "lucknow is tha capital of up"
]

result = embedding.embed_documents(document)

print(str(result))