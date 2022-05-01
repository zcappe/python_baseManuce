from flask import render_template, request, flash, redirect
from flask_login import login_required, current_user


from ..app import app, db
from ..modeles.donnees import Books, Printers, Institutions, Authorship


@app.route("/book/<int:book_id>/mod_form", methods=["GET", "POST"])
@login_required
def form_modifs(book_id):
    mon_livre = Books.query.get_or_404(book_id)
    imprimeurs = Printers.query.all()
    institutions = Institutions.query.all()

    erreurs = []
    updated = False

    if request.method == "POST":
        if not request.form.get("bookTitle", "").strip():
            erreurs.append("Le titre n'est pas renseigné")
        if not request.form.get("bookDate", "").strip():
            erreurs.append("La date n'est pas valide")
        if not request.form.get("bookFormat", "").strip():
            erreurs.append("Le format n'est pas renseigné")
        if not request.form.get("bookLanguage", "").strip():
            erreurs.append("La langue n'est pas renseignée")
        if not request.form.get("bookIdentifier").strip():
            erreurs.append("L'identifiant n'est pas renseigné")

        if not erreurs:
            print("Faire ma modification")
            mon_livre.book_title = request.form["bookTitle"]
            mon_livre.publidate = request.form["bookDate"]
            mon_livre.format = request.form["bookFormat"]
            mon_livre.language = request.form["bookLanguage"]
            mon_livre.identifier = request.form["bookIdentifier"]

            db.session.add(mon_livre)
            db.session.add(Authorship(book=mon_livre, user=current_user))
            db.session.commit()
            updated = True

    return render_template("pages/form_modifs.html", nom="Base Manuce", livre=mon_livre,
                           imprimeurs=imprimeurs, institutions=institutions,
                           erreurs=erreurs, updated=updated)


@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    if current_user.is_authenticated is True:
        if request.method == "POST":
            statut, data = Books.new_infos(
                title=request.form.get("title", None),
                publidate=request.form.get("publidate", None),
                format=request.form.get("format", None),
                language=request.form.get("language", None),
                identifier=request.form.get("identifier", None),
                imprimeur=request.form.get("imprimeur", None),
                conserv=request.form.get("conserv", None)
            )
            if statut is True:
                db.session.add(Authorship(book=data, user=current_user))
                db.session.commit()
                flash("Votre livre a bien été enregistré", "success")
                return redirect("/index")
            else:
                flash("Il y a eu une erreur et les modifications n'ont pas été enregistrées", "danger")
    return render_template("/pages/add_book.html", nom="Base Manuce")


@app.route("/book/<int:book_id>/delete_book", methods=["GET", "POST"])
@login_required
def delete_book(book_id):
    deleted_book = Books.query.get_or_404(book_id)
    if current_user.is_authenticated is True:
        if request.method == "POST":
            db.session.delete(deleted_book)
            db.session.add(Authorship(book=deleted_book, user=current_user))
            db.session.commit()
            return redirect("/index")

    return render_template("pages/delete_book.html", nom="Base Manuce", book=deleted_book)
