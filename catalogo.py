from pelicula import Pelicula

class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)


p = Pelicula("El Padrino", 175, 1972)
c = Catalogo([p])
c.mostrar()
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))
c.mostrar()
c.agregar(Pelicula("El Padrino: Parte 3", 162, 1990))
c.mostrar()


