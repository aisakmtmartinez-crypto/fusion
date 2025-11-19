#Objetivo: practicar clases, atributos, métodos y constructores.

class Producto:
    def __init__(self,id, nombre, precio, cantidad):
        self.id= id
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def calcular_total(self):
        return self.precio * self.cantidad

    #__str__ Permite impirmir objetos de forma legible
    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Cantidad: {self.cantidad}"
    
    
        
        
        
class Consumibles(Producto):
    def __init__(self,id,nombre,precio,cantidad,unidad):
        super().__init__(id,nombre,precio,cantidad)
        self.unidad= unidad
        
    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.precio}, {self.cantidad}, {self.unidad}"
    
class Equipo(Producto):
    def __init__(self,id,nombre,precio,cantidad,numero_serie,estado = "Funcional"):
        super().__init__(id,nombre,precio,cantidad)
        self.numero_serie = numero_serie
        self.estado = estado
    
    def marcar_mantenimiento(self):
        self.estado = "En mantenimiento"
    
    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.precio}, {self.cantidad}, {self.numero_serie}, {self.estado}"
        
class Reactivo(Producto):
    def __init__(self,id,nombre,precio,cantidad,caducidad,peligrosidad):
        super().__init__(id,nombre,precio,cantidad)
        self.caducidad= caducidad
        self.peligrosidad = peligrosidad
    
    def esta_vencido(self, fecha_actual):
        if fecha_actual > self.caducidad:
            return "Ya no esta chido"
        else: return "No ha caducado"
    
    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.precio}, {self.cantidad}, {self.caducidad}, {self.peligrosidad}"
    

