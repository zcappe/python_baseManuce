from flask import render_template, request
from flask_login import login_required


from ..app import app
from ..modeles.donnees import Books, Printers, Institutions


@app.route("/book/<int:book_id>/form", methods=["GET", "POST"])
@login_required
def formulaire(book_id):
    mon_livre = Books.query.get_or_404(book_id)
    imprimeurs = Printers.query.all()
    institutions = Institutions.query.all()

    erreurs = []
    updated = False

    if request.method == "POST":
        if not request.form.get("title")

    return render_template("pages/formulaire.html", nom="Base Manuce")
