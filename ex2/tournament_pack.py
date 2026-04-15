from ex0.battle_package import Creature
from ex1.capacitor_package import HealCapability, TransformCapability
from abc import ABC, abstractmethod


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException("Battle error, "
                                           "aborting tournament:")
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException("Battle error, "
                                           "aborting tournament:")
        return (f"{creature.transform()}\n"
                f"{creature.attack()}\n{creature.revert()}\n")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        pass

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException("Battle error,"
                                           " aborting tournament:")
        return f"{creature.attack()}\n{creature.heal()}"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
