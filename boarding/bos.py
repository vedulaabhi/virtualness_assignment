from dataclasses import dataclass


@dataclass(frozen=True)
class BoardingCard:
    transportation: str
    transportation_number: str
    origin: str
    destination: str
    seat: str
    gate: str
    baggageDrop: str
