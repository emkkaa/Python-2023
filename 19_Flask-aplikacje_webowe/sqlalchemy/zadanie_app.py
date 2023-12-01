###zadanie

# dodac i usunac uzytkownika z bazy

tag = session.query(Tag).filter_by(tagname=tagname).one()

session.delete(tag)

session.commit()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)