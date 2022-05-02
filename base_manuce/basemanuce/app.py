# On importe flask, qui permet de gérer le développement d'application web, et sa classe Flask qui permet de gérer
# la configuration de l'application.
from flask import Flask
# On importe flask_sqlalchemy, qui est une extension de flask pour gérer les bases de données SQL dans son application,
# et sa classe SQLAlchemy qui permet de configurer la base de données
from flask_sqlalchemy import SQLAlchemy
# On importe flask_login qui est aussi une extension de flask qui permet de gérer les utilisateurs et les actions de
# connexion ou déconnexion par exemple, avec sa classe LoginManager qui permet d'associer cette gestion des utilisateurs
# avec l'application
from flask_login import LoginManager
# on importe os comme dans path.py pour gérer les liens des fichiers
import os
# on importe la clé secrète définie dans le fichier constantes.py utilisée ici pour la configuration de l'application
from .constantes import SECRET_KEY


# on définit le chemin du fichier actuel
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
# on associe les chemins du fichier actuel et celui du dossier templates avec la pages web en html et python
templates = os.path.join(chemin_actuel, "templates")
# et on y associe la dossier static qui contient les fichiers qui permettent une meilleure mise en page des pages
statics = os.path.join(chemin_actuel, "static")


# On crée l'application Flask et on la nomme, et on lui lie les dossiers
# templates et static pour qu'elle fonctionne avec eux
app = Flask("Base Manuce", template_folder=templates, static_folder=statics)

# On configure la clé secrète en l'associant à l'application
app.config['SECRET_KEY'] = SECRET_KEY

# On définit l'URI de la base de données qui permet de la connecter grâce à SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basemanuce.sqlite'
# On désactive le suivi des modifications de la base de données avec False sur SQLAlchemy track modifications pour
# éviter l'utilisation d'un surplus de ressources
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# On crée l'objet SQLAlchemy de l'application, qu'on peut ensuite utiliser pour créer des modèles (tables) avec la
# variable db qui sera appelée à chaque fois pour lier les modifications de la base de données à la base de
# l'application :
db = SQLAlchemy(app)

# On met en place la gestion des utilisateurs
login = LoginManager(app)

# On importe toutes les fonctions définies dans les fichiers cités ci-dessous, qui permettent le bon fonctionnement de
# l'application, et leur fonctionnement associé dans l'application.
from .routes import routes_user, routes_classic, routes_form
