# main.py
from inventario import Inventario
from productos import Producto,Consumibles,Equipo,Reactivo
from ventas import Ventas
from datetime import datetime

inv = Inventario()
inv.leer_csv("inventario.csv")
ruta = r"D:\documentos\cursoPOO\ejercicios\ejercicio3\inventario.csv"
ruta_dos = r"D:\documentos\cursoPOO\ejercicios\ejercicio3\ventas.csv"

dic = {"Consumibles":["Guantes","Alcohol","Tubo de ensayo","Papel filtro"],
    "Equipo": ["Microscopio","Osciloscopio","Balanza digital"],
    "Reactivo":["Acetona","Etanol","Acido"]
    }
while True:
    
    print("\n--- MENÚ ---")
    print("1. Agregar producto/s")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Guardar en CSV")
    print("5. Realizar venta")
    print("6. Guardar venta en CSV")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
           #eleccion = None
        categoria = input("Que tipo de producto quieres agregar?\n1. Consumibles\n2. Equipo\n3. Reactivo\n Pon el numero: ")
        if categoria == "1":
            print("Esta es la lista de productos que hay en la categoria de Consumibles")
            mostrar= dic.get("Consumibles")
            print("\n ".join(mostrar))
            producto = input("Que producto? ").capitalize()
            if producto in dic.get("Consumibles"):
                #cant= int(input("¿Cuantos productos quieres agregar? Pon el numero: "))
                
                #if cant == 1:
                    
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                unidad = input("¿En que unidad? ")
                inv.agregar_producto(Consumibles(1,producto, precio, cantidad,unidad))

        if categoria == "2":
            print("Esta es la lista de productos que hay en la categoria de Equipo")
            mostrar= dic.get("Equipo")
            print("\n ".join(mostrar))
            producto = input("Que producto? ").capitalize()
            if producto in dic.get("Equipo"):
                precio = float(input("Precio: "))
                cantidad = input("Cantidad: ")
                numero_serie = input("¿Cual es el numero de serie? ")
                estado = input("¿Cual es su estado? ")
                inv.agregar_producto(Equipo(1,producto, precio, cantidad,numero_serie,estado))
                
        if categoria == "3":
            print("Esta es la lista de productos que hay en la categoria de Reactivos")
            mostrar= dic.get("Reactivo")
            print("\n ".join(mostrar))
            producto = input("Que producto? ").capitalize()
            if producto in dic.get("Reactivo"):
                precio = input("Precio: ")
                cantidad = int(input("Cantidad: "))
                caducidad= input("Pon su fecha de caducidad: Formato dd/mm/aaaa\n")
                fecha = datetime.strptime(caducidad, "%d/%m/%Y")
                peligrosidad = input("Cual es su nivel de peligrosidad? (Bajo,Medio,Alto) ").capitalize()
                actual = datetime.now()
                reactivo = Reactivo(1,producto, precio, cantidad,fecha,peligrosidad)
                print(reactivo.esta_vencido(actual))
                inv.agregar_producto(reactivo)
                
        
        #total = inv.calcular_valor_total()
        
        #print(f"💰 Valor total actual del inventario: ${total:.2f}")
        
    elif opcion == "2":
        nombre = input("Nombre del producto a eliminar: ").capitalize()
        inv.eliminar_producto(nombre)
        
    elif opcion == "3":
        inv.mostrar_inventario(ruta)
    elif opcion == "4":
        
        inv.guardar_en_csv(ruta)
        
    elif opcion == "5":
        inv.mostrar_inventario(ruta)
        eleccion = input("Que producto quieres añadir a la venta? ").capitalize()
        producto_datos= inv.traer_inventario(ruta, eleccion)
        if not producto_datos:
            print("Ese producto no existe pai, Escoje uno de la lista")
        #Recuerda hacer desempaquetado, lo de abajo ocupa mas codigo
        #nombre = producto[0]
        #cantidad = producto[1]
        #precio = producto[2]
        #desempaquetado
        nombre,precio,cantidad= producto_datos
        cantidad_vender = int(input(f"Cuantas unidades del producto {nombre} quieres vender, hay {cantidad}? "))
        if cantidad_vender > cantidad:
            print("No hay suficiente cantidad en el inventario para vender")
        else:
            inv.agregar_producto(Producto(nombre,precio,cantidad_vender))
            ven = Ventas(inv.productos)
            ven.mostrar_resumen()
            while True:
                otro_producto = input("¿Quieres añadir otro producto a la venta? Pon SI o NO: ").upper()
                if otro_producto == "SI":
                    inv.mostrar_inventario(ruta)
                    eleccion = input("Que producto quieres añadir a la venta? ").capitalize()
                    producto_datos= inv.traer_inventario(ruta, eleccion)
                    if not producto_datos:
                        print("Ese producto no existe pai, Escoje uno de la lista")
                    nombre,precio,cantidad= producto_datos
                    cantidad_vender = int(input(f"Cuantas unidades del producto {nombre} quieres vender, hay {cantidad}? "))
                    if cantidad_vender > cantidad:
                        print("No hay suficiente cantidad en el inventario para vender")
                    else:
                        inv.agregar_producto(Producto(nombre,precio,cantidad_vender))
                        ven = Ventas(inv.productos)
                        ven.mostrar_resumen()
                else: 
                    ven.mostrar_resumen(True)
                    break
    elif opcion == "6":
            ven.guardar_csv(ruta_dos)
            
        
    elif opcion == "7":
        print("👋 Saliendo del programa...")
        break
    else:
        print("❌ Opción no válida, intenta de nuevo.")

