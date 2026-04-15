from ex0.battle_package import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1.capacitor_package import HealingCreatureFactory, \
    TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.tournament_pack import BattleStrategy
from typing import List, Tuple


def battle(lst: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    i = 0
    print("*** Tournament ***")
    print(f"{len(lst)} oppenents involved")
    for first_opponent in lst[i:]:
        creature1, strategy1 = first_opponent
        for opponent in lst[i + 1:]:
            creature, strategy = opponent
            print("\n* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
            except Exception as e:
                print(f"{e} Invalid Creature  "
                      f"'{creature1.name}' for this"
                      f" {strategy1.__class__.__name__})")
                return
            else:
                print(strategy1.act(creature1))
            try:
                strategy.act(creature)
            except Exception as e:
                print(f"{e} Invalid Creature "
                      f"'{creature.name}' for this "
                      f"{strategy.__class__.__name__})")
                return
            else:
                print(strategy.act(creature))
        i += 1


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print(" [ (Flameling,Normal), (Healing+Defensive)]")
    flameling = FlameFactory()
    normal = NormalStrategy()
    Sproutling = HealingCreatureFactory()
    defense = DefensiveStrategy()
    lst1 = [(flameling.create_base(), normal),
            (Sproutling.create_base(), defense)]
    battle(lst1)
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    agg = AggressiveStrategy()
    lst2 = [(flameling.create_base(), agg),
            (Sproutling.create_base(), defense)]
    try:
        battle(lst2)
    except Exception as e:
        print(f"{e}")
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    aqua = AquaFactory()
    trans = TransformCreatureFactory()
    lst3 = [(aqua.create_base(), normal),
            (Sproutling.create_base(), defense),
            (trans.create_base(), agg)]
    battle(lst3)
