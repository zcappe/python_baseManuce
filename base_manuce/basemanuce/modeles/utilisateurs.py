from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from ..app import db, login


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    user_mail = db.Column(db.Text, nullable=False)
    user_pseudo = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
<<<<<<< HEAD
    authorships = db.relationship("Authorship", back_populates="user")
=======
>>>>>>> a3fd71d5dfa4f9ffb838c252a7aabb8cc88aa78d

    @staticmethod
    def identification(pseudo, motdepasse):
        """
        Cette fonction permet l'identification d'un utilisateur. Si cela fonctionne, cela renvoie
        les données de l'utilisateur :
            :param pseudo: Pseudo de l'utilisateur
            :param motdepasse: Mot de passe de l'utilisateur
            :returns: Si cela fonctionne, renvoie les données de l'utilisateur. Sinon, cela renvoie None
            :rtype: User ou None
        """
        utilisateur = User.query.filter(User.user_pseudo == pseudo).first()

        if utilisateur and check_password_hash(utilisateur.user_password, motdepasse):
            return utilisateur
        return None

    @staticmethod
    def creer(email, pseudo, nom, motdepasse):
        """
        Cette fonction permet de créer le compte d'un utilisateur.
        S'il y a une erreur, la fonction renvoie False suivi d'une liste d'erreurs.
        S'il n'y a pas d'erreur, la fonction renvoie True suivi de la donnée enregistrée.

            :param email: Email de l'utilisateur
            :param pseudo: Pseudo de l'utilisateur
            :param nom: Nom de l'utilisateur
            :param motdepasse: Mot de passe de minimum 8 caractères
        """
        erreurs = []

        if not email:
            erreurs.append("Vous n'avez pas renseigné votre email.")
        if not pseudo:
            erreurs.append("Vous n'avez pas renseigné votre pseudo.")
        if not nom:
            erreurs.append("Vous n'avez pas renseigné votre nom.")
        if not motdepasse or len(motdepasse) < 8:
            erreurs.append("Vous n'avez pas renseigné votre mot de passe, ou celui-ci fait moins de 8 caractères.")

        # On vérifie que l'email ou le pseudo n'ont pas déjà été utilisés par un autre utilisateur
        uniques = User.query.filter(db.or_(User.user_mail == email, User.user_pseudo == pseudo)).count()
        if uniques > 0:
            erreurs.append("L'email ou le pseudo que vous avez choisis sont déjà utilisés.")

        # Si on a au moins une erreur, on renvoie False et la liste d'erreurs
        if len(erreurs) > 0:
            return False, erreurs

        # On crée ici un nouvel utilisateur
        utilisateur = User(
            user_mail=email,
            user_pseudo=pseudo,
            user_name=nom,
            user_password=generate_password_hash(motdepasse)
        )

        try:
<<<<<<< HEAD
            # On ajoute et on intègre le nouvel utilisateur dans la base de données, puis on renvoie ses informations
=======
            # On ajoute et on envoie le nouvel utilisateur à la base de données, puis on renvoie ses informations
>>>>>>> a3fd71d5dfa4f9ffb838c252a7aabb8cc88aa78d
            db.session.add(utilisateur)
            db.session.commit()
            return True, utilisateur
        # On prévient le cas d'une erreur au moment de l'ajout de l'utilisateur à la base
        except Exception as erreur:
            return False, [str(erreur)]

    def get_id(self):
        """
        Cette fonction retourne l'identifiant de l'utilisateur qui est créé

            :return: l'identifiant de l'utilisateur
            :rtype: int
        """
        return self.user_id


@login.user_loader
def find_user_with_id(identifier):
    return User.query.get(int(identifier))
