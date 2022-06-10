from abc import ABC
from abc import abstractmethod


""" interface PersistenceManager """
class PersistenceManager(ABC):

    @abstractmethod
    def save():
        pass

    @abstractmethod
    def remove(id: str):
        pass

    @abstractmethod
    def update(id: str, data):
        pass

    @abstractmethod
    def get_entity(id: str):
        pass
