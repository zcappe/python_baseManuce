from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy


app = Flask("Base Manuce")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_manuce/basemanuce.sqlite'
# db = SQLAlchemy(app)

books = {
    0: {
        "name": "Discorsi della penitenza",
        "publidate": 1589,
        "format": "in-8",
        "language": "italien",
        "identifier": "8R23"
    },
    1: {
        "name": "Ovidii Metamorphoseon",
        "publidate": 1502,
        "format": "in-12",
        "language": "latin",
        "identifier": "8R24"
    }
}


@app.route("/")
def accueil():
    return render_template("pages/accueil.html", nom="Base Manuce", books=books)


@app.route("/book/<int:livre_id>")
def book(livre_id):
    return render_template("pages/livre.html", nom="Base Manuce", book=books[livre_id])


if __name__ == "__main__":
    app.run(debug=True)
