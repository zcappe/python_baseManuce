from flask import render_template, request, flash, redirect


from ..app import app, login
from ..modeles.utilisateurs import User
from flask_login import login_user, current_user, logout_user


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
