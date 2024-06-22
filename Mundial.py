from Equipo import Equipo
from Grupo import Grupo
from Estadio import Estadio
from Partido import Partido
import random

class Mundial:
    def __init__(self):
        self.equipos = []
        self.grupos = []
        self.estadios = []
        self.fixture = []

    def registrar_equipo(self, equipo):
        self.equipos.append(equipo)

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def generar_fixture(self):
        equipos_copy = self.equipos[:]

        while len(equipos_copy) > 1:
            equipo1 = equipos_copy.pop(0)
            for equipo2 in equipos_copy:
                partido = Partido(equipo1, equipo2)
                self.fixture.append(partido)

    def jugar_partidos(self):
        for partido in self.fixture:
            partido.jugar_partido()

    def mostrar_fixture(self):
        resultados = []
        for partido in self.fixture:
            resultados.append(partido.mostrar_resultado())
        return "\n".join(resultados)
