


class Persona():
    especie = "Humano" #Atributo de clase(para todos)
    def __init__(self,sexo,nombre,edad,peso):
        #Atributos de instancia
        self.sexo= sexo
        self.nombre = nombre
        self.edad =edad
        self.peso = peso

persona1 = Persona("Hombre","Alan",21,"60kg")
persona2 = Persona("Mujer","Marlen",45,"80kg")

print(persona1.especie, persona1.nombre)
print(persona2.especie, persona2.nombre)

class Celular():
    #este es el metodo contructor
    def __init__(self, marca, modelo, camara):
        #Son ATRIBUTOS DE INSTANCIA, se los pasamos cuando instanciamos el objeto
        #self se refiere al objeto que pasamos en ese momento
        self.marca= marca
        self.modelo= modelo
        self.camara= camara
    #Estos son metodos, como parametro debemos de pasarle siempre el self
    #para que sepa al momento de ser llamado, a que objeto se esta referenciando 
    
    def llamar(self):
        #Sin self, no podria acceder al modelo del celular2, o al que llame al metodo
        print(f"Estas haciendo la llamada desde un modelo: {self.modelo}")
    def cortar(self):
        print(f"Estas colgando la llamada desde un modelo: {self.modelo}")

#este es el objeto

celular1= Celular("Samsung","S23","48MP")#Pasar argumentos, no necesitamos pasar el self
                                        #se pasa solo
celular2= Celular("Apple","Iphone 15","96MP")

#Ahora tenemos variables distintas en cada ojbeto
print(celular1.modelo)
print(celular2.modelo)

celular2.llamar()

