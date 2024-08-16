import streamlit as st
from SimplerLLM.language.llm import LLM, LLMProvider
from prompts import Standard, Academic, Kiddie, Formal, Expand, Shorten, Creative

st.title("AI Paraphrasing Tool")

input_text = st.text_area("Paste your text here", height=300)

style = st.selectbox("Choose the style of transformation", 
                             ['Standard', 'Academic', 'Formal', 'Kiddie', 'Creative', 'Expand', 'Shorten'])


def get_style(style):
    return {
        'Standard': Standard,
        'Academic': Academic,
        'Formal': Formal,
        'Kiddie': Kiddie,
        'Creative': Creative,
        'Expand': Expand,
        'Shorten': Shorten
    }[style]

if st.button("Paraphrase Text"):
        
    prompt = get_style(style) 
    final_prompt = prompt.format(input=input_text)
        
    llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-4o")  
    response = llm_instance.generate_response(prompt=final_prompt, max_tokens=1000)
        
    st.write(response)
    st.success("Text Paraphrased Successfully!")