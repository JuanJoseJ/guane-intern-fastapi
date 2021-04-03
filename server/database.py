import os
from pymongo import MongoClient

# Es posible cambiar los valores por los de la db que se sete utilizando
# pero se recomienda hacerlo desde el entorno.
# Nota: La variable de entorno de la URL no esta siendo usada pero puede ser configurada

client = MongoClient(host=os.environ.get("MONGODB_HOST"), port=int(os.environ.get("MONGODB_PORT")))
db = client[os.environ.get("MONGODB_NAME")]