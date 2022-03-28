from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask("Base Manuce")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basemanuce.db'
db = SQLAlchemy(app)


class Printers(db.Model):
    __tablename__ = 'printers'
    printer_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    printer_name = db.Column(db.Text, nullable=False)
    birthyear = db.Column(db.Integer)
    deathyear = db.Column(db.Integer)


class Institutions(db.Model):
    __tablename__ = 'institutions'
    institution_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    country = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    institution_name = db.Column(db.Text, nullable=False)


class Books(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    publidate = db.Column(db.Text)
    format = db.Column(db.Text)
    language = db.Column(db.Text)
    identifier = db.Column(db.Text, nullable=False)
    id_printer = db.Column(db.Integer, db.ForeignKey('printers.printer_id'))
    id_institution = db.Column(db.Integer, db.ForeignKey('institutions.institution_id'))


@app.route("/")
def accueil():
    livres = Books.query.all()
    return render_template("/pages/accueil.html", nom="Base Manuce", livres=livres)


@app.route("/book/<int:book_id>")
def livre(book_id):
    unique_livre = Books.query.get(book_id)
    return render_template("pages/livre.html", nom="Base Manuce", livre=unique_livre)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
