from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MarutiSuzuki(Engine):
    def start(self):
        print("Maruti Suzuki engine started")

    def stop(self):
        print("Maruti Suzuki engine stopped")