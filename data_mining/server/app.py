from flask import Flask, render_template
from database import con, cur
import sqlite3
from flask import g 

app = Flask(__name__) 

DATABASE = 'market.db' 

def get_db():
    db = getattr(g, '_database', None) 
    if db is None:
        db= g._database = sqlite3.connect()
    return db 
