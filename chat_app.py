import streamlit as st
import openai

openai.api_key = "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"
model = openai.Model.retrieve("text-davinci-003")

st.title("Chat with something more intelligent than you!")
st.sidebar.header("Instructions")
st.sidebar.info("""Just aks any question you want and the chat bot will give you an answer! Depending on your task, you can choose different models:\n
model 1: 'text-davinci-003' very good for question and answer\n
model 2: 'curie' for sentiment and summarization\n
model 3: 'ada' good for classification tasks""")
model_input = st.text_input("Choose the model you want to use!")
prompt_input = st.text_input("Ask a question!", "Why are vegan people superior?")

def ChatGPT():
    completion = openai.Completion.create(engine=model_input, prompt=prompt_input, max_tokens = 2000, temperature=0.7)
    message = completion.choices[0].text
    return message

def main():
    response = ChatGPT()
    return st.write(f"{response}")

if model_input != "":
    main()
