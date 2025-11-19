class Persona():
    def __init__(self, nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola, estoy hablando un poco")
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,escuela,promedio):
        super().__init__(nombre,edad,nacionalidad)
        self.escuela = escuela
        self.promedio = promedio
class Jefe(Persona):
    def __init__(self,nombre,edad,nacionalidad,empresa,ganancias):
        super().__init__(nombre,edad,nacionalidad)
        self.empresa = empresa
        self.ganancias = ganancias
    def __str__(self):
        return f"Soy {self.nombre}, con la edad {self.edad}, de la empresa {self.empresa}"
        
        
    def hacer_ganancias(self):
        print(f"Estoy haciendo ganancias con la empresa {self.empresa}")
        
        
roberto = Empleado("Isaac",21,"mexicano","full-stack",20000)
roberto.hablar()
print(roberto.nombre)

antonio = Jefe("Antonio", 70,"mexicano","IMSS", 100000)
print(antonio)
antonio.hacer_ganancias()
