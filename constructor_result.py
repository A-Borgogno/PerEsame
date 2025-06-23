from dataclasses import dataclass

# Questa classe rappresenta delle relazioni tra tabelle, usare solo se necessario
@dataclass
class ConstructorResult:
    constructorResultsId: int
    raceId: int
    constructorId: int
    points: float
    status: str

    def __eq__(self, other):
        return self.constructorResultsId == other.constructorResultsId

    def __hash__(self):
        return hash(self.constructorResultsId)

    def __str__(self):
        return f"{self.constructorResultsId} - {self.raceId} - {self.constructorId}"

    def __repr__(self):
        return str(self)