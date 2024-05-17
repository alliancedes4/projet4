from controlers.gestion_inscriptions import GestionInscriptions
from models.joueur import Joueur

# Création de joueurs fictifs
joueur1 = Joueur("Alice", "Dupont", "01/01/1990", "AD1234")
joueur2 = Joueur("Bob", "Martin", "02/02/1992", "BM5678")

# Création du gestionnaire d'inscriptions
gestionnaire = GestionInscriptions()

# Création d'un tournoi fictif
gestionnaire.creer_tournoi("Tournoi d'échecs", "Paris", "2024-04-15")

# Inscription des joueurs fictifs au tournoi
gestionnaire.inscrire_joueur(joueur1)
gestionnaire.inscrire_joueur(joueur2)
