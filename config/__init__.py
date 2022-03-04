from abc import ABC, abstractmethod


class Config(ABC):
    @abstractmethod
    def load(self, **kwargs):
        pass

    @abstractmethod
    def get(self, key):
        pass
