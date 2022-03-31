from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# on lie les fichiers entre eux
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

# On crée l'application Flask et on la nomme, et on lui lie les dossiers
# templates et static pour qu'elle fonctionne avec eux
app = Flask("Base Manuce",
            template_folder=templates,
            static_folder=statics)
# On définit l'URI de la base de données qui permet de la connecter
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basemanuce.sqlite'
# On crée l'objet SQLalchemy de l'application, qu'on peut ensuite utiliser pour créer des modèles (tables):
db = SQLAlchemy(app)


from .routes import accueil, index, livre, inscription, connexion, recherchesimple, formulaire
