from dataclasses import dataclass


@dataclass
class Season:
    year: int
    url: str

    def __eq__(self, other):
        return self.year == other.year

    def __hash__(self):
        return hash(self.year)

    def __str__(self):
        return f"{self.year}"

    def __repr__(self):
        return str(self)