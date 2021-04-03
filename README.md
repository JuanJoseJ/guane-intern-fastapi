

<h3 align="center">guane-intern-fastapi</h3>

---

<p align="center"> Este proyecto es una prueba técnica de backend para la empresa Guane. Hace parte del CRUD de una aplicación que almacena información sobre perros.
    <br> 
</p>

## 📝 Table of Contents

- [Prerequisitos](#prerequisitos)
- [Configuracion Inicial](#getting_started)
- [Pruebas](#tests)
- [Programas utilizados](#built_using)
- [Autos](#authors)
- [Reconocimientos](#acknowledgement)

### Prerequisites <a name = "prerequisito"></a>

Para obtener una copia del proyecto solo se requiere descargarlo, una forma de hacer esto es con:
```
git clone https://github.com/JuanJoseJ/guane-intern-fastapi.git
```

Lo siguiente es instalar las dependencias del proyecto desde el Pipfile, para esto se requiere tener en su máquina [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html#example-pipenv-workflow). Se debe recordar hacerlo desde el directorio principal del proyecto y usando el siguiente comando:
```
pipenv install
```


## 🏁 Getting Started <a name = "getting_started"></a>

La base de datos utilizada para este proyecto es MongoDB, y se requiere configurar las variables de esta en el archivo .env que se encuentra acá, cambiando las variables de MONGODB_HOST, MONGODB_PORT y MONGODB_NAME por el nombre de host, puerto y nombre de la base de datos que se quiera utilizar.
**Importante**: Recuerde que la base de datos debe tener una colección llamada 'dogs' para funcionar.

En la carpeta de modelos queda adjunto un archivo llamado sampledb.json con el registro de varios documentos y que puede ser utilizado a modo de ejemplo para iniciar la colección.

Para más información sobre cómo crear una base de datos con MongoDB, dirigirse a los [Documentos Oficiales](https://www.mongodb.com/basics/create-database)

Una vez que se tenga configurada la base de datos en el entorno, es posible iniciar el mismo de la siguiente manera:
```
pipenv shell
```

Desde aquí se iniciara el programa con el archivo *main.py*, además, cada que se hagan actualizaciones en la aplicación, este se reiniciara para actualizarse a estas medidas.


## 🔧 Running the tests <a name = "tests"></a>

Con el programa corriendo es posible hacer los llamados a la api que esta configurada de manera predeterminada en *http://localhost:8000* y que redigirá a la documentación autogenerada por OpenAPI en el programa.
Desde este mismo puerto es posible ahcer todos los llamados de POST, GET, PUT y DELETE.

### Break down into end to end tests

Los posibles llamados que la aplicación maneja son los siguientes:

*(GET) http://localhost:8000/dogs : Obtener una listado de los perros registrados

*(GET) http://localhost:8000/dogs/{name} : Obtener una entrada a partir del nombre de un perro (Puede regresar varios perros)

*(GET) http://localhost:8000/dogs/is_adopted: Obtener todas las entradas donde la bandera is_adopted sea True

*(POST) http://localhost:8000/dogs/{name}: Guardar un registro según el esquema de perros. El campo picture se debe rellenar con una consulta al API externa https://dog.ceo/api/breeds/image/random

*(PUT) http://localhost:8000/dogs/{name}: Actualizar un registro según el nombre. Puede ser necesaria la id del perro en  caso de que el nombre este repetido

*(DELETE) http://localhost:8000/dogs/{name}: Borrar un registro según el nombre. Puede ser necesaria la id del perro en  caso de que el nombre este repetido

### And coding style tests

Algunos ejemplos de llamados a la API pueden ser:

*(GET) http://localhost:8000/dogs/Poker
  Regresa:
  ```
    {
    "_id": {
      "$oid": "6067729060536f56c8380a45"
    },
    "name": "Poker",
    "picture": "https://images.dog.ceo/breeds/bulldog-boston/n02096585_6238.jpg",
    "create_date": "2021-04-02",
    "is_adopted": true
    }
  ```

*(POST) http://localhost:8000/dogs/Canela:
  Regresa y se incluye en la base de datos:
  ```
    {
    "_id": {
      "$oid": "6067729060536f56c8380a45"
    },
    "name": "Poker",
    "picture": "https://images.dog.ceo/breeds/bulldog-boston/n02096585_6238.jpg",
    "create_date": "2021-04-02",
    "is_adopted": true
    }
  ```

*(PUT) http://localhost:8000/dogs/Lola?is_adopted=false
  Regresa y se actualiza en la abse de datos:
  ```
    {
    "_id": {
      "$oid": "6067729060536f56c8380a45"
    },
    "name": "Lola",
    "picture": "https://images.dog.ceo/breeds/bulldog-boston/n02096585_6238.jpg",
    "create_date": "2021-04-02",
    "is_adopted": false
    }
  ```

*(DELETE) http://localhost:8000/dogs/Rocky?id=6067729060536f56c8380a45
  Regresa y se elimina de la base de datos:
  ```
    {
    "_id": {
      "$oid": "6067729060536f56c8380a45"
    },
    "name": "Rocky",
    "picture": "https://images.dog.ceo/breeds/bulldog-boston/n02096585_6238.jpg",
    "create_date": "2021-04-02",
    "is_adopted": false
    }
  ```

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [FastAPI](https://fastapi.tiangolo.com/) - Server Framework
- [uvicorn](https://www.uvicorn.org/) - ASGI server

## ✍️ Authors <a name = "authors"></a>

- [@JuanJoseJ](https://github.com/JuanJoseJ) - Desarrollador de la API y aplicante

 Nota: Definitivamente contrataría a [@JuanJoseJ](https://github.com/JuanJoseJ)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Gracias a [Guane](http://guane.com.co/) por la oportunidad

