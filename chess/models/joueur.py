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

        # Parcourt la liste des joueurs pour trouver celui avec l'identifiant spécifié
        for player_data in all_players:
            if player_data["identifiant"] == identifiant:
                # Si l'identifiant correspond, crée une instance de Joueur et retourne
                return cls(
                    nom=player_data["nom"],
                    prenom=player_data["prenom"],
                    date_naissance=player_data["date_naissance"],
                    identifiant=player_data["identifiant"],
                )

        # Si aucun joueur avec cet identifiant n'est trouvé, retourne None
        return None

    def __repr__(self) -> str:
        return f"Joueur({self.__dict__})"
