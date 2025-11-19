class Persona():
    def __init__(self, nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")
        

        
class  Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        #Si aqui lo dejo como print en vez de retornar, al momento de llamar el metodo al objeto 
        #roberto, solo mostrar mi habilidad es... En vez de todo el txt que tiene el metodo
        #presentarse de EmpleadoArtista, con return, devuelve esa cadena pero no la imprime
        return f"Mi habilidad es: {self.habilidad}"


#HERENCIA MULTIPLE DE PERSONA Y ARTISTA
class EmpleadoArtista(Persona, Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        #En vez de usar super, llamamos directamente a los constructores de las clases
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario =salario
        self.empresa = empresa
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
    def presentarse(self):
        #Aqui si podria dejarlo como print, si quiero que salga en pantalla sin que tenga 
        #que meterlo en una variable e imprimirla.
    
        #Lo mejor es usar super() para llamar a metodos de otras clases que heredas, no self
        #al usar self, si tenemos un metodo con mismo nombre en esta clase, elegira ese
        print (f"Hola soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}")
    
roberto = EmpleadoArtista("Alan", 21,"mexicano","Cantar",20000,"TEC")
presentacion = roberto.presentarse()



#FUNCIONES PARA VER SI HEREDA UNA CLASE DE OTRA PADRE, Y VER SI UN OBJETO ES INSTANCIA
#DE UNA CLASE
herencia = issubclass(EmpleadoArtista, Persona)

#Como EmpleadoArtista es subclase de Artista y Persona, tambien dara True como instancia
# de esas clases, porque hereda de ellas.
instancia = isinstance(roberto, EmpleadoArtista) #PERSONA / ARTISTA TRUE

#instancia = isinstance(roberto, Jefe) #False
print(herencia)
print(instancia)