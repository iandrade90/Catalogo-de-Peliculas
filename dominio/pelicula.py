class Pelicula():
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return str(self.__nombre)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self):
        self.__nombre = nombre
