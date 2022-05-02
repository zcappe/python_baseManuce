from flask import render_template, request


from ..app import app
# on importe les classes Books et Printers
from ..modeles.donnees import Books, Printers
# on importe la variable de limite de nombre de livres par page pour la pagination de l'index
from ..constantes import LIVRES_PAR_PAGE


@app.route("/")
def accueil():
    """ Cette route permet d'accéder à la page d'accueil du site et affiche un index par ordre alphabétique des
    imprimeurs de la base."""

    imprimeurs = Printers.query.order_by(Printers.birthyear.asc()).all()

    return render_template("/pages/accueil.html", nom="Base Manuce", imprimeurs=imprimeurs)


@app.route("/index")
def index():
    """ Cette route donne un index de tous les livres enregistrés dans la base de données.
    On y ajoute un pagination, avec deux livres par page. Ils sont aussi triés par ordre alphabétique."""

    livres = Books.query.order_by(Books.title.asc()).all()

    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    index_livres = Books.query.order_by(Books.title.asc()).paginate(page=page, per_page=LIVRES_PAR_PAGE)

    return render_template("/pages/index.html", nom="Base Manuce", livres=livres, index_livres=index_livres)


@app.route("/book/<int:book_id>")
def livre(book_id):
    """Cette route permet d'afficher, pour chaque livre, selon son identifiant, toutes les informations des livres de
    la base de données"""

    unique_livre = Books.query.get(book_id)

    return render_template("pages/livre.html", nom="Base Manuce", livre=unique_livre)


@app.route("/imprimeur/<int:printer_id>")
def imprimeur(printer_id):
    """Cette route permet d'afficher, pour chaque imprimeur, selon son identifiant, toutes les informations des
    imprimeurs de la base de données"""

    unique_imprimeur = Printers.query.get(printer_id)

    return render_template("pages/imprimeur.html", nom="Base Manuce", imprimeur=unique_imprimeur)


@app.route("/recherche_simple")
def recherche_simple():
    """Cette route permet d'afficher les résultats de la recherche par mot clé ou par caractère dans les livres de
    la base.
    On ajoute un filtre pour faire la recherche sur les titres des livres"""

    motclef = request.args.get("keyword", None)
    resultats = []
    titre = "Recherche simple"

    if motclef:
        resultats = Books.query.filter(Books.title.like("%{}%".format(motclef))).all()
        titre = "Résultats pour la recherche `" + motclef + "`"

    return render_template("pages/resultats.html", nom="Base Manuce",
                           resultats=resultats,
                           titre=titre)


@app.route("/research_date")
def research_date():
    """
    Cette fonction permet d'afficher un formulaire pour rentrer une date afin de faire une recherche par date
    dans les livres de la base.
    """

    dates = Books.query.all()

    return render_template("pages/search_date.html", nom="Base Manuce", dates=dates)


@app.route("/search_date")
def search_date():
    """
    Cette fonction permet d'obtenir les résultats de la recherche par date en réutilisant le même template de résultats
    que la fonction recherche_simple, ce qui évite une multiplication des templates et des liens.
    """

    dateclef = request.args.get("dateclef", None)
    resultats = []
    titre = "Recherche par date"

    if dateclef:
        resultats = Books.query.filter(Books.publidate.like("%{}%".format(dateclef))).all()
        titre = "Résultats pour la recherche `" + dateclef + "`"

    return render_template("pages/resultats.html", nom="Base Manuce",
                           resultats=resultats,
                           titre=titre)
