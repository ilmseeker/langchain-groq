import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv("main_code\\env\\.env")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


llm = ChatGroq(model="llama3-8b-8192", 
               api_key=GROQ_API_KEY,
               verbose=True,
               temperature=0.0,
               
               )