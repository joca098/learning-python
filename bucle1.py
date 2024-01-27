'''
Bucle: Loop, Repetir una accion N veces, iteraciones (Cantidad de ejecuciones.)
Contadores (Cuenta o inncrementa)
Acumuladores (Acumilacion de valores. Sumar valores.)
Contar valores es diferente de sumar valores
'''
#Funcion Bucle para imprimir los numeros del 1 al 10 en pantalla
def list_numers(): 
    #Bucle que imprime lista de numeros de 1 al 10 por pantalla
    i = 1
    while i <= 100:
        print (i)
        i = i+1  # i = i + 1   

    print("i: ",i)

def list_numers2(): 
    #Bucle que imprime lista de numeros de 1 al 10 por pantalla
    i = 1
    status = True
    while status: #While status == True
        if i == 11:
            break
        print (i)
        i = i+1  # i = i + 1   
    print("i: ",i)

def list_numers3(): 
    #Bucle que imprime lista de numeros de 1 al 10 por pantalla
    i = 1
    status = True
    while status: #While status == True
        print (i)
        i = i+1  # i = i + 1   
        if i > 10: 
            status = False
    print("i: ",i)

def list_numers4(): 
    #Bucle que imprime lista de numeros de 1 al 10 por pantalla
    i = 1
    status = False
    while not status: #While status == True
        print (i)
        i = i+1  # i = i + 1   
        if i > 10: 
            status = True
    print("i: ",i)

#list_numers()
#list_numers2()
#list_numers3()
list_numers4()