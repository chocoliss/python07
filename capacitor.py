from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex1.capacitor_package import HealCapability,TransformCapability

if __name__ == "__main__":
    print("Testing Creature with healing capability")
    print("base")
    heal = HealingCreatureFactory()
    sproutling = heal.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    if isinstance(sproutling, HealCapability):
        print(sproutling.heal())
    Bloomelle = heal.create_evolved()
    print(" evolved")
    print(Bloomelle.describe())
    print(Bloomelle.attack())
    if isinstance(sproutling, TransformCapability):
        print(Bloomelle.heal)
    print("\nTesting Creature with transform capability")
    print("base:")
    trans = TransformCreatureFactory()
    shiftling = trans.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())
    print(" evolved")
    Morphagon = trans.create_evolved()
    print(Morphagon.describe())
    print(Morphagon.attack())
    print(Morphagon.transform())
    print(Morphagon.attack())
    print(Morphagon.revert())
