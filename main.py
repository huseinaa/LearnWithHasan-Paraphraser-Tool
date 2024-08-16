from SimplerLLM.tools.generic_loader import load_content
from SimplerLLM.language.llm import LLM, LLMProvider
from prompts import Academic, Kiddie, Shorten

text = load_content("text.txt")

#Edit the prompt name in accordance to what you want to convert it to
final_prompt = Academic.format(input = text.content)

llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-4o")

response = llm_instance.generate_response(prompt=final_prompt, max_tokens=1000)

with open("response.txt", "w", encoding='utf-8') as f:
    f.write(response)
