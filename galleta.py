class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color

    def __str__(self):
       return f"Soy una galleta {self.color} y {self.sabor}."

galleta = Galleta("dulce", "blanca")

print(galleta)
print(str(galleta))
print(galleta.__str__())









