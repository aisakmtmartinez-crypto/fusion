#Objetivo: practicar clases, atributos, métodos y constructores.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def calcular_total(self):
        return self.precio * self.cantidad

    #__str__ Permite impirmir objetos de forma legible
    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Cantidad: {self.cantidad}"
