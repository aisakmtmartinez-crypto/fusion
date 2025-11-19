from profesor import Profesor
from libro import Libro
from biblioteca import Biblioteca
from escuela import Escuela



esc = Escuela("Heroes")
while True:
    
    print("\nHaremos algunas cosas en este menu, presiona el numero correspondiente a la accion que prefieras\nPresiona 1. Agregar libro\nPresiona 2. Mostrar libros\nPresiona 3. Agregar nuevo profesor a escuela\nPresiona 4. Asignarle una biblioteca a algun profesor\nPresiona 5. Profesor consulte libros de la biblioteca\nPresiona 6. Salir del programa\nPresiona 7. Listar los profesores de la escuela Heroes\nPresiona 8. Añadir biblioteca a la escuela Heroes\nPresiona 9. Ver que profesores pertenecen a cierta biblioteca")
    
    opcion= input("Que eliges: ")
    
    if opcion == "1":
        bandera = esc.listar_bibliotecas()
        if bandera == False:
            print("No hay bibliotecas en donde agregar libros")
        else:
            eleccion = input("A que biblioteca quieres agregar el libro? Pon su nombre: ")
            existe = esc.buscar_biblioteca(eleccion)
            if existe:
                titulo = input("Dame el titulo del libro: ")
                autor = input("Dame el autor del libro: ")
                existe.agregar_libro(Libro(titulo,autor))
    elif opcion == "2":
        nombre = input("De que biblioteca quieres ver los libros: ")
        existe = esc.buscar_biblioteca(nombre)
        if existe:
            existe.mostrar_libros()
        
    elif opcion == "3":
        nombre = input("Dame el nombre del profesor: ")
        profe = Profesor(nombre)  
        esc.agregar_profesor(profe)
    elif opcion == "7":
        print("listamos")
        esc.listar_profesores()
        
    elif opcion == "4":
        esc.listar_profesores()
        nombre = input(f"Dame el nombre del profesor al que vas a asignar a alguna biblioteca: ")
        profesor = esc.buscar_profesor(nombre)
        if profesor:
            esc.listar_bibliotecas()
            biblioteca = input("A que biblioteca?: ")
            existe= esc.buscar_biblioteca(biblioteca)
            if existe:
                profesor.asignar_biblioteca(existe)
        else: 
            print("❌ No se encontró un profesor con ese nombre.")
    elif opcion == "5":
        nombre = input("Dame el nombre del profesor del que quieres que consulte libros de su biblioteca: ")
        existe= esc.buscar_profesor(nombre)
        if existe:
            existe.consultar_libros()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    
    elif opcion == "8":
        nombre_biblioteca = input("Dame el nombre de la biblioteca: ")
        biblio = Biblioteca(nombre_biblioteca)
        esc.agregar_biblioteca(biblio)
        
    elif opcion == "9":
        esc.profesores_en_bibliotecas()
        opcion = input("¿Quieres buscar una en especifico? Pon SI o NO: ").upper()
        if opcion == "SI":
            nom = input("Dame el nombre de la biblioteca para ver que profesores estan ahi: ")
            existe = esc.buscar_biblioteca(nom)
            if existe:
                esc.profesores_en_bibliotecas(True, existe.nombre)
            else: print("no existe esa")
        else: pass
        
    #codigo optimizado
    
    elif opcion == "9":
        esc.profesores_en_bibliotecas()
        opcion = input("¿Quieres buscar una en específico? (SI/NO): ").strip().upper()
        if opcion == "SI":
            nom = input("Nombre de la biblioteca: ")
            existe = esc.buscar_biblioteca(nom)
            if existe:
                esc.profesores_en_bibliotecas(True, existe.nombre)
            else:
                print("❌ No existe esa biblioteca.")

    else: print("Elige una opcion del menu")

