# Base Manuce - devoir de python 

La Base Manuce est application développée dans le cadre du cours de Python du master TNAH. Elle permet de regrouper les différents ouvrages imprimés par la famille Manuce au cours du XVIe siècle.


# Installation

Pour commencer, cloner ce dépôt.

Puis y installer un environnement virtuel pour Python, ce qui permettra d'installer les librairies nécessaires et utiliser l'application uniquement dans le cadre de cet environnement virtuel. 

Pour ce faire, aller dans le dossier base_manuce et lancer les commandes suivantes:

`sudo apt-get install python3-virtualenv`

`virtualenv -p python3 env`

`source env/bin/activate`

Une fois l'environnement virtuel activé, on peut lancer la commande suivante afin d'installer les librairies nécessaires au bon fonctionnement de l'application:

`pip install -r requirements.txt`

Enfin, pour lancer l'application:

`python run.py`
