from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Leandro Guarnier"

if __name__ == '__main__':
    app.run()