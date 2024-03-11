"""
Module pour la classe Joueur
"""

class Joueur:
    """Classe représentant un joueur d'échecs."""

    def __init__(self, nom, prenom, date_naissance, identifiant):
        """Init method."""

        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.identifiant = identifiant
