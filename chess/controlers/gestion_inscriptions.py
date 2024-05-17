from ..models.tournoi import Tournoi

class GestionInscriptions:
    def __init__(self):
        self.tournoi_en_cours = None

    def creer_tournoi(self, nom, lieu, date):
        self.tournoi_en_cours = Tournoi(nom, lieu, date)
        print(f"Tournoi '{nom}' créé avec succès.")

    def inscrire_joueur(self, joueur):
        if self.tournoi_en_cours:
            self.tournoi_en_cours.inscrire_joueur(joueur)
        else:
            print("Aucun tournoi n'a été créé.")
