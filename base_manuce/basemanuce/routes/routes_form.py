from flask import render_template, request
from flask_login import login_required, current_user


from ..app import app, db
from ..modeles.donnees import Books, Printers, Institutions, Authorship


@app.route("/book/<int:book_id>/mod_form", methods=["GET", "POST"])
@login_required
def form_update(book_id):
    mon_livre = Books.query.get_or_404(book_id)
    imprimeurs = Printers.query.all()
    institutions = Institutions.query.all()

    erreurs = []
    updated = False

    if request.method == "POST":
        if not request.form.get("bookTitle", "").strip():
            erreurs.append("bookTitle")
        if not request.form.get("bookDate", "").strip():
            erreurs.append("bookDate")
        if not request.form.get("bookFormat", "").strip():
            erreurs.append("bookFormat")
        if not request.form.get("bookLanguage", "").strip():
            erreurs.append("bookLanguage")
        if not request.form.get("bookIdentifier").strip():
            erreurs.append("bookIdentifier")

        if not request.form.get("bookPrinter", "").strip():
            erreurs.append("bookPrinter")
        elif not Printers.query.get(request.form["bookPrinter"]):
            erreurs.append("bookPrinter")

        if not request.form.get("bookPlace", "").strip():
            erreurs.append("bookPlace")
        elif not Institutions.query.get(request.form["bookPlace"]):
            erreurs.append("bookPlace")

        if not erreurs:
            print("Faire ma modification")
            mon_livre.book_id = request.form["bookTitle"]
            mon_livre.publidate = request.form["bookDate"]
            mon_livre.format = request.form["bookFormat"]
            mon_livre.language = request.form["bookLanguage"]
            mon_livre.identifier = request.form["bookIdentifier"]
            mon_livre.printer = Printers.query.get(request.form["bookPrinter"])
            mon_livre.institution = Institutions.query.get(request.form["bookPlace"])

            db.session.add(mon_livre)
            db.session.add(Authorship(book=mon_livre, user=current_user))
            db.session.commit()
            updated = True

    return render_template("pages/form_modifs.html", nom="Base Manuce", livre=mon_livre,
                           imprimeurs=imprimeurs, institutions=institutions,
                           erreurs=erreurs, updated=updated)
