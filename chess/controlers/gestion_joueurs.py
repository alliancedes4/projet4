# controlers/gestion_joueurs.py

from ..models.joueur import Joueur

class GestionJoueurs:
    """Classe pour gérer les joueurs."""

    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, nom, prenom, date_naissance, identifiant):
        """Ajoute un joueur à la liste des joueurs."""
        joueur = Joueur(nom, prenom, date_naissance, identifiant)
        self.joueurs.append(joueur)

    @classmethod
    def boot_players(cls):
       """Crée 4 joueurs fictifs dans la base de données."""
       Joueur.boot()

    @classmethod
    def reboot_players(cls):
      """Supprime tous les joueurs de la base de données et crée 4 joueurs fictifs."""
      Joueur.reboot()
