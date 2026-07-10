from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def aquaspalsh(target: str, power: int) -> str:
    return f"Aquasplash hits {target} for {power} damage"


def tpmattack(target: str, power: int) -> str:
    return f"TPMattack hits {target} for {power} damage"


def less_than_42(num: int):
    return 42 > num


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combinator(target: str, power: int):
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)

    return combinator


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiply(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return multiply


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def to_test_the_condition(target: str, power: int):
        if condition(power):
            return spell(target, power)
        else:
            return "*sad violin music*  The number doens't pass the condition"

    return to_test_the_condition


def spell_sequence(spells: list[Callable]) -> Callable:

    def comb_all_functions(target: str, power: int):
        results: list[str] = [m(target, power) for m in spells]
        return (results)

    return comb_all_functions


if __name__ == "__main__":
    print("spell_combiner")
    comb = spell_combiner(tpmattack, aquaspalsh)
    print(comb("antonio recio", 10000))

    print()
    print("power_amplifier")
    super_fireball = power_amplifier(fireball, 5)
    print(super_fireball("asturias", 5))

    print()
    print("conditional_caster")
    to_test = conditional_caster(less_than_42, aquaspalsh)
    print(to_test("Margarita", 40))
    print(to_test("Margarita", 42))

    print()
    print("spell sequence")
    comb_funtions = spell_sequence([fireball, aquaspalsh, tpmattack])
    results = comb_funtions("Alejandria", 800)
    print(results)
