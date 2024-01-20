#Tipos de datos en Python 
#Python es un lenguaje dinamicamente tipado

#1. Numericos
##Enteros Z = Int
num1 = 42
print("Num1:",type(num1))
##Flotantes o decimales (reales) = Float
num2 = 50.5
print("Num2:",type(num2))
#Complejos = complex
num3 = 2j
print("Num3:",type(num3))
#2. Cadena
my_name = "Camilo"
print("my_name", type(my_name))
my_lastname = 'Gelpud'
print("my_lastname", type(my_lastname))
profile = '''
jorge es una persona que 
estudia licenciatura en informatica'''
print("profile", type(profile))


a = 1
b = 1
suma1 = a + b #Suma aritmetica 

c = "1"
d = '1'
suma2 = c + d #Suma de cadenas   (concatenar)
#suma3 = a + c 
print("Suma1:", suma1)
print("Suma2:", suma2)
#print("Suma3:", suma3)

#3. Logicos (valores o expresiones booleanas)
usuario_activo = True
print("usuario_activo", type(usuario_activo))
pago_realizado = False 
print("pago_realizado", type(pago_realizado))

#4. Listas
frutas = ['Apple', 'Banana']
print(frutas)
print("frutas", type(frutas))
colors = ['Blue', 'Red', ' White', 'Green', 'Brown']
print(colors)
print("colors", type(colors))
detodito = ["Camilo", 20, 5000, "Chambu", 1.65]
print("detodito:", type(detodito[4]))
#5. Tuplas
#6. Diccionarios
#7. Conjuntos