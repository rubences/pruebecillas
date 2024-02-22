class Pelicula:
    def __init__(self, titulo, duracion, anio):
        self.titulo = titulo
        self.duracion = duracion
        self.anio = anio

    def __str__(self):
        return f"{self.titulo} ({self.anio}), {self.duracion} minutos"
