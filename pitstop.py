from dataclasses import dataclass
from datetime import time


@dataclass
class Pitstop:
    raceId: int
    driverId: int
    stop: int
    lap: int
    time: time
    duration: str
    milliseconds: str

    def __eq__(self, other):
        return self.raceId == other.raceId and self.driverId == other.driverId and self.stop == other.stop

    def __hash__(self):
        return hash((self.raceId, self.driverId, self.stop))

    def __str__(self):
        return f"{self.raceId} - {self.driverId} - {self.stop}"

    def __repr__(self):
        return str(self)