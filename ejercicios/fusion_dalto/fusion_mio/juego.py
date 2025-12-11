class Juego:
    def __init__(self):
        self.personajes = []
        
    def agregar_personaje(self,personaje):
        self.personajes.append(personaje)
        print("Personaje creado con exito")
    
    # permitir for-in, Permite hacer: for p in juego
    def __iter__(self):
        return iter(self.personajes)

    # permitir indices y slices  Permite hacer: juego[0], juego[1:3], etc.
    def __getitem__(self, index):
        return self.personajes[index]
    
     # Permite hacer: len(juego)
    def __len__(self):
        return len(self.personajes)
    
    #Eso no funciona porque hace la comprobacion de los dos en cada nombre, no uno y uno
    # def encontrar_personaje(self,nombres):
    #     per1, per2 = nombres
    #     for p in self.personajes:
    #         if per1 in p.nombre and per2 in p.nombre:
    #             print("Si estan")
    #         else: print("no estan")
    
    #ESTA FUNCION SOLO SIRVE SI SON DOS PERSONAJES
    # def encontrar_personaje(self, nombres):
    #     per1, per2 = nombres  #ESTO ES UN TIPO DE SLICE DESESTRUCTURADO
    #     personajes = []
    #     for p in self.personajes:
    #         if per1 in p.nombre:
    #             print([per1, p.nombre])
    #             personajes.append(p)
            
    #         if per2 in p.nombre:
    #             print([per2, p.nombre])
    #             personajes.append(p)
            
            
    #     return personajes

    #ESTA FUNCION SIRVE CON N PERSONAJES, LOS QUE YO QUIERA METER
    def encontrar_personajes(self, nombres):
        encontrados = []
        
        for nombre_buscado in nombres:
            encontrado = None
            
            for p in self.personajes:
                if nombre_buscado == p.nombre:
                    encontrado = p
                    break
            
            if encontrado:
                encontrados.append(encontrado)
            else:
                print(f"No se encontró el personaje: {nombre_buscado}")
        
        return encontrados

    #NO ES NECESARIO SI USAMOS GETITEM E ITER METODOS ESPECIALES
    # def mostrar_personajes(self):
    #     for p in self.personajes:
    #         print(p)
    
    def mostrar_cantidad(self):
        print(len(self.personajes))
        
    def mostrar_personaje(self):
        print("Segun es una funcion para mostrar para mostrar personajes")
        self.personajes