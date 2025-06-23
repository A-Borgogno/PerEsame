from dataclasses import dataclass


@dataclass
class Laptime:
    raceId: int
    driverId: int
    lap: int
    position: int
    time: str
    milliseconds: int

    def __eq__(self, other):
        return self.raceId == other.raceId and self.driverId == other.driverId and self.lap == other.lap

    def __hash__(self):
        return hash((self.raceId, self.driverId, self.lap))

    def __str__(self):
        return f"{self.raceId} - {self.driverId} - {self.lap}"

    def __repr__(self):
        return str(self)