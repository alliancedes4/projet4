from models.tournoi import Tournoi


class GestionTournois:
    def __init__(self):
        self.tournois = []

    def ajouter_tournoi(
        self,
        nom,
        lieu,
        date_debut,
        date_fin,
        nb_tours,
        num_tour_actuel,
        joueurs,
        description,
    ):
        tournoi = Tournoi(
            nom,
            lieu,
            date_debut,
            date_fin,
            nb_tours,
            num_tour_actuel,
            joueurs,
            description,
        )
        self.tournois.append(tournoi)
