class Objetos:
    def __init__(self,precio,cantidad):
        self.precio = precio
        self.cantidad = cantidad
    def __repr__(self):
        return f"{self.precio} - {self.cantidad}"
    
    def __str__(self):
        return f"Representacion bonita Precio: {self.precio} y {self.cantidad}"