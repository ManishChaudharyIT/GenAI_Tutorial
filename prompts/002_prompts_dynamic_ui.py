from prompt_templates import prompt_templates  # ✅ No install needed, just import
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st



load_dotenv()

def simple_promots():
    # Initialize the model
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    st.title("🧠 AI Research Tool")

    # Step 1: Task Type Selection
    task = st.selectbox(
        "Choose a task",
        ["Summarize", "Explain", "List points", "Give pros & cons", "Translate to Hindi"]
    )

    # Step 2: Topic Selection (or custom entry)
    topics = ["Climate change", "Artificial Intelligence", "Blockchain", "Electric Vehicles", "Custom Topic"]
    selected_topic = st.selectbox("Choose a topic", topics)

    # If user chooses custom topic, show a text input
    if selected_topic == "Custom Topic":
        selected_topic = st.text_input("Enter your custom topic")

    # Step 3: Generate dynamic prompt
    prompt_map = {
        "Summarize": f"Summarize the topic: {selected_topic}",
        "Explain": f"Explain in detail: {selected_topic}",
        "List points": f"List the key points about {selected_topic}",
        "Give pros & cons": f"What are the pros and cons of {selected_topic}?",
        "Translate to Hindi": f"Translate this to Hindi: {selected_topic}"
    }

    default_prompt = prompt_map.get(task, "")

    # Step 4: Editable prompt
    user_input = st.text_area("Generated prompt (you can edit it):", value=default_prompt)

    # Step 5: Run the model
    if st.button("Run"):
        if user_input.strip():
            result = model.invoke(user_input)
            st.markdown("### ✨ Response:")
            st.write(result.content)
        else:
            st.warning("Prompt cannot be empty!")






def with_importing_template():
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    st.title("🧠 AI Prompt Generator")

    # Select a prompt template
    selected_template_name = st.selectbox("Select a prompt template", list(prompt_templates.keys()))

    # Choose topic
    topics = ["Climate Change", "Artificial Intelligence", "Blockchain", "Custom"]
    selected_topic = st.selectbox("Choose a topic", topics)

    if selected_topic == "Custom":
        selected_topic = st.text_input("Enter your custom topic")

    # Generate prompt from template
    raw_template = prompt_templates[selected_template_name]
    filled_prompt = raw_template.format(topic=selected_topic)

    # Allow user to edit
    final_prompt = st.text_area("Generated Prompt (you can edit it)", value=filled_prompt)

    # Run prompt
    if st.button("Run Prompt"):
        if final_prompt.strip():
            result = model.invoke(final_prompt)
            st.markdown("### 🔍 AI Response:")
            st.write(result.content)
        else:
            st.warning("Prompt is empty.")
