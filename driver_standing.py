from dataclasses import dataclass

# Questa classe rappresenta delle relazioni tra tabelle, usare solo se necessario
@dataclass
class DriverStanding:
    driverStandingsId: int
    raceId: int
    driverId: int
    points: float
    position: int
    positionText: str
    wins: int

    def __eq__(self, other):
        return self.driverStandingsId == other.driverStandingsId

    def __hash__(self):
        return hash(self.driverStandingsId)

    def __str__(self):
        return f"{self.driverStandingsId} - {self.raceId} - {self.driverId}"

    def __repr__(self):
        return str(self)