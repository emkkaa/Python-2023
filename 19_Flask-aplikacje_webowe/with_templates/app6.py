# flask --app app2 run
#
from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    return render_template('form.html', data=data, tytul="To jest tytul z parametru")


@app.route('/add')
def add():
    args = request.args
    print(args)
    data.append(args["name"])

    return render_template('form.html', data=data, tytul="Dodano pozycję do listy")


# Stworzyć aplikację która nas wita po podaniu z formularza swojego imienia

# flask --app app run
#
from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    return render_template('form.html', data=data, tytul="To jest tytul z parametru")


@app.route('/add')
def add():
    args = request.args
    print(args)
    data.append(args["name"])

    return render_template('form.html', data=data, tytul="Dodano pozycję do listy")