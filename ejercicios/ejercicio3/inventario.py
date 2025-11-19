import pandas as pd
import numpy as np
from productos import Producto 
from tabulate import tabulate

class Inventario:
    def __init__(self):
        
        #es una lista la variable de instancia, pero no lo agregamos al contsructor porque
        #inicializa vacia, que es lo que queremos
        self.productos = []
    

    #Metodos de instancia, sirven para trabajar con los atributos del objeto, en este caso
    #la lista self.productos
    def agregar_producto(self, producto):
        self.productos.append(producto)
        


    def eliminar_producto(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                self.productos.remove(p)
                print(f"✅ Producto '{nombre}' eliminado correctamente.")
                return
        print(f"❌ Producto '{nombre}' no encontrado.")

    
    #Este metodo podria ser estatico, ya que no trabajamos con algun metodo o 
    # attributo de la clase inventario
    #@staticmethod
    def mostrar_inventario(self,ruta):
        df = pd.read_csv(ruta)
        if df.empty:
            print("No hay que mostrar")
        else: print(df)
            
    def traer_inventario(self,ruta,eleccion):
        df = pd.read_csv(ruta)
        df= df.loc[df["nombre"] == eleccion,]
        print(df)
        df= df.iloc[0,].tolist()
        df = [v.item() if isinstance(v, (np.int64, np.float64)) else v for v in df]
        return df

    def calcular_valor_total(self):
        return sum(p.calcular_total() for p in self.productos)

    # ✅ Guardar con pandas
    def guardar_en_csv(self, ruta):
        if not self.productos:
            print("⚠️ No hay productos para guardar.")
            return
        
        data = {
            "nombre": [p.nombre for p in self.productos],
            "precio": [p.precio for p in self.productos],
            "cantidad": [p.cantidad for p in self.productos],
        }

        
        df = pd.read_csv(ruta)
        print(df)
        if df.empty:
            print("Esta vacio")
            df = pd.DataFrame(data)
            df.to_csv(ruta, index=False, encoding="utf-8")
            print(f"💾 Inventario guardado en '{ruta}'.")
        else:
            print("Hay registros")
            df_nuevo = pd.DataFrame(data)
            df= pd.concat([df,df_nuevo], ignore_index= True)
            print(df)
            df.to_csv(ruta, index=False, encoding="utf-8")
            print(f"💾 Inventario guardado en '{ruta}'.")
        self.productos.clear()
        print(f"Nueva lista: {self.productos}")

    
    def leer_csv(self, archivo):
        try:
            df = pd.read_csv(archivo, encoding="utf-8")
            self.productos = [
                Producto(row["nombre"], float(row["precio"]), int(row["cantidad"]))
                for _, row in df.iterrows()
            ]
            print(f"📂 Inventario cargado desde '{archivo}'.")
        except FileNotFoundError:
            print("⚠️ No se encontró el archivo. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"❌ Error al leer el archivo: {e}")
