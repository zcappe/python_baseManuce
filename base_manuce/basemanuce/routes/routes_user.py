from flask import render_template, request, flash, redirect


from ..app import app, login
from ..modeles.utilisateurs import User
from flask_login import login_user, current_user, logout_user


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    """
    Cette route permet de s'inscrire avec le formulaire de la page inscription.html.
    Si la requête est bien 'POST' (envoi et non récupération d'informations), elle permet de créer dans la base de
    données une adresse mail (email), un identifiant (pseudo), un nom (nom) et un mot de passe (motdepasse) pour le
    nouvel utilisateur. Ces informations sont renseignées via le formulaire, pour lequel chaque champ est associé par
    son nom aux noms des éléments de la première condition (entre guillemets: comme 'nom' ou 'mot de passe') grâce à
      request.form.get().
    Si la requête a bien fonctionné, le nouvel utilisateur est enregistré dans la base de données et peut maintenant
    se connecter. Grâce à la variable statut, le succès de l'opération peut être vérifié et un message apparaît si
    cela a fonctionné, et un autre apparaît dans le cas contraire, contenant les raisons de l'erreur grâce à la
    méthode .join(donnees) qui rapporte les erreurs associées aux données de la variable donnees. Ces erreurs ont
    été définies au préalable dans la static method de la classe (table) User.
      """
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
    """
    Cette route permet de se connecter avec le formulaire de la page connexion.html.
    Elle vérifie d'abord si l'utilisateur est déjà connecté: si c'est le cas, elle affiche le message 'Vous êtes
    déjà connecté'.
    Elle vérifie ensuite si la requête http utilisée avec le formulaire est bien 'POST', et si l'utilisateur renseigne
     un identifiant (=pseudo) et un mot de passe (=motdepasse) déjà enregistré dans la base de données, la connexion
     est effectuée. Dans le cas d'une erreur ou d'un utilisateur inconnu, c'est un message d'erreur qui est renvoyé.
    """

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
    """Cette route permet de se déconnecter, et affiche un message informatif indiquant que la déconnexion a bien été
    effectuée. Elle renvoie vers la page deconnexion.html """

    if current_user.is_authenticated is True:
        logout_user()

    flash("Vous êtes déconnecté", "info")

    return render_template("pages/deconnexion.html", nom="Base Manuce")
