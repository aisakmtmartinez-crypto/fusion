class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Mi nombre es {self.nombre}, mi edad es {self.edad}"
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        #si usamos super, no debe llevar self adentro de los atributos, pero si no lo usamos
        #y ponemos el nombre de la clase directamente, si usar self
        super().__init__(nombre,edad)
        self.grado = grado

    def __str__(self):
        return f"Hola {super().__str__()} y mi grado es {self.grado}"

estudiante = Estudiante("Alan",21,"Decimo cuatrimestre")
print(estudiante)