from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.attack())
    print(base.describe())
    print(evolved.attack())
    print(evolved.describe())


def fight_factory(factory1: CreatureFactory, factory2) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    print("Testing Factory")
    test_factory(FlameFactory())
    print("\nTesting Factory")
    test_factory(AquaFactory())
    print("\nTesting battle")
    fight_factory(FlameFactory(), AquaFactory())
