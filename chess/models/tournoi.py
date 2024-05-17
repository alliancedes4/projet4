from tinydb import TinyDB

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
        self.list_id_rounds = list_id_rounds
        self.description = description
        self.status = status  # Statut initial : Prêt

    def save(self):
        """Sauvegarde le tournois dans la base de données."""

        db = TinyDB("data_tournois.json")
        db.insert(self.__dict__)
        db.close()

    def update(self, **kwargs):
        """Met à jour les informations du tournois."""

        for key, value in kwargs.items():
            setattr(self, key, value)

        # manque qqch ici

    @classmethod
    def load(cls):
        """Charge tous les joueurs depuis la base de données."""

        db = TinyDB("data_tournois.json")
        list_tournois = db.all()
        db.close()
        return list_tournois

    @classmethod
    def search_by_id(cls, identifiant):
        """Recherche un joueur par identifiant."""

        all_tournois = cls.load()
        for tournois in all_tournois:
            if tournois["identifiant"] == identifiant:
                return Tournoi(**tournois)
            
        return None

    @classmethod
    def delete_all(cls):
        """Supprime tous les joueurs de la base de données."""

        db = TinyDB("data_joueurs.json")
        db.truncate()
        db.close()

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

    def create_rounds(self):
        """Crée les rondes et les matchs du tournoi."""

        # ici on crée les rondes et les matchs / supposons qu'on a 4 jours A, B , C et D
            # ronde 1 : # [A, B], [C, D] 2 matchs 
            # ronde 2 :   # [A, C], [B, D] 2 matchs 
            # ronde 3 # [A, D], [B, C] 2 matchs 
            # fin du tournoi ! 

        # MAIS il  faut stocker les results dans les matchs de chaque ronde

        # donc on aura : 
            # ronde  1 : 
            # [A, B], # match 1  # [C, D] # match 2

        # avec en réel : 
            # [(A, -1), (B, -1)], # match 1 
            # [(C, -1), (D, -1)] # match 2
            # pour stocker pour chaque match le id _player et le score
            # à la place de A, B .... on aura les id des joueurs
            # on met -1 comme valeur par default pur bien comprendre que celan n'a pas été joué
            # au fur et à mesure des matchs/ rondes on mettra a jour avec les bons socres
        
        # pour chaque ronde , on créé et save la ronde dans la base de donnée : 
            # les rondes on 2 attibuts
            #     * id_ronde et 
            #     * macht_list 

            # les rondes ont plusieurs methodes comme : 
            #     * __init__
            #     * from_dict
            #     * to_dict
            #     * save
            #     * update
            #     * load (load all )
            #     * find_by_id 

        return -1

    def get_current_round(self):
        # on retourne la ronde actuelle
        # aller chercher dans la liste des rondes

        return -1

    def update_round(self, match_list):
        # on met à jour la ronde avec toute les informations des matchs

        

        return -1
    
    def compute_scores(self):
        # on calcule les scores de chaque joueur

        # placeholder

        return -1
    
    def compute_classement(self):
        # on calcule le classement des joueurs

        # placeholder

        return -1
