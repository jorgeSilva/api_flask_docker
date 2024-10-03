import flask
from flask import request, json, jsonify
import requests
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'db'  # Nome do serviço definido no docker-compose
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootpassword'  # Corrigido de MYSQL_ROOT_PASSWORD
app.config['MYSQL_DB'] = 'flaskdocker'  # Certifique-se de que o nome do banco de dados está correto

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

@app.route("/insertHost", methods=["POST"])
def insertHost():
    response = requests.get('https://randomuser.me/api')
    data = response.json()

    username = data['results'][0]['name']['first']

    cur = mysql.connection.cursor()
    cur.execute(""" INSERT INTO users(name) VALUES(%s) """, (username,))
    mysql.connection.commit()
    cur.close()

    return f"Olá {username}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)  # Portas como números não precisam de aspas
