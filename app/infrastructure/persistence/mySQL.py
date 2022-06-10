
from app.infrastructure.persistence.interfaces import PersistenceManager


class MySql(PersistenceManager):
    def save(self):
        print("save in my db")
        pass

    def remove(self, id: str):
        print("remove in my db")
        pass

    def update(self, id: str, data):
        print("update in my db")
        pass

    def get_entity(self, id: str):
        print("get in my db")
        pass
