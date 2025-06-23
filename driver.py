from dataclasses import dataclass
from datetime import date


@dataclass
class Driver:
    driverId: int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: date
    nationality: str
    url: str

    def __eq__(self, other):
        return self.driverId == other.driverId

    def __hash__(self):
        return hash(self.driverId)

    def __str__(self):
        return f"{self.driverId} - {self.forename} {self.surname}"

    def __repr__(self):
        return str(self)