class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nb_tours=4, num_tour_actuel=1, joueurs=[], description=""):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tours = nb_tours
        self.num_tour_actuel = num_tour_actuel
        self.joueurs = joueurs
        self.description = description

# ajouter_tournoi
# ajouter un joueur a un tournoi
     