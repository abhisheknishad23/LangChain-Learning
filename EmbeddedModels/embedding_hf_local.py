from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="")

text = "delhi is the capittal of india"

vector = embedding.embed_query(text)

print(str(vector))