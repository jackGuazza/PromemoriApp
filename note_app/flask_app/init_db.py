import sqlite3

connection = sqlite3.connect('database.db') 

with open('crea_posts.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close()
print("Database creato con successo !")
