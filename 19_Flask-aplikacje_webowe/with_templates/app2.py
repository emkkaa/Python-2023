# flask --app app2 run
#
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('index_param.html', title="To jest tytul z parametru")



#Zadanie

from flask import Flask, render_template

app = Flask(__name__)



@app.route('/test')
def hello():
    return render_template('index_param.html', title="To jest tytul z parametru")
