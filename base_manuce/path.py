import os

# Le module os, avec son module os.path, permet de gérer et manipuler les chemins de fichiers et leurs relations entre
# eux. Il permet notamment de lier le dossier basemanuce et le dossier templates, afin qu'ils soient associés pour
# le bon fonctionnement de l'application.

# on définit une variable chemin actuel qui crée un chemin dans ce fichier
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
print(chemin_actuel)

# avec cette variable templates, on lie le dossier basemanuce et le dossier templates ensemble avec le fichier actuel
# et son chemin grâce au join et à l'appel de la variable chemin_actuel associé aux noms des deux dossiers
templates = os.path.join(chemin_actuel, "basemanuce", "templates")
print(templates)
