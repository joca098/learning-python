'''
script description:
Cree una funcion que genere el lanzamiento de dos dados (1-6) 
y muestre por pantalla el mensaje GANADOR cuando genere un par de seis,
de lo contrario el mensaje dirá, SIGUE INTENTANDO.
'''

#Importar biblioteca para generar numeros aleatorios enteros.
from random import randint 

#Lanzar y generar los valores de los dos dados.
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

d = dices()
d1 = d[0]
d2 = d[1]
print("Dices:",d)
print("Dice 1:",d1)
print("Dice 2:",d2)

if d1 == d2:
    print("Felicidades eres el GANADOR")
else:
    print("Sigue intentando")

#print("dice1:",dice1)
#print("dice2:",dice2)