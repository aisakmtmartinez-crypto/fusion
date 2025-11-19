#Esta es una forma de crear objetos de forma secuencial, no con POO
#usando demasiadas lineas de codigo y sin un orden claro, no es una 
#practica real

#celular1_marca = "samsung"
#celular2_marca = "apple" 
#celular3_marca = "huawei"
#celular1_modelo = "S23"
#celular2_modelo = "iPhone 15 pro"
#celular3_modelo = "P20 pro"
#celular1_camaraT = "48MP"
#celular2_camaraT = "48MP"
#celular3_camaraT = "12MP"
#celular1_camaraF = "24MP"
#celular2_camaraF = "24MP"
#celular3_camaraF = "8MP"
#print(celular1_modelo)

#Clase
class Celular():
    #Estos son atributos estaticos o de clase, no cambian
    marca = "Samsung"
    modelo ="S23"
    camara= "48MP"

#Instanciar un objeto, un objeto es una instancia de una clase
#"Creamos algo despues de pasarlo por la clase"

celular1= Celular()
celular2= Celular()
celular3= Celular()
celular4= Celular()

#Esta no es una forma correcta de cambiar los atributos, ya que se lo 
# cambiaramos a todos y no solo a celular3

#celular3.camara = "60MP"
#Los objetos se guardan en la RAM, en un espacio de memoria y estan dentro
#del modulo main
#print(celular3)

print(celular3.camara)

