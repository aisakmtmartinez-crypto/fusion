class Escuela:
    def __init__(self, nombre):
        self.nombre= nombre
        self.profesores = []
        self.bibliotecas=[]
        
    def buscar_profesor(self, nombre):
        for profesor in self.profesores:
            if profesor.nombre.lower() == nombre.lower():
                return profesor
        return None

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)
        print(f"✅ Agregado profesor {profesor.nombre}")
        
    def listar_profesores(self):
        if not self.profesores:
            print(f"No hay ningun profesor en la escuela{self.nombre}")
        for profesor in self.profesores:
            print(profesor.nombre)
    
    
    def agregar_biblioteca(self, biblioteca):
        self.bibliotecas.append(biblioteca)
        print(f"✅ Biblioteca agregada {biblioteca.nombre} ")
    
    def listar_bibliotecas(self):
        bandera = True
        if not self.bibliotecas:
            print(f"No hay ninguna biblioteca en la escuela {self.nombre}")
            bandera = False
            return bandera 
        for biblio in self.bibliotecas:
            print(biblio.nombre)
            
    def buscar_biblioteca(self, nombre):
        for biblio in self.bibliotecas:
            if biblio.nombre.lower() == nombre.lower():
                return biblio
            
    def profesores_en_bibliotecas(self, opcion = False, Nombre = None):
        for p in self.profesores:
            if p.biblioteca:
                print(f"El profesor {p.nombre} esta en la biblioteca {p.biblioteca.nombre}")
        if opcion == True:
            for p in self.profesores:
                if p.biblioteca.nombre.lower() == Nombre.lower():
                    print(f"Profesor {p.nombre} en biblioteca {p.biblioteca.nombre}")
                
    # codigo optimizado
    
    def profesores_en_bibliotecas(self, filtro=False, nombre_biblioteca=None):
        if not self.profesores:
            print("❌ No hay profesores registrados.")
            return

        encontrados = False
        for profesor in self.profesores:
            if profesor.biblioteca:
                if not filtro:
                    print(f"👨‍🏫 {profesor.nombre} está en la biblioteca {profesor.biblioteca.nombre}")
                    encontrados = True
                elif filtro and profesor.biblioteca.nombre.lower() == nombre_biblioteca.lower():
                    print(f"👨‍🏫 {profesor.nombre} pertenece a la biblioteca {profesor.biblioteca.nombre}")
                    encontrados = True

        if not encontrados:
            if filtro:
                print(f"❌ No hay profesores en la biblioteca '{nombre_biblioteca}'.")
            else:
                print("❌ Ningún profesor tiene biblioteca asignada.")

        
if __name__== "__main__":
    pass