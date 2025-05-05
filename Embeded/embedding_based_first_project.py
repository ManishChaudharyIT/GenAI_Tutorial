from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


'''
model="text-embeding-3-large ye free nhi hai
'''

embeding = OpenAIEmbeddings(model="text-embeding-3-large",dimensions=300)
# Sample documents
documents = [
    "Python is a high-level programming language.",
    "Paris is the capital of France.",
    "The moon orbits the Earth.",
    "Football is a popular sport."
]

# user query 
query = "tell me about python language"

# First documents embeding
doc_embeding = embeding.embed_documents(documents)

# Second Query Embeding
query_embeding = embeding.embed_query(query)

# Third send your query_embeding and doc_embeding in 2-d to cosine_similarity

scores =  cosine_similarity([query_embeding],doc_embeding)[0]

index,scrore = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
