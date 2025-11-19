class A():
    def hablar(self):
        print("Hola desde A")
class B(A):
    def hablar(self):
        print("Hola desde B")
        
class F(A):
    def hablar(self):
        print("Hola desde D")
        
class C(F):
    def hablar(self):
        print("Hola desde C")
class D(B,C):
    def hablar(self):
        print("Hola desde D")
    

d = D()
d.hablar()
# El metodo mro me sirve para ver exactamente la jerarquia de prioridad a que atributo/metodo
#le dara prioridad la instancia del objeto
print(D.mro())