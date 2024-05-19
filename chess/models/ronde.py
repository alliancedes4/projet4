from tinydb import TinyDB

class Ronde:
    def __init__(self, nom, match_list, id_ronde=None):
        self.nom = nom
        self.match_list = match_list
        self.id_ronde = id_ronde

    def save(self):
        """Sauvegarde la ronde dans la base de données."""
        db = TinyDB("data_rondes.json")
        if self.id_ronde is None:
            self.id_ronde = db.insert(self.to_dict())
        else:
            db.update(self.to_dict(), doc_ids=[self.id_ronde])
        db.close()

    @classmethod
    def from_dict(cls, data):
        return cls(data['nom'], data['match_list'], data.get('id_ronde'))

    def to_dict(self):
        return {
            "nom": self.nom,
            "match_list": self.match_list,
            "id_ronde": self.id_ronde
        }

    @classmethod
    def load(cls):
        """Charge toutes les rondes depuis la base de données."""
        db = TinyDB("data_rondes.json")
        list_rondes = db.all()
        db.close()
        return [cls.from_dict(r) for r in list_rondes]

    @classmethod
    def find_by_id(cls, id_ronde):
        """Recherche une ronde par identifiant."""
        db = TinyDB("data_rondes.json")
        data = db.get(doc_id=id_ronde)
        db.close()
        if data:
            return cls.from_dict(data)
        return None

    def update(self, match_list):
        """Met à jour les informations de la ronde."""
        self.match_list = match_list
        self.save()
