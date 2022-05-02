# warn permet d'envoyer un message d'avertissement
from warnings import warn

# cette variable permet de limiter le nombre de résultats affichés par page lorsque la pagination est utilisée
LIVRES_PAR_PAGE = 2

# on définit le secret par défaut de l'application
SECRET_KEY = "aquelleheureonmange"

# si le code secret correspond à 'je suis un secret', un message d'avertissement est envoyé
if SECRET_KEY == "JE SUIS UN SECRET":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire")