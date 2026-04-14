from ex1.capacitor_package import HealingCreatureFactory, TransformCreatureFactory
from abc import ABC, abstractmethod

class BattleStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def act(self) -> bool:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass

class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> bool:
        if self.is_valid(creature):
            return True
        return False
        

    def is_valid(self, strategy: Creature) -> bool:
        if isinstance(strategy, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self,) -> None:
        if is_valid()