'''Crear una calculadora que reciba dos valores 
por consola, y realice las operaciones aritmeticas basicas'''

import os 

os.system('clear')

#inputs
print("Ingrese el primer valor")
n1 = int (input())
n2 = int (input("Ingrese el segundo valor "))
suma = n1 + n2
print("suma:", suma)
print(type(n1))

