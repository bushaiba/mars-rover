from src.foundations import Instructions, Compass, Position, PlateauSize
from typing import List

class InstructionsParser():
    def parse(instructions_str: str) -> List[Instructions]:
        
        if not isinstance(instructions_str, str):
            return []
        
        parsed = []
        for char in instructions_str:
            if char in [i.value for i in Instructions]:
                parsed.append(Instructions(char))
        return parsed
    
class CompassParser():
    def parse(compass_str: str) -> List[Compass]:
        
        if not isinstance(compass_str, str):
            return []
        
        parsed = []
        for char in compass_str:
            if char in [i.value for i in Compass]:
                parsed.append(Compass(char))
        return parsed
