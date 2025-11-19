class Animal():
    def comer():
        print("El animal Estoy comiendo")
        
class Mamifero(Animal):
    def amamantar():
        print("El animal Estoy amamantando")
        
class Ave(Animal):
    def volar():
        print("El animal Estoy volando")
    
class Murcielago(Mamifero, Ave):
    #como no hay atributos en clases padres, no le pasamos los super o sus 
    # atributos de las demas clases
    pass

batman = Murcielago()