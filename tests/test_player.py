"""
Teste la classe Joueur.
"""

import secrets
from chess.models.joueur import Joueur


# def hello():
#     """Cette fonction ne sera pas lancé par pytest car elle ne commence pas par test_"""

#     print("Hello World !")


def test_init_joueur():
    """Teste l'initialisation d'un joueur."""

    # initialisation d'un joueur
    joueur = Joueur("Doe", "John", "01/01/1900", "1234")

    # initialisation d'un joueur
    random_id = "test_" + secrets.token_hex(6)
    joueur = Joueur(random_id, random_id, "01/01/1900", random_id)  # save


def test_save_Joueur():
    """Test creation and save Joueur"""

    # initialisation d'un joueur
    random_id = "test_" + secrets.token_hex(6)
    joueur = Joueur(random_id, random_id, "01/01/1900", random_id)  # save
    joueur.save()


def test_load_Joueur():
    """Test to know hot to load a Joueur

    ==> LOAD ALL JOUERS in A LIST"""

    # initialisation d'un joueur
    random_id = "test_" + secrets.token_hex(6)
    joueur = Joueur(random_id, random_id, "01/01/1900", random_id)  # save
    joueur.save()

    # output = Joueur().load()
    output = Joueur.load()

    # # ==> Voudrais => la liste de tous les joueurs
    # assert isinstance(output, list)
    # p1 = output[-1]

    # # le 1er item de la liste soit un object de class Joueur (*instance*)
    # assert isinstance(p1, Joueur)


def test_search_by_id():
    """test if possible to select a specific Joueur directly with is id

    LOAD JUST THE GOOD PLAYER WITH GOOD ID
    """

    # initialisation d'un joueur + Save
    random_id = "test_" + secrets.token_hex(6)
    joueur = Joueur(random_id, random_id, "01/01/1900", random_id)  # save
    joueur.save()

    found_player = Joueur.search_by_id(random_id)
    # Alternative  :  new_p = Joueur().search_by_id(random_id)

    found_player = Joueur.search_by_id(random_id)

    # fond player is an instance from Jouer class
    assert isinstance(found_player, Joueur)

    # we fo have correct id
    assert found_player.identifiant == random_id
