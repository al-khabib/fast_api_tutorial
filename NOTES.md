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

#### Lifespan events

#### Security and Authentical Components

#### Bidirectional Web Socket, GraphQL, and Custom Response Support

---

### FastAPI Project Structure

- unlike opinionated frameworks like Djano, with nonopinionated framework like FastAPI you may need to follow good practices for having success.

- learning to structure large applications maybe even more important when working with GenerativeAI models.

-You know you have a good project structure if you can find any function or component within your codebase.

#### POPULAR FASTAPI PROJECT STRUCTURES

##### -FLAT

Advantages: most common due to its simplicity. When you are building an initial version of your application or building a simple microservice, by default you want to go for the Flat structure.

Disadvantages: However, if your projects grows over time it is going to be increasingly difficult to maintain and manage your application. this care it is bast to next your modules and dependencies in their own "block"

```
flat-project
├── app
│ ├── services.py
│ ├── database.py
│ ├── models.py
│ ├── routers.py
│ └── main.py
├── requirements.txt
├── .env
├── .gitignore
```

##### - NESTED

groups similar modules into packages - effectively creating a nested structure and hierarchy of modules.

You group all the models that are similar in nature into a single package, irrespective of the fuature they support.

```
nested-project
├── app
│ ├── main.py
│ ├── dependencies.py
│ └── services
│ │ ├── users.py
│ │ └── profiles.py
│ └── models
│ │ ├── users.py
│ │ └── profiles.py
│ └── routers
│ ├── users.py
│ └── profiles.py
├── requirements.txt
├── .env
├── .gitignore
```

The main pitfall with this project structure is the ambiguous coupling of modules. Changes in one module can cascade into other modules, and it can become difficult to understand the cascading effect of new changes. Over time, it can be challenging to maintain and change the code without performing many updates everywhere else. This is referred to as shotgun updates. Shotgun updates in the context of software development are when it is challenging to maintain and change the code without per‐
forming many updates everywhere else.

<strong>Shotgun Update</strong> - a shotgun update (often called shotgun surgery) is a code smell that occurs when a single, simple, logical change requires numerous, scattered modifications across many different classes, files, or modules.

##### - MODULAR

If you expect difficulty managing module coupling or expecting to deal with a large application, I would recommend using a modular structure.

<strong>The modular structure</strong>—popularized by the Netflix Dispatch FastAPI project—is similar to the nested structure because you can place multiple modules within a package and subpackages. However, the core difference is in how you organize your project.

In the modular structure, modules that are closely related and refer to a specific domain are grouped together.

```
modular-project
├── app
│ └── modules
│ │ ├── auth
│ │ │ ├── routers.py
│ │ │ ├── models.py
│ │ │ ├── dependencies.py
│ │ │ ├── guards.py
│ │ │ ├── services.py
│ │ └── users
│ │ │ ├── router.py
│ │ │ ├── models.py
│ │ │ ├── dependencies.py
│ │ │ ├── services.py
│ │ │ ├── mappers.py
│ │ │ ├── pipes.py
│ │ └── profiles
│ └── routers
│ │ └── users.py
│ └── providers
│ │ └── email.py
│ │ └── stripe.py
............
│ ├── settings.py # global configs
│ ├── middlewares.py # global middleware
│ ├── models.py # global models
│ ├── exceptions.py # global exceptions
│ └── main.py
├── requirements.txt
├── .env
├── .gitignore
```

---

you may be asking yourself, “Which project structure should I
adopt for building generative AI services with FastAPI?”

I found that the best way to structure projects is to progressively reorganize your
project from a flat to a modular structure as your service complexity grows:
