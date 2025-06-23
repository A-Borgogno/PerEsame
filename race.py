from dataclasses import dataclass
from datetime import datetime, time


@dataclass
class Race:
    raceId: int
    year: int
    round: int
    circuitId: int
    name: str
    date: datetime
    time: time
    url: str

    def __eq__(self, other):
        return self.raceId == other.raceId

    def __hash__(self):
        return hash(self.raceId)

    def __str__(self):
        return f"{self.raceId}"

    def __repr__(self):
        return str(self)