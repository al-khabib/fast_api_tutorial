from fastapi import FastAPI
from fastapi import Body
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# path operation or root function
@app.get("/")
async def root_controller():
    return {"status": "healthy"}

@app.get("/chat")
def chat_controller(prompt: str = "Inspire me"):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": 'system', "content": "You are a helpful assistant."
            },
            {
                "role": 'user', "content": prompt
            }
        ]
    )
    statement = response.choices[0].message.content
    return {"statement": statement}

