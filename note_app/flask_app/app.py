from flask import Flask, render_template, redirect, request
import sqlite3

#app = Flask(__name__)
#if __name__ == "app":
 #   app.run(host='192.168.1.39', port=5000)
 #   print("server avviato correttamente")

HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "database.db"
app = Flask(__name__)
# app.debug = True



def connect():
    connection = sqlite3.connect(DBFILE)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/", methods=["GET", "POST"])  #restituisce tutti i post
def index():
    conn = connect()
    if request.method == "POST":
        data = dict(request.form)
        posts = search(data["search"])
    else:
        posts = conn.execute('SELECT * FROM posts').fetchall() #lista di post
        conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:idx>/delete', methods=('POST',))  #elimina il post con quell id
def delete(idx): # il nome del parametro deve coincidere con il nome del parametro della richiesta
    conn = connect()
    conn.execute('DELETE FROM posts WHERE id=?', (idx,))
    conn.commit()    
    conn.close()
    return redirect('/')


@app.route('/create', methods=('GET','POST'))  #crea post
def create():
    conn=connect()
    if request.method=='POST':
        titolo = request.form['titolo']
        info = request.form['info']    
        conn.execute('INSERT INTO posts(titolo, info) VALUES(?, ?)', (titolo, info))
        conn.commit()    
        conn.close()
        return redirect('/')
    return render_template('create.html')


def search(titolo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `POSTS` WHERE `TITOLO` LIKE ?", ("%"+titolo+"%",))
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "app":
    app.run(HOST_NAME, HOST_PORT)
    print("Server avviato con successo ! ")