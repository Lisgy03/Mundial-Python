class Grupo:
    def __init__(self, nombre, equipos):
        self.__nombre = nombre
        self.__equipos = equipos

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_equipos(self):
        return self.__equipos

    def set_equipos(self, equipos):
        self.__equipos = equipos

    def agregar_equipo(self, equipo):
        self.__equipos.append(equipo)

    def mostrar_info(self):
        if not self.__equipos:
            return f"Grupo: {self.__nombre}, Equipos: []"

        info_equipos = ", ".join(equipo.mostrar_info() for equipo in self.__equipos)
        return f"Grupo: {self.__nombre}, Equipos: {info_equipos}"
