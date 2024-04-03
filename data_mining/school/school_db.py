'''
Dev: Jorge Camilo Gelpud Rosero
Script description: configure SQLite data base School
'''
import sqlite3


# Especifica la ruta del archivo de la base de datos
'''ruta_base_de_datos = 'school.db'
if os.path.exists(ruta_base_de_datos):
    # Elimina el archivo de la base de datos
    os.remove(ruta_base_de_datos)
    print("La base de datos ha sido eliminada exitosamente.")
else:
    print("La base de datos no existe.")
 '''   
con = sqlite3.connect("school.db")

cur = con.cursor()

table_country = '''
    CREATE TABLE IF NOT EXISTS country (
        id INTEGER PRIMARY KEY NOT NULL ,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleled_at DATETIME DEFAULT NULL     
    );
'''

table_department = '''
    CREATE TABLE IF NOT EXISTS department (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        created_at  DATETIME  NOT NULL,
        updated_at  DATETIME  NOT NULL,
        deleled_at  DATETIME  NULL,
        id_country INTEGER NOT NULL,
        FOREIGN KEY  (id_country)   REFERENCES country (id)   
    );
'''

table_city ='''
    CREATE TABLE IF NOT EXISTS city (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        id_dept INTEGER NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleled_at DATETIME NULL,
        FOREIGN KEY (id_dept) REFERENCES department (id)
    );
'''

table_person = '''
    CREATE TABLE IF NOT EXISTS person (      
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        id_ident_type INTEGER NOT NULL,
        ident_number VARCHAR(15) NOT NULL,
        id_exp_city INTEGER NOT NULL,
        id_user INTEGER,
        address VARCHAR(50) NOT NULL,
        mobile VARCHAR(50) NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleled_at DATETIME NULL,
        FOREIGN KEY (id_exp_city) REFERENCES city (id),
        FOREIGN KEY (id_user) REFERENCES user (id) 
    );
'''


table_user = '''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(250) NOT NULL,
        status BOOLEAN NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleled_at DATETIME NULL
    );
'''

table_identification_type = '''
    CREATE TABLE IF NOT EXISTS identification_type (
    id INTEGER  PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    abrev VARCHAR(10) NOT NULL,
    descrip VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleled_at DATETIME NULL,
    FOREIGN KEY (id) REFERENCES person(id_ident_type) 
    );
'''


table_student = '''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        code VARCHAR(50) NOT NULL,
        id_person INTEGER ,
        status BOOLEAN NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleled_at DATETIME NULL,
        FOREIGN KEY (id_person) REFERENCES person(id)
    );
'''
cur.execute(table_country)
cur.execute(table_department)
cur.execute(table_city)
cur.execute(table_identification_type)
cur.execute(table_person)
cur.execute(table_student)
cur.execute(table_user)

con.commit()
print("::: Database market has been created :::")