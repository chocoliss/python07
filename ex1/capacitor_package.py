from abc import ABC, abstractmethod
from .ex0 import CreatureFactory, Creature

class HealCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self,target: str) -> str:
        pass

class TransformCapability(ABC):
    def __init__(self, state: str) -> None:
        pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

class Sproutling(Creature,HealCapability):
    def __init__(self) -> None:
        Creature.__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return