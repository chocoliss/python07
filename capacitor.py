from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex0 import Creature, CreatureFactory

if __name__ == "__main__":
    print("Testing Creature with healing capability")
    print("base")
    heal = HealingCreatureFactory.create_base()
    print(heal)