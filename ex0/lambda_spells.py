
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    min_power = min(mages, key=lambda power: power['power'])['power']
    max_power = max(mages, key=lambda power: power['power'])['power']

    total_power = sum(map(lambda m: m['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":

    artifacts = [{'name': 'Earth Shield', 'power': 67, 'type': 'armor'},
                 {'name': 'Lightning Rod', 'power': 87, 'type': 'focus'},
                 {'name': 'Wind Cloak', 'power': 65, 'type': 'armor'},
                 {'name': 'Shadow Blade', 'power': 62, 'type': 'armor'}]

    mages = [{'name': 'Jordan', 'power': 79, 'element': 'light'},
             {'name': 'Jordan', 'power': 87, 'element': 'earth'},
             {'name': 'Storm', 'power': 91, 'element': 'shadow'},
             {'name': 'Ash', 'power': 84, 'element': 'ice'},
             {'name': 'Riley', 'power': 77, 'element': 'earth'}]

    spells = ['lightning', 'blizzard', 'tornado', 'fireball']

    print("Artifacts sorted by power:")
    print(artifact_sorter(artifacts))
    print()
    print("Mages with power greater than or equal to the filter:")
    print(power_filter(mages, 91))
    print()
    print("Transformed spells:")
    print(spell_transformer(spells))
    print()
    print("Mage stats (max, min, and average power):")
    print(mage_stats(mages))
