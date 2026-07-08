from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    initial = initial_power

    def accumulator(power: int) -> int:
        nonlocal initial
        initial += power
        return initial

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    enchantment = enchantment_type

    def factory(object: str) -> str:
        return f"{enchantment} {object}"

    return factory


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Callable) -> None:
        vault[key] = value

    def recall(key: str) -> str:
        return vault.get(key, "Memory not foud")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print()
    print("Testing spell accumulator...")
    fun_sum = spell_accumulator(2)
    print(fun_sum(1))
    print(fun_sum(2))
    fun_sum2 = spell_accumulator(3)
    print(fun_sum2(3))

    print()
    print("Testing enchantment factory...")
    factory = enchantment_factory("Flamig")
    print(factory("Sword"))

    print()
    print("Testing memory vault...")
    system = memory_vault()
    print("Store 'secret' = 42")
    system["store"]("secret", 42)
    print(system["recall"]("secret"))
    print(system["recall"]("unknown"))
