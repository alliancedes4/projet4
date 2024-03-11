"""
Module pour la classe Joueur
"""


class Joueur:
    """Classe représentant un joueur d'échecs."""

    def __init__(self, nom, prenom, identifiant, date_naissance="01/01/1900"):
        """Init method."""

        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.identifiant = identifiant

    def save(self) :
        """Sauvegarde le joueur dans la base de données."""
        
        ########################
        # Write some code here
        ########################
        
        pass

    def load(self) :
        """Charge le joueur depuis la base de données."""
        
        ########################
        # Write some code here
        ########################
        
        pass

    def __repr__(self) -> str:

        return f"Joueur({self.__dict__})"
