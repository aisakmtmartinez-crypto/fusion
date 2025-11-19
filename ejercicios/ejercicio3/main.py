# main.py
from inventario import Inventario
from productos import Producto
from ventas import Ventas

inv = Inventario()
inv.leer_csv("inventario.csv")
ruta = r"D:\documentos\cursoPOO\ejercicios\ejercicio3\inventario.csv"
ruta_dos = r"D:\documentos\cursoPOO\ejercicios\ejercicio3\ventas.csv"

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
        cant= int(input("¿Cuantos productos quieres agregar? Pon el numero: "))
        
        
        if cant == 1:
            nombre = input("Nombre del producto: ").capitalize()
            precio = input("Precio: ")
            cantidad = input("Cantidad: ")
            inv.agregar_producto(Producto(nombre, precio, cantidad))
            
        if cant > 1:
            lista = []
            for i in range(1, cant + 1):
                print(f"Producto{i}")
                nombre = input("Nombre del producto: ")
                precio = input("Precio: ")
                cantidad = input("Cantidad: ")
                inv.agregar_producto(Producto(nombre, precio, cantidad))
                
        # ✅ Mostrar el total una sola vez, al final de todos los agregados
        total = inv.calcular_valor_total()
        print(f"\n✅ Se agregaron {cant} productos.")
        print(f"💰 Valor total actual del inventario: ${total:.2f}")
        
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
