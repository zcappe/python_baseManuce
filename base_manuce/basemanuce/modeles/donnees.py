# On importe, depuis 'app.py' la variable db qui contient base de données pour pouvoir y apporter des modifications
from ..app import db
# On importe date qui permet d'indiquer la date à laquelle quelque chose a été fait
import datetime
# On importe la table/classe User qui définit les utilisateurs depuis le fichier voisin 'utilisateurs.py'
from .utilisateurs import User
# On importe la fonction current user depuis flask login, afin de repérer les informations concernant l'utilisateur qui
# parcourt l'application
from flask_login import current_user

# Avec les class ...(db.Model), on crée ce qui correspond aux tables dans la base de données,
# pour ensuite y insérer des objets (enregistrements)
# On a ici les quatre tables contenant les auteurs de modifications et les modifications apportées sur l'application,
# les livres, les imprimeurs et les institutions de conservations


class Authorship(db.Model):
    """
    Cette classe est liée à la fois à la classe User du fichier voisin utilisateurs.py, grâce à une clé étrangère, ainsi
    que, de la même façon, à la classe Books.
    Elle contient la trace des modifications effectuées par les utilisateurs sur les livres.
     On y retrouve:
      -l'identifiant unique de la modification qui permet de la singulariser,
      - l'identifiant unique du livre qui a été modifié,
      - l'identifiant unique de l'utilisateur qui a effectué les modifications,
      - la date à laquelle les modifications ont été effectuées.
    """

    # on force la définition du nom de la table
    __tablename__ = "authorship"

    # On définit le nom de chaque colonne de la table en tant que variable de la classe, et on définit, pour chaque
    # colonne, le type de données qu'elle contient en faisant appel à la variable db pour modifier la bonne base de
    # données, et en utilisant sur celle-ci la méthode Column() qui les définit comme colonne, et les types de données
    # dans les parenthèses de cette methode en tant que méthodes (integer, text...) auxquelles ont peut appliquer des
    # paramètres (db.ForeignKey=('books.user_id')); ou en tant que paramètres, qui fonctionnent en
    # booléens (nullable=True)
    authorship_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    authorship_book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    authorship_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    authorship_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # On définit ici dans des variables les relations des clés étrangères avec les clés primaires qui leur correspondent
    # dans la table qui leur est liée: par exemple ici la variable book lie la clé étrangère de authorship_book_id à la
    # table Books via la variable de relation "authorships" qui est sont équivalente dans cette table.
    user = db.relationship("User", back_populates="authorships", foreign_keys=authorship_user_id)
    book = db.relationship("Books", back_populates="authorships", foreign_keys=authorship_book_id)


