from models.joueur import Joueur


class GestionJoueurs:
    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, nom, prenom, date_naissance, identifiant):
        joueur = Joueur(nom, prenom, date_naissance, identifiant)
        self.joueurs.append(joueur)
