from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

# Initialize the LLM model
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

st.header("Research Tool!")

# Example input prompt
example_prompt = "Summarize the impact of climate change on agriculture."

# Input box with placeholder and default value
user_input = st.text_input("Enter your prompt", value=example_prompt)

if st.button("Summarize"):
    if user_input.strip():
        result = model.invoke(user_input)
        st.write(result.content)
    else:
        st.warning("Please enter a prompt to summarize.")
