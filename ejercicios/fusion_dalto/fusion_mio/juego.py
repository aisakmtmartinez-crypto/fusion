class Juego:
    def __init__(self):
        self.personajes = []
        
    def agregar_personaje(self,personaje):
        self.personajes.append(personaje)
        print("Personaje creado con exito")
        
    #Eso no funciona porque hace la comprobacion de los dos en cada nombre, no uno y uno
    # def encontrar_personaje(self,nombres):
    #     per1, per2 = nombres
    #     for p in self.personajes:
    #         if per1 in p.nombre and per2 in p.nombre:
    #             print("Si estan")
    #         else: print("no estan")
    
    
    def encontrar_personaje(self, nombres):
        per1, per2 = nombres
        personajes = []
        for p in self.personajes:
            if per1 in p.nombre:
                print([per1, p.nombre])
                personajes.append(p)
            
            if per2 in p.nombre:
                print([per2, p.nombre])
                personajes.append(p)
            
            
        return personajes

    def mostrar_personajes(self):
        for p in self.personajes:
            print(p)