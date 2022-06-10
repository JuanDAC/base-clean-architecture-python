
from app.infrastructure.persistence.interfaces import PersistenceManager


class FileStorage(PersistenceManager):
    def save(self):
        print("save in my file storage")

    def remove(self, id: str):
        print("remove in my file storage")

    def update(self, id: str, data):
        print("update in my file storage")

    def get_entity(self, id: str):
        print("get in my file storage")
