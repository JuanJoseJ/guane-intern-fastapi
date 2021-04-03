
from pydantic import BaseModel, Field
from bson import ObjectId


# Para usar mongodb se requiere poder manejar ObjectIDs como pk
# El metodo siguiente funciona como parser de este tipo para pydantic


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

# Modelo base para los perros
# uso este alias porque mongo lo requiere


class Dog(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str
    picture: str
    create_date: str
    is_adopted: bool

    # Se requiere esta clase para pydantic acepte PyObjectId en el modelo

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
