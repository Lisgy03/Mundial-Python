import tkinter as tk
from tkinter import messagebox, ttk
from Equipo import Equipo
from Estadio import Estadio
from Grupo import Grupo
from Partido import Partido
from Mundial import Mundial
import random

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Mundial de Fútbol")
        self.root.geometry("600x400")
        self.root.configure(bg='#d0f0c0')  # Fondo verde suave

        self.mundial = Mundial()

        self.create_equipo_widgets()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_equipo_widgets(self):
        self.clear_frame()
        frame = tk.LabelFrame(self.root, text='Registrar Equipos', padx=10, pady=10, bg='#d0f0c0')
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Cargar y mostrar la imagen en la parte superior
        try:
            self.img = tk.PhotoImage(file="balon.png")
            self.img = self.img.subsample(4, 4)  # Reducir el tamaño de la imagen
            tk.Label(frame, image=self.img, bg='#d0f0c0').grid(row=0, column=0, columnspan=2, pady=10)
        except Exception as e:
            messagebox.showerror("Error al cargar la imagen", str(e))

        tk.Label(frame, text='Equipo 1 - Nombre:', bg='#d0f0c0').grid(row=1, column=0, padx=5, pady=2, sticky='e')
        self.nombre_equipo1_entry = tk.Entry(frame, width=25)
        self.nombre_equipo1_entry.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame, text='Equipo 1 - Entrenador:', bg='#d0f0c0').grid(row=2, column=0, padx=5, pady=2, sticky='e')
        self.entrenador_equipo1_entry = tk.Entry(frame, width=25)
        self.entrenador_equipo1_entry.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(frame, text='Equipo 2 - Nombre:', bg='#d0f0c0').grid(row=3, column=0, padx=5, pady=2, sticky='e')
        self.nombre_equipo2_entry = tk.Entry(frame, width=25)
        self.nombre_equipo2_entry.grid(row=3, column=1, padx=5, pady=2)

        tk.Label(frame, text='Equipo 2 - Entrenador:', bg='#d0f0c0').grid(row=4, column=0, padx=5, pady=2, sticky='e')
        self.entrenador_equipo2_entry = tk.Entry(frame, width=25)
        self.entrenador_equipo2_entry.grid(row=4, column=1, padx=5, pady=2)

        tk.Button(frame, text='Registrar Equipos', command=self.registrar_equipos, bg='#7cbf7c').grid(row=5, columnspan=2, padx=5, pady=10)

    def registrar_equipos(self):
        nombre_equipo1 = self.nombre_equipo1_entry.get()
        entrenador1 = self.entrenador_equipo1_entry.get()
        equipo1 = Equipo(nombre_equipo1, entrenador1, [])
        self.mundial.registrar_equipo(equipo1)

        nombre_equipo2 = self.nombre_equipo2_entry.get()
        entrenador2 = self.entrenador_equipo2_entry.get()
        equipo2 = Equipo(nombre_equipo2, entrenador2, [])
        self.mundial.registrar_equipo(equipo2)

        messagebox.showinfo("Equipos Registrados", f"Se han registrado los equipos {nombre_equipo1} y {nombre_equipo2} con éxito.")
        self.create_grupo_widgets()

    def create_grupo_widgets(self):
        self.clear_frame()
        frame = tk.LabelFrame(self.root, text='Registrar Grupo', padx=10, pady=10, bg='#d0f0c0')
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(frame, text='Selecciona el Grupo:', bg='#d0f0c0').grid(row=0, column=0, padx=5, pady=2, sticky='e')
        self.grupo_var = tk.StringVar()
        self.grupo_combobox = ttk.Combobox(frame, textvariable=self.grupo_var, values=["A", "B", "C", "D", "E", "F"], state="readonly", width=23)
        self.grupo_combobox.grid(row=0, column=1, padx=5, pady=2)

        tk.Button(frame, text='Registrar Grupo', command=self.registrar_grupo, bg='#7cbf7c').grid(row=1, columnspan=2, padx=5, pady=10)

    def registrar_grupo(self):
        nombre_grupo = self.grupo_var.get()
        grupo = Grupo(nombre_grupo, [])
        self.mundial.registrar_grupo(grupo)
        messagebox.showinfo("Grupo Registrado", f"Se ha registrado el grupo {nombre_grupo} con éxito.")
        self.create_estadio_widgets()

    def create_estadio_widgets(self):
        self.clear_frame()
        frame = tk.LabelFrame(self.root, text='Registrar Estadio', padx=10, pady=10, bg='#d0f0c0')
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(frame, text='Nombre del Estadio:', bg='#d0f0c0').grid(row=0, column=0, padx=5, pady=2, sticky='e')
        self.nombre_estadio_entry = tk.Entry(frame, width=25)
        self.nombre_estadio_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame, text='Ciudad del Estadio:', bg='#d0f0c0').grid(row=1, column=0, padx=5, pady=2, sticky='e')
        self.ciudad_estadio_entry = tk.Entry(frame, width=25)
        self.ciudad_estadio_entry.grid(row=1, column=1, padx=5, pady=2)

        tk.Button(frame, text='Registrar Estadio', command=self.registrar_estadio, bg='#7cbf7c').grid(row=2, columnspan=2, padx=5, pady=10)

    def registrar_estadio(self):
        nombre_estadio = self.nombre_estadio_entry.get()
        ciudad_estadio = self.ciudad_estadio_entry.get()
        estadio = Estadio(nombre_estadio, ciudad_estadio, 50000)
        self.mundial.registrar_estadio(estadio)
        messagebox.showinfo("Estadio Registrado", f"Se ha registrado el estadio {nombre_estadio} en {ciudad_estadio} con éxito.")
        self.create_fixture_widgets()

    def create_fixture_widgets(self):
        self.clear_frame()
        frame = tk.LabelFrame(self.root, text='Gestión de Fixture', padx=10, pady=10, bg='#d0f0c0')
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Button(frame, text='Generar Fixture', command=self.generar_fixture, bg='#7cbf7c').grid(row=0, column=0, padx=5, pady=10)
        tk.Button(frame, text='Mostrar Resultados', command=self.mostrar_resultados, bg='#7cbf7c').grid(row=0, column=1, padx=5, pady=10)

        self.resultados_text = tk.Text(frame, height=10, width=60)
        self.resultados_text.grid(row=1, columnspan=2, padx=10, pady=10)

    def generar_fixture(self):
        self.mundial.generar_fixture()
        messagebox.showinfo("Fixture Generado", "Se ha generado el fixture correctamente.")

    def mostrar_resultados(self):
        detalles_mundial = ""

        detalles_mundial += "Grupos:\n"
        for grupo in self.mundial.grupos:
            detalles_mundial += f"Grupo {grupo.get_nombre()}:\n"
            if grupo.get_equipos():
                for equipo in grupo.get_equipos():
                    detalles_mundial += f" - {equipo.get_nombre()}, Entrenador: {equipo.get_entrenador()}\n"
        else:
            detalles_mundial += " - Aún por definir\n"
        detalles_mundial += "\n"

        detalles_mundial += "Estadios:\n"
        for estadio in self.mundial.estadios:
            detalles_mundial += f" - {estadio.get_nombre()} en {estadio.get_ciudad()}, Capacidad: {estadio.get_capacidad()}\n"
            detalles_mundial += "\n"

            detalles_mundial += "Resultados de los Partidos:\n"
            for partido in self.mundial.fixture:
                if partido.jugado:
                    detalles_mundial += f"Partido entre {partido.equipo1.get_nombre()} y {partido.equipo2.get_nombre()}: "
                    detalles_mundial += f"{partido.goles_equipo1} - {partido.goles_equipo2}\n"
        else:
            detalles_mundial += f"Partido entre {partido.equipo1.get_nombre()} y {partido.equipo2.get_nombre()}: Aún no se ha jugado\n"

            self.resultados_text.delete('1.0', tk.END)
            self.resultados_text.insert(tk.END, detalles_mundial)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='#d0f0c0')
    app = Interfaz(root)
    root.mainloop()
