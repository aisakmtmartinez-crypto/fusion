#from libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"\n✅ {libro} fue agregado a {self.nombre}\n")
        print(self.libros)
        
    def mostrar_libros(self):
        
        print(f"\nBiblioteca {self.nombre}\n")
        
        if not self.libros:
            print("Aun no hay libros")
            return
        else:
            print(f"Cantidad de libros: {len(self.libros)}")
            for libro in self.libros:
                print(libro)
                
        