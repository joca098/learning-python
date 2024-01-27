'''
    Bucle que genere una n cantidad de numeros enteros (+-) aleatorios (-100 . 100).
    El usuario debe digitar la cantidad de numeros a generar
    Al finalizar, debe presentar el siguiente reporte:
        -Total de numeros generados
        -Cuantos numeros son pares
        -Cuantos numeros son impares
        -Cuantos numeros son positivos
        -Cuantos numeros son negativos
        -Suma de numeros positivos
        -Suma de numeros negativos
'''

import os
import random
os.system('clear')

def numers_generator(cant): 
    i = 1
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    sum_pos = 0
    sum_neg= 0

    while i <= cant:
        num = random.randint(-10,10)
        print(num)
        #Validar y contar los pares e impares
        if num % 2 == 0:
            pares = pares + 1
        else:
            impares +=1
        
        #Validar y contar positivos y negativos
        if num > 0:
            positivos = positivos + 1
            sum_pos = sum_pos + num
        else:
            negativos +=1
            sum_neg += num

        i += 1
    
    print(f"Total numeros ingresados: {cant}") #i - 1 
    print(f"Total pares generados: {pares}")
    print(f"Total impares generados: {impares}")
    print(f"Total positivos generados: {positivos}")
    print(f"Total negativos generados: {negativos}")
    print(f"Suma de positivos generados: {sum_pos}")
    print(f"Suma de negativos generados: {sum_neg}")
#main     
cant_num = int (input("Qué cantidad de numeros deseas generar: "))
numers_generator(cant_num)