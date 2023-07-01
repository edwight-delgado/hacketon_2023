from typing import Union
import os
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import json
from chatbot import chatbot




root = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()
app.mount("/js", StaticFiles(directory=os.path.join(root, 'js')), name="js")
app.mount("/css", StaticFiles(directory=os.path.join(root, 'css')), name="css")

origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    with open(os.path.join(root, 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")


@app.post("/")
async def read_question(request: Request):
    req_info = await request.json()
    print(req_info['data'])
    #res = chatbot(message = req_info['data'])
    res = 'esto es una prueba con capybara'

    #print(await request.body())
    #return {"data": await request.json()}
    return res

@app.get("/shopping-card-api")
async def get_card():
    with open("product.json", "r") as read_file:
        items = json.load(read_file)

    return {"items": items}