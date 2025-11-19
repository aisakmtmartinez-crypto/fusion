from datetime import datetime, timedelta


class Ventas:
    def __init__(self, productos):
        self.productos = productos
        self.fecha = datetime.now()
    
    def hacer_venta(self):
        for p in self.productos:
            print(f"Venta realiza con {p} el {self.fecha}")


from datetime import datetime, timedelta

class Venta:
    def __init__(self, productos):
        self.productos = productos  # lista de objetos Producto
        self.fecha = datetime.now()

    def tiempo_desde_venta(self):
        diferencia = datetime.now() - self.fecha
        return diferencia  # devuelve un timedelta

    def mostrar_resumen(self):
        total = sum(p.calcular_total() for p in self.productos)
        print(f"🧾 Venta del {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Total de productos: {len(self.productos)}")
        print(f"Valor total: ${total:.2f}")
        print(f"Tiempo desde la venta: {self.tiempo_desde_venta()}")

from productos import Producto
from venta import Venta
import time

p1 = Producto("Manzanas", 10, 3)
p2 = Producto("Leche", 20, 2)

venta = Venta([p1, p2])
venta.mostrar_resumen()

# Esperar unos segundos para ver el cambio de tiempo
time.sleep(3)
print("⏳ Tiempo después:", venta.tiempo_desde_venta())
