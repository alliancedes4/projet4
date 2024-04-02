"""
Class Player
"""

from tinydb import TinyDB, Query


class Joueur:
    """ """

    def __init__(
        self,
        nom: str,
        prenom: str,
        date_naissance: str,
        identifiant: str,
    ):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.identifiant = identifiant

    def save(self):
        """Sauvegarde le joueur dans la base de données."""

        db = TinyDB("player.json")
        db.insert(self.__dict__)
        db.close()

    @classmethod
    def load(self):
        """Charge tous les jouers depuis la base de données."""

        db = TinyDB("player.json")
        # Joueur = Query()
        # joueur_cherche = db.get(Joueur.identifiant == self.identifiant)
        # db.close()
        # if joueur_cherche:
        #     self.nom = joueur_cherche["nom"]
        #     self.prenom = joueur_cherche["prenom"]
        #     self.date_naissance = joueur_cherche["date_naissance"]
        #     self.identifiant = joueur_cherche["identifiant"]
        #     return True
        # else:
        #     return False

        list_player = db.all()
        return list_player

    @classmethod
    def search_by_id(self, identifiant):
        """ """

        # >>> from tinydb import TinyDB, Query
        # >>> db = TinyDB('path/to/db.json')
        # >>> User = Query()
        # >>> db.insert({'name': 'John', 'age': 22})
        # >>> db.search(User.name == 'John')
        # [{'name': 'John', 'age': 22}]

        #########################################"
        #   INSERT CODE HERE
        #   forcement on va utiliser les resultats de la methode précédente
        #########################################""

        # RETURN AN INSTANCE OF JOUEUR

    def __repr__(self) -> str:

        return f"Joueur({self.__dict__})"
