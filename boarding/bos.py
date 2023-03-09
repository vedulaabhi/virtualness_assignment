from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class BoardingCard:
    transportation: str
    origin: str
    destination: str
    transportationNumber: Optional[str] = None
    seat: Optional[str] = None
    gate: Optional[str] = None
    baggageDrop: Optional[str] = None