class Books(db.Model):
    """
    Cette classe définit les livres qui se trouvent ou qui seront ajoutés dans la base de données, et toutes les
    informations qui les concernent.

    On a donc ici:
        - book_id = identifiant unique du livre
        - title = intitulé du livre
        - publidate = date de publication du livre (par année)
        - format = le format du livre
        - language = la langue utilisée dans le livre
        - identifier = la cote ou un autre identifiant associé au livre
        - id_printer = clé étrangère qui associe le livre à son imprimeur
        - id_printer = clé étrangère qui associe le livre à son institution de conservation

    La classe est liée via trois relations aux tables Printers et Institutions par les relations printer et institution,
     qui lui sont associées par le biais de ses deux clés étrangères, et à la table Authorship par la relation
     authorships, car elle fournit cette table en informations mais n'en reçoit pas de
    celle-ci.
    """

    # On force la définition du nom de la table
    __tablename__ = 'books'

    # On définit ici les noms de ses colonnes par le biais de ses variables et les types de données de ses colonnes par
    # le biais de la méthode .Column()
    book_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    publidate = db.Column(db.Text)
    format = db.Column(db.Text)
    language = db.Column(db.Text)
    identifier = db.Column(db.Text, nullable=False)
    id_printer = db.Column(db.Integer, db.ForeignKey('printers.printer_id'))
    id_institution = db.Column(db.Integer, db.ForeignKey('institutions.institution_id'))

    # On définit ici ses trois relations aux trois autres classes
    printer = db.relationship("Printers", back_populates="book", foreign_keys=id_printer)
    institution = db.relationship("Institutions", back_populates="book", foreign_keys=id_institution)
    authorships = db.relationship("Authorship", back_populates="book", foreign_keys=Authorship.authorship_book_id)

    @staticmethod
    def add_book(title, publidate, format, language, identifier):
        """
        Cette static method qui est créée pour cette classe est ensuite utilisée pour créer de nouveaux livres dans la
        classe Books, c'est cette method qui permet le bon fonctionnement de la fonction (voir son utilisation dans la
        fonction aa_book dans routes_form.py).

        :param title: intitulé du livre
        :param publidate: date de publication du livre
        :param format: format du livre
        :param language: langue utilisée dans le livre
        :param identifier: cote ou autre identifiant du livre
        :return: new book or erreur
        """

        # On ouvre une liste vide dans une variable normmée erreurs qui va récupérer toutes les erreurs rencontrées
        erreurs = []

        # Si une ou plusieurs des informations des paramètres ne sont pas renseignées, une erreur est ajoutée dans la
        # liste de la variable erreurs avec le message indiqué dans la méthode append()
        if not title:
            erreurs.append("Le titre n'est pas renseigné")
        if not publidate:
            erreurs.append("La date n'est pas renseignée")
        if not format:
            erreurs.append("Le format n'est pas renseigné")
        if not language:
            erreurs.append("Le language n'est pas renseigné")
        if not identifier:
            erreurs.append("L'identifiant n'est pas renseigné")

        # On définit une variable add qui permet de vérifier si les informations renseignées sont correspondent à des
        # données déjà enregistrées dans les colonnes correspondant aux paramètres (title, publidate, format, language,
        # identifier).
        add = Books.query.filter(db.and_(Books.title == title,
                                         Books.publidate == publidate,
                                         Books.format == format,
                                         Books.language == language,
                                         Books.identifier == identifier)).count()

        # Si les informations sont les mêmes que celles d'un livre déjà enregistré dans la base de données, une erreur
        # est ajoutée à la liste d'erreurs
        if add > 0:
            erreurs.append("Le livre existe déjà")

        # S'il y a une erreur ou plus, on retourne False et la liste des erreurs enregistrées pour pouvoir mieux les
        # identifier et les corriger
        if len(erreurs) > 0:
            return False, erreurs

        # Si le livre n'existe pas déjà, on définit la variable new_book qui récupère les informations renseignées pour
        # chaque paramètre
        new_book = Books(title=title,
                         publidate=publidate,
                         format=format,
                         language=language,
                         identifier=identifier)

        # On effectue ici un test: on essaie d'ajouter le nouveau livre (new_book) à la base de données, en créant une
        # information aussi à ce sujet dans la classe Authorship pour l'utilisateur qui effectue l'ajout.
        # Si le test est True, le new_book est ajouté à Books et la modification à Authorship.
        # SI le test est False, c'est qu'il y a eu un problème qui est signalé et l'ajout est annulé.
        try:
            db.session.add(new_book)
            db.session.commit()

            if new_book:
                book = Books.query.order_by(Books.book_id.desc()).limit(1).first()
                user = User.query.get(current_user.user_id)
                creates = Authorship(user=user, book=book)
                db.session.add(creates)
                db.session.commit()

            return True, new_book

        except Exception as erreur:
            db.session.rollback()
            return False, [str(erreur)]


class Printers(db.Model):

    # On force la définition du nom de la table
    __tablename__ = 'printers'

    # On définit ici les noms de ses colonnes par le biais de ses variables et les types de données de ses colonnes par
    # le biais de la méthode .Column()
    printer_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    printer_name = db.Column(db.Text, nullable=False)
    birthyear = db.Column(db.Integer)
    deathyear = db.Column(db.Integer)
    printer_othername1 = db.Column(db.Text)
    printer_othername2 = db.Column(db.Text)
    description = db.Column(db.Text)

    # On définit ici sa relation avec la classe Books
    book = db.relationship("Books", back_populates="printer", foreign_keys=Books.id_printer)


class Institutions(db.Model):

    # On force la définition du nom de la table
    __tablename__ = 'institutions'

    # On définit ici les noms de ses colonnes par le biais de ses variables et les types de données de ses colonnes par
    # le biais de la méthode .Column()
    institution_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    country = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    institution_name = db.Column(db.Text, nullable=False)

    # On définit ici sa relation avec la classe Books
    book = db.relationship("Books", back_populates="institution", foreign_keys=Books.id_institution)
