# on importe de flask les fonctions qui permettent d'associer les fonctions aux pages html de sortie, de faire des
# requêtes POST ou GET, d'afficher des messages et de faire des redirections
from flask import render_template, request, flash, redirect
# on importe de flask_login (gestion des utilisateurs) les fonctions qui permettent de vérifier si l'utilisateur est
# connecté ou non et ainsi sécuriser et limiter l'accès à certaines pages
from flask_login import login_required, current_user

# on importe l'application pour faire des liens dans l'application en elle-même avec Click et db pour la base de données
from ..app import app, db
# on importe des modèles de données les classes que l'on va utiliser dans les formulaires
from ..modeles.donnees import Books, Printers, Institutions, Authorship


@app.route("/book/<int:book_id>/mod_form", methods=["GET", "POST"])
@login_required
def form_modifs(book_id):
    """
    Cette fonction permet de gérer un formulaire de modification des données de la classe Books.
    Les informations de chaque livre enregistré peuvent ainsi être modifiées.

    :param book_id: identifiant unique du livre à modifier
    :return: True, mon_livre
    """

    # on crée une variable pour récupérer les informations du livre qui correspond à son identifiant, sinon erreur 404
    mon_livre = Books.query.get_or_404(book_id)
    # on récupère toutes les informations des deux classes Printers et Institutions
    imprimeurs = Printers.query.all()
    institutions = Institutions.query.all()

    # on ouvre une liste vide d'erreurs
    erreurs = []
    # update est pour l'instant fausse car le livre n'est pas modifié
    updated = False

    # si la méthode requêtée est bien POST
    if request.method == "POST":
        # mais que les infos ne sont pas renseignées pour chaque champ ou qu'elles ne sont pas valides, on envoie un
        # message d'erreur dans la liste d'erreurs
        if not request.form.get("bookTitle", "").strip():
            erreurs.append("Le titre n'est pas renseigné")
        if not request.form.get("bookDate", "").strip():
            erreurs.append("La date n'est pas valide")
        if not request.form.get("bookFormat", "").strip():
            erreurs.append("Le format n'est pas renseigné")
        if not request.form.get("bookLanguage", "").strip():
            erreurs.append("La langue n'est pas renseignée")
        if not request.form.get("bookIdentifier", "").strip():
            erreurs.append("L'identifiant n'est pas renseigné")

        if not request.form.get("bookPrinter", ""):
            erreurs.append("L'imprimeur n'est pas valide")
        elif not Printers.query.get(request.form["bookPrinter"]):
            erreurs.append("L'imprimeur n'est pas valide")

        if not request.form.get("bookPlace", ""):
            erreurs.append("Le lieu de conservation n'est pas valide")
        elif not Institutions.query.get(request.form["bookPlace"]):
            erreurs.append("Le lieu de conservation n'est pas valide")

        # s'il n'y a pas d'erreurs dans la liste d'erreurs, on ajoute pour mon_livre les informations des champs du
        # formulaire aux colonnes qui lui correspondent pour ce même enregistrement
        if not erreurs:
            print("Faire ma modification")
            mon_livre.title = request.form["bookTitle"]
            mon_livre.publidate = request.form["bookDate"]
            mon_livre.format = request.form["bookFormat"]
            mon_livre.language = request.form["bookLanguage"]
            mon_livre.identifier = request.form["bookIdentifier"]
            mon_livre.id_printer = request.form["bookPlace"]
            mon_livre.id_institution = request.form["bookPrinter"]

            # on ajoute le livre à la base et la modification à Authorship pour l'utilisateur qui l'a faite
            db.session.add(mon_livre)
            db.session.add(Authorship(book=mon_livre, user=current_user))
            db.session.commit()
            # updated devient true si le livre est modifié, ce qui va permettre d'afficher l'historique des
            # modifications dans la page
            updated = True

    return render_template("pages/form_modifs.html", nom="Base Manuce", livre=mon_livre,
                           imprimeurs=imprimeurs, institutions=institutions,
                           erreurs=erreurs, updated=updated)


@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    """
    Cette fonction permet d'ajouter un livre à la base de données. Les informations peuvent ensuite être modifiées avec
    le formulaire de modification pour être plus complètes.

    :return: le livre est ajouté
    """
    livre = Books.query.all()

    if request.method == "POST":
        statut, livre = Books.add_book(
            title=request.form.get("title", None),
            publidate=request.form.get("publidate", None),
            format=request.form.get("format", None),
            language=request.form.get("language", None),
            identifier=request.form.get("identifier", None)
        )
        if statut is True:
            flash("Votre livre a bien été enregistré", "success")
            return redirect("/index")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(livre), "error")

    return render_template("/pages/add_book.html", nom="Base Manuce", livre=livre)


@app.route("/book/<int:book_id>/delete_book", methods=["GET", "POST"])
@login_required
def delete_book(book_id):
    """
    Cette fonction permet de supprimer des livres (un livre par un livre, en utilisant son identifiant pour ce faire).

    :param book_id: identifiant unique du livre
    :return: deleted_book
    """
    deleted_book = Books.query.get_or_404(book_id)
    if current_user.is_authenticated is True:
        if request.method == "POST":
            db.session.delete(deleted_book)
            db.session.add(Authorship(book=deleted_book, user=current_user))
            db.session.commit()
            return redirect("/index")

    return render_template("pages/delete_book.html", nom="Base Manuce", book=deleted_book)
