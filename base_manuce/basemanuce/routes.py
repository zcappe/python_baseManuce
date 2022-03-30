from flask import render_template


from .app import app
from .modeles.donnees import Books


# On définit le chemin (la route) qui permet d'accéder à la page d'accueil de l'application
@app.route("/")
def accueil():
    livres = Books.query.all()
    return render_template("/pages/accueil.html", nom="Base Manuce", livres=livres)


@app.route("/index")
def index():
    livres = Books.query.all()
    return render_template("/pages/index.html", nom="Base Manuce", livres=livres)


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
