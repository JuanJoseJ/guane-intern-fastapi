from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from .models import Dog
from .functions.functions import buscar_nombre, buscar_adoptados

app = FastAPI()


temporal_dog_database = []

# Como "/" no esta en uso, se  rediriga a "/docs" 
@app.get("/")
def redirect():
    return RedirectResponse(url='/docs')

# Obtener una listado de los perros
@app.get("/dogs")
def read_dogs():
    return temporal_dog_database

@app.get("/dogs/{name}")
def read_name(name:str):
    matches = buscar_adoptados(temporal_dog_database)
    return matches

