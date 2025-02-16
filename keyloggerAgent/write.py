from abc import ABC,abstractmethod


class writeTo(ABC):
    @abstractmethod
    def write(self,data):
        pass