from fastapi import FastAPI
from fastapi import Body
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
anthropic_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# path operation or root function
@app.get("/")
async def root_controller():
    return {"status": "healthy"}

@app.get("/chat")
def chat_controller(prompt: str = "Inspire me"):
    response = anthropic_client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system="You are a helpful assistant.",
        messages=[
            {
                "role": "user", "content": prompt
            }
        ]
    )
    statement = response.content[0].text
    return {"statement": statement}

