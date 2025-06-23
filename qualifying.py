from dataclasses import dataclass


@dataclass
class Qualifying:
    qualifyId: int
    raceId: int
    driverId: int
    constructorId: int
    number: int
    position: int
    q1: str
    q2: str
    q3:str

    def __eq__(self, other):
        return self.qualifyId == other.qualifyId

    def __hash__(self):
        return hash(self.qualifyId)

    def __str__(self):
        return f"{self.qualifyId} - {self.raceId} - {self.driverId}"

    def __repr__(self):
        return str(self)