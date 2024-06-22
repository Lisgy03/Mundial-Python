class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__capacidad = capacidad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_ciudad(self):
        return self.__ciudad

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def get_capacidad(self):
        return self.__capacidad

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self.__nombre}, Ciudad: {self.__ciudad}, Capacidad: {self.__capacidad}"
