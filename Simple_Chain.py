from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq  # Import from Groq instead of OpenAI
from dotenv import load_dotenv


import os

load_dotenv()  # Load environment variables from .env file

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing. Please set it in the .env file.")

# Initialize the Groq model (You may need to specify a model name)
model = ChatGroq(model_name="llama3-8b-8192", api_key=groq_api_key)  

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()