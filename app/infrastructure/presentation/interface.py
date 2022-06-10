from abc import ABC
from abc import abstractmethod


class PresentationManager(ABC):
    @abstractmethod
    def get_idetification():
        pass