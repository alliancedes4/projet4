class Tournoi:
    """Classe représentant un tournoi."""

    AUTHORISED_STATUS = ["Created", "Live", "Finished"]
    NB_PLAYERS = 4
    NB_ROUNDS = 3

    def __init__(
        self,
        nom,
        lieu,
        date_debut,
        date_fin,
        nb_tours=4,
        num_tour_actuel=0,
        description="",
        list_id_joueurs=[],
        list_id_rounds=[],
        status="Created",
    ):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tours = nb_tours
        self.num_tour_actuel = num_tour_actuel
        self.list_id_joueurs = list_id_joueurs
        self.list_id_rounds = []
        self.description = description
        self.status = status  # Statut initial : Prêt

    @property
    def n_players(self):
        return len(self.list_id_joueurs)

    def ajouter_joueur(self, id_joueur):
        """Ajoute un joueur au tournoi."""

        if self.status != "Created":
            return "Impossible d'ajouter un joueur. Le tournoi est déjà en cours ou terminé."

        if self.n_players == self.NB_PLAYERS:
            return "Impossible d'ajouter un joueur. Le tournoi est complet."

        if id_joueur in self.list_id_joueurs:
            return (
                "Impossible d'ajouter un joueur. Le joueur est déjà inscrit au tournoi."
            )

        self.list_id_joueurs.append(id_joueur)

    def changer_status(self, new_status):
        """Change le statut du tournoi."""

        if new_status not in self.AUTHORISED_STATUS:
            return "Statut invalide."

        if new_status == self.status:
            return "Le tournoi est déjà dans ce statut."

        if new_status == "Created":
            return "Impossible de revenir au statut 'Created'."

        if new_status == "Live" and (self.n_players != self.NB_PLAYERS):
            return "Impossible de démarrer le tournoi. Le nombre de joueurs est insuffisant."

        if (new_status == "Live") and (self.status != "Created"):
            return "Impossible de démarrer le tournoi. Le tournoi est déjà en cours ou terminé."

        if (new_status == "Finished") and (self.status != "Live"):
            return "Impossible de terminer le tournoi. Le tournoi n'est pas en cours."

        if (new_status == "Finished") and (self.num_tour_actuel != self.NB_ROUNDS):
            return (
                "Impossible de terminer le tournoi. Tous les tours n'ont pas été joués."
            )

        # Mise à jour du statut
        self.status = new_status

        if new_status == "Live":
            self.next_round()

    def next_round(self):
        """Passe à la ronde suivante.s"""

        if self.num_tour_actuel == 0:
            # il faut calculer toutes les rondes et tous les matchs avec des scoress à -1
            self.compute_rounds()
            self.num_tour_actuel += 1
            return -1

        if self.num_tour_actuel == self.NB_ROUNDS:
            # le tournoi est terminé ! on ne passe pas à la ronde suivante
            return -1

        self.num_tour_actuel += 1

    def compute_rounds(self):
        # on crée les rondes et les matchs

        return -1

    def get_current_round(self):
        # on retourne la ronde actuelle
        # aller chercher dans la liste des rondes
        return -1

    def update_round(self, match_list):
        # on met à jour la ronde avec toute les informations des matchs
        return -1
