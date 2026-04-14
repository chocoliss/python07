from abc import ABC, abstractmethod
from ex0.battle_package import CreatureFactory, Creature


class HealCapability(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.time = 0

    def attack(self) -> str:
        if self.time == 0:
            self.time += 1
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", " Normal/Dragon")
        self.time = 0

    def attack(self) -> str:
        if self.time == 0:
            self.time += 1
            return "Morohagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()
