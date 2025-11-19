from datetime import datetime, timedelta
import pandas as pd

class Ventas:
    def __init__(self, productos):
        self.productos = productos
        self.fecha = datetime.now()
    
            
    def mostrar_resumen(self, terminar= False):
        if terminar == True:
            total = sum(p.calcular_total() for p in self.productos)
            print(f"🧾 Venta del {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Total de productos: {len(self.productos)}")
            for p in self.productos:
                print(p)
            print(f"Con un total de: {total}")
            self.productos.clear()
            print(self.productos)
        else: print("Añadido a la venta")

    def leer_csv(self,ruta):
        df = pd.read_csv(ruta)
        
    def guardar_csv(self,ruta):
        df = pd.read_csv(ruta)
        if df.empty:
            print(df.columns)
            data = [ [1], 
                [p.nombre for p in self.productos],
                [p.cantidad for p in self.productos],
                [p.precio for p in self.productos],
                [self.fecha.strftime('%d/%m/%Y %H:%M:%S')]]
            print(self.productos)
          
            print(data)

