# models/joueur.py

from tinydb import TinyDB

from tinydb import Query


class Joueur:
    """Classe représentant un joueur."""

    def __init__(self, nom: str, prenom: str, date_naissance: str, identifiant: str):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.identifiant = identifiant

    def save(self):
        """Sauvegarde le joueur dans la base de données."""
        db = TinyDB("data_joueurs.json")
        db.insert(self.__dict__)
        db.close()

    def update(self, **kwargs):
        """Met à jour les informations du joueur."""
        for key, value in kwargs.items():
            setattr(self, key, value)

        db = TinyDB("data_joueurs.json")
        q = Query()
        db.update(self.__dict__, q.identifiant == self.identifiant)
        db.close()

        # manque qqch ici : le save des valuers dns la db

    @classmethod
    def load(cls):
        """Charge tous les joueurs depuis la base de données."""
        db = TinyDB("data_joueurs.json")
        list_player = db.all()
        db.close()
        return list_player

    @classmethod
    def search_by_id(cls, identifiant):
        """Recherche un joueur par identifiant."""
        all_players = cls.load()
        for player_data in all_players:
            if player_data["identifiant"] == identifiant:
                return cls(
                    nom=player_data["nom"],
                    prenom=player_data["prenom"],
                    date_naissance=player_data["date_naissance"],
                    identifiant=player_data["identifiant"],
                )
        return None

    @classmethod
    def delete_all(cls):
        """Supprime tous les joueurs de la base de données."""
        db = TinyDB("data_joueurs.json")
        db.truncate()
        db.close()

    @classmethod
    def boot(cls):
        """Crée 4 joueurs fictifs dans la base de données."""
        db = TinyDB("data_joueurs.json")
        for i in range(1, 5):
            joueur = cls(
                nom=f"Nom{i}",
                prenom=f"Prénom{i}",
                date_naissance="2000-01-01",
                identifiant=f"identifiant{i}",
            )
            joueur.save()
        db.close()

    def __repr__(self) -> str:
        return f"Joueur({self.__dict__})"
