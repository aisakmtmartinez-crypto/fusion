class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre= nombre
        self.edad=edad
        self.grado=grado
        
    def estudiar(self):
        print(f"estudiando pa...")
        
name = input("¿Cual es el nombre del estudiante? ")
age = input("¿Cual es la edad del estudiante? ")
grade = input("¿Cual es el grado del estudiante? ")

estudiante1 = Estudiante(name,age,grade)
print(f"""

DATOS DEL ESTUDIANTE:

    Nombre: {estudiante1.nombre}
    Edad: {estudiante1.edad}
    Grade: {estudiante1.grado}
    """)
while True:
    decision = input(f"Quieres que estudie? Escribe (estudiar)").lower()
    if decision == "estudiar":
        estudiante1.estudiar()
        
    else: print("deberias hacerlo")
    break