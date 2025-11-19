#Objetivo: practicar clases, atributos, métodos y constructores.
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def calcular_total(self):
        return self.precio * self.cantidad

    #__str__ Permite impirmir objetos de forma legible
    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Cantidad: {self.cantidad}"
# Lista para guardar los productos
productos = []

while True:
    try:
        cant_productos= input("¿Cuantos productos quieres ingresar(Min: 1, Max:3)? ")
        if cant_productos.isdigit():
            cant_productos=int(cant_productos)
            if 1 <= cant_productos <= 3:
                break
            else:print("Debe estar entre 1 a 3 productos")
        else: print("Ingresa numero, no letras")
    except ValueError:
        print("No caracteres raros")

# Pedir datos e instanciar productos
for i in range(1, cant_productos + 1):
    print(f"\nProducto {i}:")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")

    producto = Producto(nombre, precio, cantidad)
    productos.append(producto)
    

#Mostrar productos
print("\n--- Lista de productos ---")
total_compra = 0
for p in productos:
    print(p)
    total_compra += p.calcular_total()

print(f"\nTotal general de la compra: ${total_compra:.2f}")

#Buscando por indice el nombre del producto
#print(productos[0].Nombre)
# Buscador de producto por nombre y no por indice
buscar = input("\nEscribe el nombre del producto que quieres buscar: ")

encontrado = False  # bandera para saber si lo encontramos o no

encontrados=[]
for p in productos:
    if p.nombre.lower().startswith(buscar):  # compara sin importar mayúsculas/minúsculas
        encontrados.append(p)

if encontrados: #saber si la lsta tiene elementos igual a decir if len(encontrados) == 0
    print(f"\n✅ Se encontraron {len(encontrados)} productos que coinciden:\n")
    for prod in encontrados:
        print(prod)  # aquí se usa __str__ automáticamente
        print(f"Total: ${prod.calcular_total():.2f}\n")
else:
    print("\n❌ No se encontraron productos con ese nombre.")