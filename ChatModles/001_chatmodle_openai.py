from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4")
result =  model.invoke("what is capital or india")
print(result)

# This code ouput will be like this 
'''
{
    'content': 'The capital of India is New Delhi.',
    'additional_kwargs': {},
    'example': False,
    'response_metadata': {
        'token_usage': {'completion_tokens': 9, 'prompt_tokens': 9, 'total_tokens': 18},
        'model_name': 'gpt-4',
        'system_fingerprint': '...',
        'finish_reason': 'stop'
    },
    'tool_calls': None,
    'name': None
}

'''