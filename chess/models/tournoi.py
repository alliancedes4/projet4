class Tournoi:
    """Classe représentant un tournoi."""

    def __init__(self, nom, lieu, date_debut, date_fin, nb_tours=4, num_tour_actuel=1, joueurs=[], description=""):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tours = nb_tours
        self.num_tour_actuel = num_tour_actuel
        self.joueurs = joueurs
        self.description = description

    def ajouter_joueur(self, joueur):
        """Ajoute un joueur au tournoi."""
        self.joueurs.append(joueur)

    def organiser_tournoi(self):
        """Organise le tournoi en rondes et matchs."""
        # Logique d'organisation du tournoi
        pass
    def organiser_ronde(self, nom_ronde):
        """Organise une ronde dans le tournoi."""
        ronde = Ronde(nom_ronde)
        ronde.organiser_matchs(self.joueurs)
# ajouter_tournoi
# ajouter un joueur a un tournoi
     