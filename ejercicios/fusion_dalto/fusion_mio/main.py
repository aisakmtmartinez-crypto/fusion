from personajes_mio import Personaje
from juego import Juego

juego = Juego()
print("--------------------------------------------")
print("Bienvenido al juego fusion de personajes")
print("--------------------------------------------")

while True:
    
    print("1. Crear personaje")
    print("2. Fusionar personajes")
    print("3. Mostrar personajes")
    print("4. Salir")
    opcion = input("Selecciona una opcion: ")
    
    if opcion == "1":
        nombre = input("Dame su nombre: ").capitalize()
        fuerza = int(input("Dame su fuerza: "))
        velocidad = int(input("Dame su velocidad: "))
        
        per = Personaje(nombre, fuerza, velocidad)
        juego.agregar_personaje(per)
        
    
    elif opcion == "2":
        nombre_uno = input("Dame el nombre del primer personaje: ").capitalize()
        nombre_dos = input("Dame el nombre del segundo personaje: ").capitalize()
        nombres = [nombre_uno, nombre_dos]
        encontrado= juego.encontrar_personaje(nombres)
        res= encontrado[0]+ encontrado [1]
        print(res)
    elif opcion == "3":
        juego.mostrar_personajes()
        
    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else: print("Elige una opcion correcta")