from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# On crée l'application Flask et on la nomme
app = Flask("Base Manuce")
# On définit l'URI de la base de données qui permet de la connecter
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../basemanuce.sqlite'
# On crée l'objet SQLalchemy de l'application, qu'on peut ensuite utiliser pour créer des modèles (tables):
db = SQLAlchemy(app)


# Avec les class ...(db.Model), on crée ce qui correspond aux tables dans la base de données,
# pour ensuite y insérer des objets (enregistrements)
# On a ici les trois tables contenant les imprimeurs, les institutions de conservations et les livres
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


# On définit le chemin (la route) qui permet d'accéder à la page d'accueil de l'application
@app.route("/")
def accueil():
    livres = Books.query.all()
    return render_template("/pages/accueil.html", nom="Base Manuce", livres=livres)


@app.route("/index")
def index():
    livres = Books.query.all()
    return render_template("/pages/index.html", nom="Base Manuce", index=livres)


# On définit le chemin (la route) qui permet d'afficher chaque livre un par un selon son identifiant (sa clé primaire)
@app.route("/book/<int:book_id>")
def livre(book_id):
    unique_livre = Books.query.get(book_id)
    return render_template("pages/livre.html", nom="Base Manuce", livre=unique_livre)


@app.route("/inscription")
def inscription():
    return render_template("pages/inscription.html", nom="Base Manuce")


@app.route("/connexion")
def connexion():
    return render_template("pages/connexion.html", nom="Base Manuce")


@app.route("/recherche")
def recherche():
    return render_template("pages/recherche.html", nom="Base Manuce")


@app.route("/formulaire")
def formulaire():
    return render_template("pages/formulaire.html", nom="Base Manuce")


# Bout de code cool et bizarre qui permet de lancer l'appli
if __name__ == "__main__":
    app.run(debug=True)
