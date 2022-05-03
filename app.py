from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Aloooooô mundo véio sem portera"

if __name__ == '__main__':
    app.run()