# fast_api_tutorial

BOOK: Building GenerativeAI services with FastAPI : https://www.oreilly.com/library/view/building-generative-ai/9781098160296/

## FastAPI offers these features out of the box:

- data validation
- type safety
- automatic documentation
- built in web server

## Challenges around the adoption of GenAI services

- inaccuracy
- relevance
- quality
- consistency
- data privacy
- cybersecurity
- potential abuse and misuse

of outputs.

## Intro to FastAPI

#### FastAPI is an asynchronous gateway interface(ASGI) web framework, that enables to build lean APIs and backend web servers.

#### Installation

```
pip install "fastapi[standard]" uvicorn openai

```

- `uvicorn` package is the bare-bones web server that FastAPI runs on.

- The app object—which is created from the FastAPI class—converts your Python
  function with a decorator into a Hypertext Transfer Protocol (HTTP) endpoint. You
  can trigger both endpoints by sending an HTTP request.

#### Terminology

- thread
- synchronous and asynchronous workflow
- concurrency
