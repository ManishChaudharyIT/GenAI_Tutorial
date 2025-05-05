# # Required imports
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env
# load_dotenv()

# # Step: Work With Hugging Face
# ''' 
# 1. Pahle LLM Banao 
# 2. Model Banao 
# '''

# # Get token from environment
# token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# # LLM Define from Hugging Face
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
#     task="text-generation",
#     huggingfacehub_api_token=token
# )

# # Model Define by you
# model = ChatHuggingFace(llm=llm)

# # Taking input with proper chat-style prompt
# prompt = "who is god of cricket"
# result = model.invoke(prompt)

# # Output
# print(result.content)


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-alpha",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("Write a short story about AI in 2050.")
print(result.content)