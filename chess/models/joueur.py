# models/joueur.py

from tinydb import TinyDB, Query
import secrets

class Joueur:
    """Classe représentant un joueur."""

    def __init__(self, nom: str, prenom: str, date_naissance: str, identifiant: str):
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
    def load(cls):
        """Charge tous les joueurs depuis la base de données."""
        db = TinyDB("player.json")
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
        db = TinyDB("player.json")
        db.truncate()
        db.close()

    @classmethod
    def boot(cls):
        """Crée 4 joueurs fictifs dans la base de données."""
        db = TinyDB("player.json")
        for _ in range(4):
            sha = secrets.token_hex(2)
            sha = "test_" + sha
            player = cls(
                nom=sha,
                prenom=sha,
                date_naissance="01/01/2000",
                identifiant=sha,
            )
            player.save()
        db.close()

    def __repr__(self) -> str:
        return f"Joueur({self.__dict__})"
