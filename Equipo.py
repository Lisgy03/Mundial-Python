
class Equipo:
    def __init__(self, nombre, entrenador, jugadores):
        self.__nombre = nombre
        self.__entrenador = entrenador
        self.__jugadores = jugadores


    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_entrenador(self):
        return self.__entrenador

    def set_entrenador(self, entrenador):
        self.__entrenador = entrenador

    def get_jugadores(self):
        return self.__jugadores

    def set_jugadores(self, jugadores):
        self.__jugadores = jugadores


