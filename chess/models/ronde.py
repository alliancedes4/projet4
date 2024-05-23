from tinydb import TinyDB

from tinydb import Query


class Ronde:
    """



    # pour chaque ronde , on crée la ronde et save la ronde dans la base de donnée :
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

    """

    DB_NAME = "data/data_rondes.json"

    def __init__(self, id_ronde, match_list):
        """Initialise une ronde."""

        self.id_ronde = str(id_ronde)
        self.match_list = match_list

    def save(self):
        """Sauvegarde la ronde dans la base de données."""

        db = TinyDB(self.DB_NAME)
        db.insert(self.__dict__)
        db.close()

    def update(self, **kwargs):
        """Met à jour les informations du joueur."""

        for key, value in kwargs.items():
            setattr(self, key, value)

        db = TinyDB(self.DB_NAME)
        q = Query()
        db.update(self.__dict__, q.id_ronde == self.id_ronde)
        db.close()

    def update_match_list(self, match_list):
        """Met à jour les informations de la ronde."""

        self.match_list = match_list
        self.update()

    def to_dict(self):
        return {
            # "nom": self.nom,
            "id_ronde": self.id_ronde,
            "match_list": self.match_list,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("id_ronde"),
            data["match_list"],
        )

    @classmethod
    def load(cls):
        """Charge toutes les rondes depuis la base de données."""

        db = TinyDB(cls.DB_NAME)
        list_rondes = db.all()
        db.close()
        return [cls.from_dict(r) for r in list_rondes]

    @classmethod
    def find_by_id(cls, id_ronde):
        """Recherche une ronde par identifiant."""

        db = TinyDB(cls.DB_NAME)
        q = Query()
        data = db.get(q.id_ronde == id_ronde)
        db.close()

        if isinstance(data, list):
            data = data[0]

        if data:
            return cls.from_dict(data)

        return None
