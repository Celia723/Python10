

class Artifact:
    def __init__(self, name: str, power: int, artifact_type: str):
        self.name: str = name
        self.power: int = power
        self.artifact_type: str = artifact_type

    def __str__(self):
        return f"{self.name} ({self.artifact_type}) - Power {self.power} "


class Arsenal:
    def __init__(self):
        self._artifacts: list[Artifact] = []

    def add_artifact(self, artifact: Artifact):
        self._artifacts.append(artifact)

    def get_artifacts_by_type(self, artifact_type: str) -> list[Artifact]:
        return list(filter(
            lambda artifact:
            artifact.artifact_type == artifact_type, self._artifacts))

    def total_power(self) -> int:
        return sum(map(lambda artifact: artifact.power, self._artifacts))
