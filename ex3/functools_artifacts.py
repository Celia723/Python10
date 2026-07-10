from operator import add, mul
import functools
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    valid_operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in valid_operations:
        raise ValueError(f"Unkown operation {operation}")

    matematic_funtcion = valid_operations[operation]
    result = functools.reduce(matematic_funtcion, spells)

    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    fire_enchant = functools.partial(base_enchantment, 50, "fire")

    ice_enchant = functools.partial(base_enchantment, 50, "ice")

    lightning_enchant = functools.partial(base_enchantment, 50, "lightning")

    return {
        "fire": fire_enchant,
        "ice": ice_enchant,
        "lightning": lightning_enchant
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return spell

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return dispatcher


if __name__ == "__main__":

    spell_powers = [22, 21, 46, 34, 24, 14]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [9, 18, 12]

    print("Testing spell_reducer...")
    print(f"List of numbers: {spell_powers}")
    print(f"List of operation: {operations}")
    result_resducer: list[int] = [
        spell_reducer(spell_powers, op) for op in operations]
    print(f"Results: {result_resducer}")
    print()

    print("Testing fibonacci...")
    fibonacci_results = [memoized_fibonacci(n) for n in fibonacci_tests]
    print(fibonacci_results)

    print()
    print("Testing spell dispatcher...")
    fun = spell_dispatcher()
    print(f"Damage spell: {fun(4)}")
    print(f"Enchantment: {fun('Fireball')}")
    print(f"Multi-cast: {fun(['Fireball', 'attcksupreme'])}")
    print(fun({'hllo': 4}))
