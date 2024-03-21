'''
Dev: Jorge Camilo Gelpud Rosero
Script description: configure SQLite data base 
'''
#Import engine databse package 
import sqlite3 

#Create a database connnection (Database name)
con = sqlite3.connect('market.db')

#Creating cursor object by conection => Let us execute sql commands or operations (Query)
cur = con.cursor()

#Create users table
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        ident_number TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
'''

#Execute SQL (Query)
cur.execute(user_table)

#Save changes in database => Push to database
con.commit()

#print("::: Database market has been created :::")