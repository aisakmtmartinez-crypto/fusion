class Objetos:
    def __init__(self,precio,cantidad):
        self.precio = precio
        self.cantidad = cantidad
    def __repr__(self):
        return f"{self.precio} - {self.cantidad}"