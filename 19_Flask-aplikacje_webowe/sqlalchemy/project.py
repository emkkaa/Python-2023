# Przy pierwszym uruchomieniu:  flask --app project shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app project run
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.tagname


def get_tags(session):
    return session.query(Tag).all()


def create_tag(tagname, session):
    try:
        tag = Tag(tagname=tagname)
        session.add(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True

def remove_tag(tagname, session):
    try:
        tag = session.query(Tag).filter_by(tagname=tagname).one()
        session.delete(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True



@app.route('/')
def hello():
    return render_template('form77.html', data=get_tags(db.session),
                           tytul="Tags", no_error=True)


@app.route('/add')
def add():
    args = request.args
    no_error = create_tag(args["tag"], db.session)
    if no_error:
        tytul = "Dodano tag"
    else:
        tytul = "Taki tag już istnieje"

    return render_template('form77.html', data=get_tags(db.session),
                           no_error=no_error,
                           tytul=tytul)




@app.route('/remove')
def remove():
    args = request.args
    remove_tag(args["tag"], db.session)

    return render_template('form77.html', data=get_tags(db.session),
                           tytul="Usunieto tag")
