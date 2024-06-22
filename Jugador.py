class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.__nombre = nombre
        self.__edad = edad
        self.__posicion = posicion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_posicion(self):
        return self.__posicion

    def set_posicion(self, posicion):
        self.__posicion = posicion

    def mostrar_info(self):
        return f"Jugador: {self.__nombre}, Edad: {self.__edad}, Posición: {self.__posicion}"
