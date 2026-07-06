

def artifact_sorter(artifacts: list[dict])-> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse= True)

def power_filter(mages: list[dict], min_power: int)-> list[dict]:
    return list(filter(lambda mage:mage['power'] >= min_power, mages))

def spell_transformer(spells: list[str])-> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))

def mage_stats(mages: list[dict])-> dict:
    if not mages:
        return {"max_power":0, "min_power":0, "avg_power":0.0}

    min_power = min(mages, key= lambda power: power['power'])['power']
    max_power = max(mage_stats, key= lambda power:power['power'])['power']

    total_power = sum(map(lambda m:m['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }
