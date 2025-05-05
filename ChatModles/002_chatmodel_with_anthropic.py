from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model="claude-3-sonnet-20240229")
result = model.invoke("What is the capital of India?")
print(result)

'''
output will be like this 
AIMessage(content='The capital of India is New Delhi.')

'''