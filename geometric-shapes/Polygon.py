from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def perimeter(self):
        pass;
