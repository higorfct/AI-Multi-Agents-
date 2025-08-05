from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_section(title, context):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um analista econômico especializado em indústria mineradora."},
            {"role": "user", "content": f"Com base nos dados a seguir, gere uma análise sobre {title}:\n{context}"}
        ]
    )
    return response.choices[0].message.content
