import os
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from datetime import date
from .models.dog import Dog
from .database import db
from .static.functions import buscar_nombre, buscar_adoptados
import requests
from pymongo import MongoClient, UpdateOne
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
    for dog in db.dogs.find({"is_adopted": True}):
        dogs.append(Dog(**dog))
    return dogs


# Buscar perros por su nombre. Regresa una lista


@app.get("/dogs/{name}")
async def read_name(name: str):
    dogs = []
    for dog in db.dogs.find({"name": name}):
        dogs.append(Dog(**dog))
    return dogs


# Para crear un registro de un perro


@app.post("/dogs/{name}")
async def create_dog(name: str, is_adopted: bool = False):
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


# Metodo con el que se puede actualizar un registro
# Nota: El unico campo obligatorio es el nombre, de manera que queda al usuario actualizar lo que se desee
# Nota2: Como el nombre no necesariamente es único, si el nombre esta repetido, se requiere la id


@app.put("/dogs/{name}")
async def update_dog(name: str, new_name: Optional[str] = None, is_adopted: Optional[bool] = None, picture: Optional[str] = None, id: Optional[str] = None):
    dogs = []
    for dog in db.dogs.find({"name": name}):
        dogs.append(Dog(**dog))

    # Se debe verificar que se este tratando con el registro correcto
    # por lo que se verifica el numero de registros encontrados, si se requiere una ID y si esta es valida.
    # Se requiere una id si hay más de un a registro con el nombre buscado

    if len(dogs) > 1:
        if id:
            if len(id) == 24:
                dogs = []
                for dog in db.dogs.find({"_id": ObjectId(id)}):
                    dogs.append(Dog(**dog))
                if len(dogs) == 0:
                    raise HTTPException(
                        status_code=404, detail="No hay registros con la ID '"+id+"' y el nombre '"+name+"'")
            else:
                raise HTTPException(
                    status_code=422, detail="La ID debe tener 24 caracteres pero tiene "+str(len(id)))

        else:
            raise HTTPException(status_code=300, detail="Varios registros con el nombre '" +
                                name+"' encontrados. Se requiere especificar una ID")
    elif len(dogs) < 1:
        raise HTTPException(
            status_code=404, detail="Registro no encontrado con el nombre '"+name+"'")

    # Se actualizan los datos segun los parametros pasados

    match = dogs[0]
    requests = []

    if is_adopted is not None:
        match.is_adopted = is_adopted
        requests.append(UpdateOne({"_id": ObjectId(match.id)}, {
                        "$set": {"is_adopted": is_adopted}}))

    if picture:
        match.picture = picture
        requests.append(UpdateOne({"_id": ObjectId(match.id)}, {
                        "$set": {"picture": picture}}))

    if new_name:
        match.name = new_name
        requests.append(UpdateOne({"_id": ObjectId(match.id)}, {
                        "$set": {"name": new_name}}))

    res = db.dogs.bulk_write(requests)

    return match


# Metodo con el que se puede eliminar un registro
# Nota: El unico campo obligatorio es el nombre, pero se puede requerir una id
# Nota2: Como el nombre no necesariamente es único, si el nombre esta repetido, se requiere la id


@app.delete("/dogs/{name}")
async def delete_dog(name: str, id: Optional[str] = None):
    dogs = []
    for dog in db.dogs.find({"name": name}):
        dogs.append(Dog(**dog))

    # Se debe verificar que se este tratando con el registro correcto
    # por lo que se verifica el numero de registros encontrados, si se requiere una ID y si esta es valida.
    # Se requiere una id si hay más de un a registro con el nombre buscado

    if len(dogs) > 1:
        if id:
            if len(id) == 24:
                dogs = []
                for dog in db.dogs.find({"_id": ObjectId(id)}):
                    dogs.append(Dog(**dog))
                if len(dogs) == 0:
                    raise HTTPException(
                        status_code=404, detail="No hay registros con la ID '"+id+"' y el nombre '"+name+"'")
            else:
                raise HTTPException(
                    status_code=422, detail="La ID debe tener 24 caracteres pero tiene "+str(len(id)))

        else:
            raise HTTPException(status_code=300, detail="Varios registros con el nombre '" +
                                name+"' encontrados. Se requiere especificar una ID")
    elif len(dogs) < 1:
        raise HTTPException(
            status_code=404, detail="Registro no encontrado con el nombre '"+name+"'")

    # Se actualizan los datos segun los parametros pasados

    match = dogs[0]

    res = db.dogs.delete_one({"_id": ObjectId(match.id)})

    return match
