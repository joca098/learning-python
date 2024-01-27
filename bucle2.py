import os
os.system('clear')
#Funcion para simular los intentos de ingreso de clase en cajero automatico
#Intentos permitidos: 3
def cajero():
    #Clave registrada en el banco
    my_clave_banco = '2024'

    cont_attempts = 1 #Contador de intentos
    status = True

    #Clave que digito en el ATM
    while status:
        clave = input("Digita tu clave: ")
        if my_clave_banco == clave:
            print("Has ingresado a tu cuenta")
            print(f"Intentos satisfactorio: {cont_attempts}")
            status = False #Brake
        else : 
            if cont_attempts > 3:
                print(f"intento {cont_attempts}: Clave incorrecta, intenta nuevamente.")
                cont_attempts +=1
            else:
                print(f"intento {cont_attempts}: Clave incorrecta")
            cont_attempts +=1

        if cont_attempts > 3:
            print("Se han agotado los intentos permitidos. \n Tu cuenta ha sido bloqueada")
            break
cajero()