from ..app import db


# Avec les class ...(db.Model), on crée ce qui correspond aux tables dans la base de données,
# pour ensuite y insérer des objets (enregistrements)
# On a ici les trois tables contenant les imprimeurs, les institutions de conservations et les livres
class Printers(db.Model):
    __tablename__ = 'printers'
    printer_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    printer_name = db.Column(db.Text, nullable=False)
    birthyear = db.Column(db.Integer)
    deathyear = db.Column(db.Integer)


class Institutions(db.Model):
    __tablename__ = 'institutions'
    institution_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    country = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    institution_name = db.Column(db.Text, nullable=False)


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
