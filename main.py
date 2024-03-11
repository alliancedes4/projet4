from views.menu import Menu
from gestion.gestion_joueurs import GestionJoueurs
from gestion.gestion_tournois import GestionTournois

menu = Menu()
gestion_joueurs = GestionJoueurs()
gestion_tournois = GestionTournois()

while True:
    menu.afficher_menu_principal()
    choix = input("Entrez votre choix : ")

    if choix == "1":
        gestion_joueurs.ajouter_joueur("John", "Doe", "01/01/2000", "AB12345")
        print("Joueur ajouté avec succès !")
    elif choix == "2":
        gestion_tournois.ajouter_tournoi(
            "Tournoi 1",
            "Paris",
            "01/01/2024",
            "01/02/2024",
            4,
            1,
            [],
            "Description du tournoi",
        )
        print("Tournoi ajouté avec succès !")
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
