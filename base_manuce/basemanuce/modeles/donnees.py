from ..app import db
import datetime
from .utilisateurs import User
from flask_login import current_user

# Avec les class ...(db.Model), on crée ce qui correspond aux tables dans la base de données,
# pour ensuite y insérer des objets (enregistrements)
# On a ici les trois tables contenant les imprimeurs, les institutions de conservations et les livres


class Authorship(db.Model):
    __tablename__ = "authorship"
    authorship_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    authorship_book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    authorship_printer_id = db.Column(db.Integer, db.ForeignKey('printers.printer_id'))
    authorship_institution_id = db.Column(db.Integer, db.ForeignKey('institutions.institution_id'))
    authorship_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    authorship_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship("User", back_populates="authorships", foreign_keys=authorship_user_id)

    book = db.relationship("Books", back_populates="authorships", foreign_keys=authorship_book_id)
    printer = db.relationship("Printers", back_populates="authorships", foreign_keys=authorship_printer_id)
    institution = db.relationship("Institutions", back_populates="authorships", foreign_keys=authorship_institution_id)


class Books(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    publidate = db.Column(db.Text)
    format = db.Column(db.Text)
    language = db.Column(db.Text)
    identifier = db.Column(db.Text, nullable=False)
    id_printer = db.Column(db.Integer, db.ForeignKey('printers.printer_id'))
    id_institution = db.Column(db.Integer, db.ForeignKey('institutions.institution_id'))

    printer = db.relationship("Printers", back_populates="book", foreign_keys=id_printer)
    institution = db.relationship("Institutions", back_populates="book", foreign_keys=id_institution)
    authorships = db.relationship("Authorship", back_populates="book", foreign_keys=Authorship.authorship_book_id)

    @staticmethod
    def add_book(title, publidate, format, language, identifier):
        erreurs = []

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

        add = Books.query.filter(db.and_(Books.title == title,
                                         Books.publidate == publidate,
                                         Books.format == format,
                                         Books.language == language,
                                         Books.identifier == identifier)).count()

        if add > 0:
            erreurs.append("Le livre existe déjà")

        if len(erreurs) > 0:
            return False, erreurs

        new_book = Books(title=title,
                         publidate=publidate,
                         format=format,
                         language=language,
                         identifier=identifier)

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
    __tablename__ = 'printers'
    printer_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    printer_name = db.Column(db.Text, nullable=False)
    birthyear = db.Column(db.Integer)
    deathyear = db.Column(db.Integer)
    printer_othername1 = db.Column(db.Text)
    printer_othername2 = db.Column(db.Text)
    description = db.Column(db.Text)

    book = db.relationship("Books", back_populates="printer", foreign_keys=Books.id_printer)
    authorships = db.relationship("Authorship", back_populates="printer", foreign_keys=Authorship.authorship_printer_id)


class Institutions(db.Model):
    __tablename__ = 'institutions'
    institution_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    country = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    institution_name = db.Column(db.Text, nullable=False)

    book = db.relationship("Books", back_populates="institution", foreign_keys=Books.id_institution)
    authorships = db.relationship("Authorship", back_populates="institution",
                                  foreign_keys=Authorship.authorship_institution_id)
