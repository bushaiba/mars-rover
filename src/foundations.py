from enum import Enum
from dataclasses import dataclass



class Instructions(Enum):
    LEFT = "L"
    RIGHT = "R"
    MOVE = "M"

class Compass(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

@dataclass
class Position():
    x: int
    y: int
    direction: Compass

@dataclass
class PlateauSize():
    width: int
    height: int

