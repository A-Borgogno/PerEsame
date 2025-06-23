from dataclasses import dataclass

# Questa classe rappresenta delle relazioni tra tabelle, usare solo se necessario
@dataclass
class ConstructorStanding:
    constructorStandingsId: int
    raceId: int
    constructorId: int
    points: float
    position: int
    positionText: str
    wins: int

    def __eq__(self, other):
        return self.constructorStandingsId == other.constructorStandingsId

    def __hash__(self):
        return hash(self.constructorStandingsId)

    def __str__(self):
        return f"{self.constructorStandingsId} - {self.raceId} - {self.constructorId}"

    def __repr__(self):
        return str(self)