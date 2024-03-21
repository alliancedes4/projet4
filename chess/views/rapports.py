class Rapports:
    def afficher_liste_joueurs(self, joueurs):
        print("Liste de tous les joueurs par ordre alphabétique :")
        for joueur in sorted(joueurs, key=lambda x: x.nom):
            print(f"{joueur.nom} {joueur.prenom}")
