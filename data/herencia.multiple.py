class SerVivo():
    def hablar(self):
        print("Hola, estoy hablando como ser vivo")
        
class Persona(SerVivo):
    def __init__(self, nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    
        
class  Artista(Persona):
    def __init__(self,nombre):
        self.nombre =nombre
        
    
        
    def mostrar_habilidad(self):
        return f"Mi hability es: {self.nombre}"
    
class Empleado(SerVivo):
    def hablar(self):
        print("Hola, estoy hablando como empleado")
        
class Perro(Empleado):
    def __init__(self):
        self.habilidad= None
        
    def mostrar_habilidad(self, habilidad):
        self.habilidad = habilidad
        return f"Mi habilidad es {habilidad}"
        
class EmpleadoArtista(Perro,Artista):
    def __init__(self,nombre,salario,empresa):
        Perro.__init__(self)
        Artista.__init__(self,nombre)
        self.salario =salario
        self.empresa = empresa
        
    
        
    def presentarse(self):
        print (f"Hola soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}")
    

chock = Perro()
hol= chock.mostrar_habilidad("ladrar")
print(hol)


