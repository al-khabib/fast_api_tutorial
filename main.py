from unittest import skip

from fastapi import FastAPI, status, Depends
from fastapi import Body
from anthropic import Anthropic
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse
import os

load_dotenv()

app = FastAPI()
anthropic_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# redirect root to docs
@app.get("/", include_in_schema=False)
def docs_redirect_controller():
    return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)

# simple chat controller that takes a prompt to generate a response from the anthropic model
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


"""
 Dependency injection - based on a development pattern called 'inversion of control'. 
 You break down a function into a series of functions that can be used across different functions.
 That way you void duplicates

"""
def paginate(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/messages")
def list_messages_controller(pagination: dict = Depends(paginate)):
    skip = pagination["skip"]
    limit = pagination["limit"]
    return {"messages": f"Returning messages from {skip} to {skip + limit}"}

@app.get("/conversations")
def list_conversations_controller(pagination: dict = Depends(paginate)):
    skip = pagination["skip"]
    limit = pagination["limit"]
    return {"conversations": f"Returning conversations from {skip} to {skip + limit}"}

