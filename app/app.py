from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Pagina de prueba</h1><p>Hello, World!</p><p>esto es otra linea</p>"

