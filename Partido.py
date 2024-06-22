class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.jugado = False

    def jugar_partido(self, goles_equipo1, goles_equipo2):
        self.goles_equipo1 = goles_equipo1
        self.goles_equipo2 = goles_equipo2
        self.jugado = True

    def mostrar_resultado(self):
        if self.jugado:
            resultado = f"{self.equipo1.get_nombre()} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo2.get_nombre()}"
        else:
            resultado = f"{self.equipo1.get_nombre()} vs {self.equipo2.get_nombre()} - Aún no se ha jugado"
        return resultado

    def get_goles_equipo1(self):
        return self.goles_equipo1

    def get_goles_equipo2(self):
        return self.goles_equipo2

    def get_ganador(self):
        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo1
        elif self.goles_equipo2 > self.goles_equipo1:
            return self.equipo2
        else:
            return None
