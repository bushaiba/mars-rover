from src.foundations import Instructions, Compass, Position, PlateauSize
from typing import List

class InstructionsParser():
    def parse(instructions_str: str):
        
        if not isinstance(instructions_str, str):
            return []
        
        parsed = []
        for char in instructions_str:
            if char in [i.value for i in Instructions]:
                parsed.append(Instructions(char))
        return parsed
    
class CompassParser():
    def parse(compass_str: str):
        
        if not isinstance(compass_str, str):
            return []
        
        parsed = []
        for char in compass_str:
            if char in [i.value for i in Compass]:
                parsed.append(Compass(char))
        return parsed

    
class PositionParser():
    def parse(position_str: str):
        if not isinstance(position_str, str) or position_str == "":
            return None
        
        cleaned = position_str.strip().split()
        # strip spaces etc, split each element into a list e,g, ['x', 'y', 'direction']
        try:
            x, y, direction = cleaned
        # tries to unpack the 3 elements expected in 'cleaned' into their own variables
        # if there are more or less elements than 3, it'll proceed to except
        except ValueError:
            raise TypeError("Please enter x and y position, followed by direction")

        if not x.isdigit() and not y.isdigit():
            return None
        # checks if x and y are digits (they're still strings)
        if direction not in [i.value for i in Compass]:
            return None
        # checks if direction is found as a value in Compass enums
        return Position(int(x), int(y), Compass(direction))
        

class PlateauSizeParser():
    def parse(plateausize_str: str):
        if not isinstance(plateausize_str, str):
            return None

        pass