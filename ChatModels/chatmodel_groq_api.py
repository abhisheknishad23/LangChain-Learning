
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load the environment variables from your .env file
load_dotenv()

#  Initialize the model using a universally available open-source model
model = ChatGroq(
    model="openai/gpt-oss-20b", # You can also use "llama3-8b-8192"
    temperature=0
)

# Invoke the model smoothly without provider roadblocks
try:
    result = model.invoke("what is democracy in india")
    print(result.content)
except Exception as e:
    print(f"An error occurred: {e}")
