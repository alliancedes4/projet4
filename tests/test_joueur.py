"""
Teste la classe Joueur.
"""

from chess.models.joueur import Joueur


def hello():
    """Cette fonction ne sera pas lancé par pytest car elle ne commence pas par test_"""

    print("Hello World !")


def test_init_joueur():
    """Teste l'initialisation d'un joueur."""

    # initialisation d'un joueur
    joueur = Joueur("Doe", "John", "1234")

    # tester les valeurs des attributs
    assert joueur.nom == "Doe"
    assert joueur.prenom == "John"
    assert joueur.identifiant == "1234"
    assert joueur.date_naissance == "01/01/1900"

    print(joueur)
