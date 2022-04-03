from flask import render_template, request, flash, redirect


from ..app import app, login
from ..modeles.donnees import Books, Printers
from ..modeles.utilisateurs import User
from ..constantes import LIVRES_PAR_PAGE
from flask_login import login_user, current_user, logout_user


@app.route("/")
def accueil():
    """ Cette route permet d'accéder à la page d'accueil du site"""
    imprimeurs = Printers.query.order_by(Printers.birthyear.asc()).all()

    return render_template("/pages/accueil.html", nom="Base Manuce",
                           imprimeurs=imprimeurs)


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
    """Cette route permet d'afficher, pour chaque livre, toutes les informations des livres de la base de données"""
    unique_livre = Books.query.get(book_id)

    return render_template("pages/livre.html", nom="Base Manuce", livre=unique_livre)


@app.route("/imprimeur/<int:printer_id>")
def imprimeur(printer_id):
    """Cette route permet d'afficher, pour chaque imprimeur, toutes les informations des imprimeurs de la
    base de données"""
    unique_imprimeur = Printers.query.get(printer_id)

    return render_template("pages/imprimeur.html", nom="Base Manuce", imprimeur=unique_imprimeur)


@app.route("/recherche_simple")
def recherche_simple():
    """Cette route permet d'afficher les résultats de la recherche par mot clé dans les titres des livres de la base.
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


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    """Cette route permet de s'inscrire avec le formulaire de la page"""
    if request.method == "POST":
        statut, donnees = User.creer(
            email=request.form.get("email", None),
            pseudo=request.form.get("pseudo", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Votre inscription a bien été prise en compte. Vous pouvez maintenant vous identifier.",
                  "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html", nom="Base Manuce")


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """Cette route permet de se connecter avec le formulaire de la page"""
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté", "info")
        return redirect("/")
    if request.method == "POST":
        utilisateur = User.identification(
            pseudo=request.form.get("pseudo", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Vous êtes maintenant connecté", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Vos identifiants sont erronés ou vous n'êtes pas encore inscrit.", "error")

    return render_template("pages/connexion.html", nom="Base Manuce")
login.login_view = 'connexion'


@app.route("/deconnexion")
def deconnexion():
    """Cette route permet de se déconnecter"""
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté", "info")
    return render_template("pages/deconnexion.html", nom="Base Manuce")


@app.route("/formulaire")
def formulaire():
    return render_template("pages/formulaire.html", nom="Base Manuce")
