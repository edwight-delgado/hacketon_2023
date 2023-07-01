from typing import Union
import os
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import json
#from chatbot import chatbot

from MyAgent import MyAgent

import re

#Check if the string starts with "The" and ends with "Spain":

txt = """
    ¡Hola! Soy tu asistente virtual Alex y estaré encantado de ayudarte a encontrar el teléfono perfecto para ti. ¿Me puedes decir tu nombre, edad y para qué usarás el teléfono?

Como eres un gamer y buscas un dispositivo con mucha RAM y GPU, te recomendaría el siguiente modelo:

Modelo: Teléfono de alta gama con un diseño elegante y un rendimiento excepcional. Es perfecto para aquellos que buscan lo mejor en términos de rendimiento, cámara y pantalla. Tiene una memoria interna de 256 GB y 12 GB de RAM, lo cual te brindará un amplio espacio para tus juegos y aplicaciones. Además, su potente GPU garantizará un rendimiento fluido y rápido para disfrutar al máximo de tus juegos.
Este modelo es ideal para tus necesidades como gamer, ya que cuenta con una gran cantidad de RAM y una GPU potente para garantizar un rendimiento óptimo en tus juegos. Además, su diseño elegante te permitirá lucir un teléfono sofisticado mientras juegas.

Si tienes alguna otra pregunta o necesitas más información, no dudes en hacerla. Estoy aquí para ayudarte.
"""
alex = re.search("Alex", txt)
sandra = re.search("Sandra", txt)
if alex:
  print("alex")

elif sandra:
    print('sandra')
else:
  print("No match")



agent1 = '4a254d76-e717-4998-9783-41bd846a0728'
agente1 = MyAgent(agent1)

prompt = """
    Debes empezar la conversacion con un saludo al cliente, presentate como un asistente virtual que busca ayudarlo a buscar un 
    telefono (ejemplo: Hola! Soy tu asistente virtual y te voy a ayudar a elegir un telefono!), luego debes preguntarle su nombre, su edad y el uso que se le dara.
    Si no se te brindan todas las respuestas, insiste con las que falten y luego continua 
    Una vez con todas las respuestas procede a buscar el telefono que mas se acomode a las caracteristicas que se necesitan, siempre puedes aceptar nuevas
"""
res = agente1.get_response(prompt)

print(res)

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
    prompt = req_info['data']
    print(req_info['data'])
    if prompt == 'inicial':
        prompt = """
            prompt = `Comportate como un asesor de ventas en telecomunicaciones que realizara acompañamiento a los usuarios que necesiten ayuda. Tu unico campo de acción es ofrecer informacion sobre telefonos y planes de la compañia "TeleCorp". 

      Debes empezar la conversacion con un saludo al cliente y una presentacion de quien eres, indicando tu nombre y tu cargo,  busca ayudarlo a buscar un telefono, luego debes preguntarle su nombre, su edad y el uso que se le dara.
      Si no se te brindan todas las respuestas, insiste con las que falten y luego continua
      
      Dile que lo vas a derivar con un experto, si el usuario te responde con lenguaje tecnico derivalo con Sandra, de lo contrario derivalo con Alex. Seguido de esto te despides
      
      Es importante que solo te centres en la informacion obtenida de los documentos asignada, no des infromacion de telefonos o planes que no se encuentren en el catalogo. 
      
      Es importante que simpre puedas realizar las siguientes preguntas:
      
      ¿Cual es su presupuesto?
      ¿Para que lo utilizará?
      ¿Para quien es? 
      
      A continuacion tendras unos ejemplos de conversaciones entre comilla:
      
      
      '
        -Usuario: Hola quiero comprar un telefono nuevo
        -Agente: Hola mucho gusto, ¿Por favor deme mas detalle sobre que producto esta buscando
        -Usuario: Quiero un telefono para jugar videojuegos
      '
      """
    #--------------------------------------------
    agent1 = '746b80b6-445f-43c4-b189-9f647d702abe'
    agente1 = MyAgent(agent1)

    res = agente1.get_response(prompt)

    alex = re.search("Alex", res)
    sandra = re.search("Sandra", res)
    if alex:
        print("alex")

    elif sandra:
        print('sandra')
    else:
        print("No match")

    #---------------------- end agente 1 ----------------------------

    #res = chatbot(message = req_info['data'])
    #res = 'esto es una prueba con capybara'

    #print(await request.body())
    #return {"data": await request.json()}
    return res

@app.get("/shopping-card-api")
async def get_card():
    with open("product.json", "r") as read_file:
        items = json.load(read_file)

    return {"items": items}