# flask --app hello2 run odpalamy z terminala bez rozszerzenia python odpalamy aplikacje

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test") #inna sciezka
def test():
    return "<p>Hello, World from test!</p>"


@app.route("/another") #inna sciezka
def another(): #mam funkcje to co zwroci to sie pojawi to w przegladrce pod ta sciezka
    return "<p>Hello, World from another!</p>"
