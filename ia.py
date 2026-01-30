import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def responder(mensagem):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Você é a assistente Deia, educada, útil, direta, prestativa, corporativa, engraçada e acolhedora"
             "responda sempre em português do Brasil, com clareza e objetividade."},
            {"role": "user", "content": mensagem}
        ]
    )
    return completion.choices[0].message.content