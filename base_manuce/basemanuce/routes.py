from flask import render_template, request


from .app import app
from .modeles.donnees import Books, Printers


LIVRES_PAR_PAGE = 2


# On définit le chemin (la route) qui permet d'accéder à la page d'accueil de l'application
@app.route("/")
def accueil():
    imprimeurs = Printers.query.order_by(Printers.birthyear.asc()).all()
    return render_template("/pages/accueil.html", nom="Base Manuce",
                           imprimeurs=imprimeurs)


@app.route("/index")
def index():
    livres = Books.query.order_by(Books.title.asc()).all()

    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    index_livres = Books.query.order_by(Books.title.asc()).paginate(page=page, per_page=LIVRES_PAR_PAGE)

    return render_template("/pages/index.html", nom="Base Manuce", livres=livres, index_livres=index_livres)


# On définit le chemin (la route) qui permet d'afficher chaque livre un par un selon son identifiant (sa clé primaire)
@app.route("/book/<int:book_id>")
def livre(book_id):
    unique_livre = Books.query.get(book_id)
    return render_template("pages/livre.html", nom="Base Manuce", livre=unique_livre)


@app.route("/imprimeur/<int:printer_id>")
def imprimeur(printer_id):
    unique_imprimeur = Printers.query.get(printer_id)
    return render_template("pages/imprimeur.html", nom="Base Manuce", imprimeur=unique_imprimeur)


@app.route("/recherche_simple")
def recherche_simple():
    motclef = request.args.get("keyword", None)
    resultats = []
    titre = "Recherche simple"
    if motclef:
        resultats = Books.query.filter(Books.title.like("%{}%".format(motclef))).all()
        titre = "Résultats pour la recherche `" + motclef + "`"
    return render_template("pages/resultats.html", nom="Base Manuce",
                           resultats=resultats,
                           titre=titre)


@app.route("/recherche_avancee")
def recherche_avancee():
    return render_template("pages/rechercheavancee.html", nom="Base Manuce")


@app.route("/inscription")
def inscription():
    return render_template("pages/inscription.html", nom="Base Manuce")


@app.route("/connexion")
def connexion():
    return render_template("pages/connexion.html", nom="Base Manuce")


@app.route("/formulaire")
def formulaire():
    return render_template("pages/formulaire.html", nom="Base Manuce")
