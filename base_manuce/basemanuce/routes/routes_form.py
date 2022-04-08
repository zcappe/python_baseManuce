from flask import render_template, request


from ..app import app
from ..modeles.donnees import Books, Printers
from ..constantes import LIVRES_PAR_PAGE


@app.route("/formulaire")
def formulaire():
    return render_template("pages/formulaire.html", nom="Base Manuce")
