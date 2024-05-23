import pytest

from chess.models.ronde import Ronde

import secrets


class TestRonde:

    def test_init(self):
        """Test l'initialisation d'une ronde."""

        token = secrets.token_hex(4)
        name = f"TestTournois-{token}-0"
        r = Ronde(f"TestTournois-{token}-0", [])

    def test_save(self):
        """test la sauvegarde d'une ronde."""

        token = secrets.token_hex(4)
        name = f"TestTournois-{token}-0"
        r = Ronde(f"TestTournois-{token}-0", [])
        r.save()

    def test_save_n_values_db(self):

        # calculer le nombre de rondes dans  la base

        # créer une ronde

        # save

        # recalculer le nombre de rondes dans la base

        # evaluer la différence +1

        pass

    def test_update(self):
        """Test la mise à jour d'une ronde."""

        # on fait une entrée dans la db
        token = secrets.token_hex(4)
        name = f"TestTournois-{token}-0"
        r = Ronde(f"TestTournois-{token}-0", [])
        r.save()

        del r

        # on vient charger à plat la ronde correspondante
        r = Ronde.find_by_id(name)
        match_list = r.match_list

        # on met à jour la ronde
        r.update(match_list=[((1, 1), (2, 1))])

        # on vient rechardt à plat la ronde correspondante
        r2 = Ronde.find_by_id(name)
        match_list2 = r2.match_list

        # on compare les deux match_list
        assert match_list != match_list2
