class Profesor:
    def __init__(self, nombre, biblioteca=None):
        self.nombre = nombre
        self.biblioteca = biblioteca  # puede o no tener una al inicio

    def asignar_biblioteca(self, biblioteca):
        self.biblioteca = biblioteca
        print(f"Se le asignó la biblioteca {biblioteca.nombre} a {self.nombre}")
        
    def consultar_libros(self):
        if self.biblioteca:
            print(f"\n👨‍🏫 {self.nombre} consulta los libros de {self.biblioteca.nombre}:")
            self.biblioteca.mostrar_libros()
        else:
            print(f"{self.nombre} no tiene biblioteca asignada.")

    
        