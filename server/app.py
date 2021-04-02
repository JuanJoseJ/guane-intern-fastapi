import os
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from datetime import date
from .models.dog import Dog, db
from .static.functions import buscar_nombre, buscar_adoptados
import requests
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

picture_url = 'https://dog.ceo/api/breeds/image/random'

# Como "/" no esta en uso, se  rediriga a "/docs"


@app.get("/")
def redirect():
    return RedirectResponse(url='/docs')

# Obtener una listado de los perros


@app.get("/dogs")
async def read_dogs():
    dogs = []
    for dog in db.dogs.find():
        dogs.append(Dog(**dog))
    return dogs

# Buscar perros adoptados. Regresa una lista
# Nota: este llamado debe ir antes que el de los nombres pues se pueden cruzar

@app.get("/dogs/is_adopted")
async def read_adopted():
    dogs = []
    for dog in db.dogs.find({"is_adopted":True}):
        dogs.append(Dog(**dog))
    return dogs

# Buscar perros por su nombre. Regresa una lista


@app.get("/dogs/{name}")
async def read_name(name: str):
    dogs = []
    for dog in db.dogs.find({"name":name}):
        dogs.append(Dog(**dog))
    return dogs


# Para crear un registro de un perro


@app.post("/dogs/{name}")
async def create_item(name: str, is_adopted: bool = False):
    picture = requests.get(picture_url).json()
    dog = {
        "name": name,
        "picture": picture['message'],
        "create_date": str(date.today()),
        "is_adopted": is_adopted
    }
    res = db.dogs.insert_one(dog)
    dog["_id"] = str(res.inserted_id)
    return dog
