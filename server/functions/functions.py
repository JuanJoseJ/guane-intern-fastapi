
# fn que busca perros en una lista por su nombre y regresa los resultados encontrados
def buscar_nombre(dogs, name):
    matches = []
    for dog in dogs:
        if dog.name == name:
            matches.append(dog)
    return matches

# fn que busca perros adoptados en una lista
def buscar_adoptados(dogs):
    matches = []
    for dog in dogs:
        if dog.is_adopter:
            matches.append(dog)
    return matches