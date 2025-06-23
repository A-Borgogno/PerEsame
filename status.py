from dataclasses import dataclass


@dataclass
class Status:
    statusId: int
    status: str

    def __eq__(self, other):
        return self.statusId == other.statusId

    def __hash__(self):
        return hash(self.statusId)

    def __str__(self):
        return f"{self.statusId} - {self.status}"

    def __repr__(self):
        return str(self)