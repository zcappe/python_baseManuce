# on importe tout ce que contient le fichier app.py contenu dans le dossier basemanuce, qui contient principalement
# la définition de l'application et la configuration de la base de données, et qui rassemble tous les chemins de
# fichiers de l'application
from basemanuce.app import app

# Bout de code cool et bizarre qui permet de lancer l'application. Le 'debug=True' permet d'expliciter les erreurs
# rencontrées lors de l'utilisation de l'application.
# On le sépare du reste pour éviter des interférences indésirables
if __name__ == "__main__":
    app.run(debug=True)
