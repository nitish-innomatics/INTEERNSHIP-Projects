import streamlit as st
from openai import OpenAI


with open("key/.api_key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)


st.title(":red[GenAI Application]")
st.subheader(":rainbow[Done under guidance of Innomatics Research Labs]")


st.header(":white[AI Code Reviewer using OpenAI]",divider='rainbow')
prompt = st.text_area("Type Your Python Code Below:", height=100)

if st.button("Verify the Code"):
    st.markdown("<h2 style='color:white;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    
    generated_text = response.choices[0].message.content
    st.write(generated_text)


