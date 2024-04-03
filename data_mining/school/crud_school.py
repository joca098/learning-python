from school_db import con, cur, sqlite3
import os

status_menu = True
global status_op

#Create tables
def create_country(op):
    os.system('clear')
    name = input("Ingrese el nombre del País: ")
    abrev = input("Ingrese la abreviatura del País: ")
    descrip = input("Ingrese la descripción del País: ")
    cur.execute("INSERT INTO country (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (name, abrev, descrip,))
    con.commit()
    print("Registro de País creado con éxito")
    os.system('pause')
    menu()

def list_all_country():
    os.system('clear')
    cur.execute("SELECT id, name FROM country")
    countries = cur.fetchall()
    print("Lista de Países ingresado:")
    for country in countries:
        print(f"ID: {country[0]}, Nombre: {country[1]}")

    

def create_department(op):
    os.system('clear')

    name = input("Ingrese el nombre del departamento: ")
    abrev = input("Ingrese la abreviatura del departamento: ")
    descrip = input("Ingrese la descripción del departamento: ")
    list_all_country()
    id_country = input("Ingrese el ID del país al que pertenece el departamento: ")
    cur.execute("INSERT INTO department (name, abrev, descrip, id_country, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_country))
    con.commit()
    print("Registro de departamento creado con éxito.")

    os.system('pause')
    menu()

def list_all_department():
    os.system('clear')
    cur.execute("SELECT id, name FROM department")
    departments = cur.fetchall()
    print("Lista de Departamentos ingresados:")
    for department in departments:
        print(f"ID: {department[0]}, Nombre: {department[1]}")

def create_city(op):
    os.system('clear')

    name = input("Ingrese el nombre de la ciudad: ")
    abrev = input("Ingrese la abreviatura de la ciudad: ")
    descrip = input("Ingrese la descripción de la ciudad: ")
    list_all_department()
    id_dept = input("Ingrese el ID del departamento al que pertenece la ciudad: ")
    cur.execute("INSERT INTO city (name, abrev, descrip, id_dept, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_dept))
    con.commit()
    print("Registro de ciudad creado con éxito.")

    os.system('pause')
    menu()

def list_all_city():
    os.system('clear')
    cur.execute("SELECT id, name FROM city")
    cities = cur.fetchall()
    print("Lista de ciudades:")
    for city in cities:
        print(f"ID: {city[0]}, Nombre: {city[1]}")

def create_identification_type(op):
    os.system('clear')

    name = input("Ingrese el nombre del tipo de identificación: ")
    abrev = input("Ingrese la abreviatura del tipo de identificación: ")
    descrip = input("Ingrese la descripción del tipo de identificación: ")
    cur.execute("INSERT INTO identification_type (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (name, abrev, descrip))
    con.commit()
    print("Registro de tipo de identificación creado con éxito.")
    os.system('pause')
    menu()

def list_all_identification_type():
    os.system('clear')
    cur.execute("SELECT id, name FROM identification_type")
    identification_types = cur.fetchall()
    print("Lista de tipos de documento:")
    for ident_type in identification_types:
        print(f"ID: {ident_type[0]}, Nombre: {ident_type[1]}")

def create_person(op):
    os.system('clear')
    first_name = input("Ingrese el primer nombre de la persona: ")
    last_name = input("Ingrese el apellido de la persona: ")
    list_all_identification_type()
    id_ident_type = input("Ingrese el ID del tipo de identificación de la persona: ")
    ident_number = input("Ingrese el número de identificación de la persona: ")
    list_all_city()
    id_exp_city = input("Ingrese el ID de la ciudad de expedición de la identificación: ")
    address = input("Ingrese la dirección de la persona: ")
    mobile = input("Ingrese el número de teléfono móvil de la persona: ")
    list_all_users()
    id_user = input("Ingrese el ID del usuario asociado a la persona: ")
    cur.execute("INSERT INTO person (first_name, last_name, id_ident_type, ident_number, id_exp_City, address, mobile, id_user, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_user))
    con.commit()
    print("Registro de persona creado con éxito.")

    os.system('pause')
    menu()

def list_all_person():
    os.system('clear')
    cur.execute("SELECT id, first_name, last_name FROM person")
    persons = cur.fetchall()
    print("Lista de personas:")
    for person in persons:
        print(f"ID: {person[0]}, Nombre: {person[1]}")

def create_student(op):
    os.system('clear')
    code = input("Ingrese el código del estudiante: ")
    list_all_person()
    id_persons = input("Ingrese el ID del estudiante: ")
    cur.execute("INSERT INTO student (code, id_person, status, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (code, id_persons, 0))  # Estado predeterminado
    con.commit()
    print("Registro de estudiante creado con éxito.")
    os.system('pause')
    menu()
    

def create_user(op):
    os.system('clear')

    email = input("Ingrese el correo electrónico del usuario: ")
    password = input("Ingrese la contraseña del usuario: ")
    cur.execute("INSERT INTO user (email, password, status, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (email, password, 0))  # Estado predeterminado
    con.commit()
    print("Registro de usuario creado con éxito.")
    os.system('pause')
    menu()

def list_all_users():
    os.system('clear')
    cur.execute("SELECT id, email FROM user")
    users = cur.fetchall()
    print("Lista de usuarios:")
    for user in users:
        print(f"ID: {user[0]}, Email: {user[1]}")
    
def list_menu():
    while True:
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: LIST MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. List all countries")
        print("[2]. List all departments")
        print("[3]. List all cities")
        print("[4]. List all users")
        print("[5]. List all persons")
        print("[6]. List all students")
        print("[7]. Back to main menu")

        opt = input("Press an option: ")

        if opt == '1':
            list_all_country()
        elif opt == '2':
            list_all_department()
        elif opt == '3':
            list_all_city()
        elif opt == '4':
            list_all_users()
        elif opt == '5':
            list_all_person()
        elif opt == '6':
            list_all_students()
        elif opt == '7':
            return  # Regresar al menú principal
        else:
            print("Invalid option. Please try again.")

        
def menu():
    global opt
    status_opt = True
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create Country")
        print("[2]. Create department")
        print("[3]. Create city")
        print("[4]. Create identification type")
        print("[5]. Create user")
        print("[6]. Create a person")
        print("[7]. Create student")
        print("[8]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_country(opt)
        elif opt == '2':
            create_department(opt)
        elif opt == '3':
            create_city(opt)
        elif opt == '4':
            create_identification_type(opt)
        elif opt == '5':
            create_user(opt)
        elif opt == '6':
            create_person(opt)
        elif opt == '7':
            create_student(opt)    
        else: 
            print("::: See 'u soon :::")
            exit()

menu()
con.close()
