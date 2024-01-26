#get all data about comets.

import requests
import os

os.system('clear')
def get_comets():
    global count
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    print(":::COMETS INFORMATION:::")

    try:
        #Request to API
        response =requests.get(url)
        response.raise_for_status() #=> Valida si se presenta algún error en la petición


        data = response.json() #Convierte el response en formato json
        #Print all comets names
        count = 0
        print("::: SOLAR SYSTEM MENU :::")
        print("[1]. Planets")
        #print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroid")
        print("[5]. Comets")
        opt = int(input("Choose an option: "))
        if opt == 1:
            body_type = "Planet"
        elif opt == 2:
            body_type = "Moon"
        elif opt == 3:
            body_type = "Asteroid"
        elif opt == 4:
            body_type = "Comet"
        else:
            print("::: Invalid option :::")

        total = int(input("Cantidad de datos a mostrar: "))
        #planet = input("Escriba el planeta a buscar: ")

        for comet in data["bodies"]:
            if comet["bodyType"] == body_type:
            #if comet ["englishName"] == planet:
            #if comet['isPlanet'] == True:
                print("English name: ", comet["englishName"] )
                print("Lunas: ", comet["moons"] )
                print("Gravedad: ", comet["gravity"] )
                print("Is planet?: ", comet["isPlanet"] )
                print("Body type: ", comet["bodyType"] )
                print("\n")

                count = count +1

            if count == total:
                break #rompe un bucle 
        print(count)
    except requests.exceptions.RequestException as e:
        print(f"API error:  {e}")

#llamar función
get_comets()
