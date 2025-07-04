from src.foundations import Instructions
from typing import List

class InstructionsParser():
    def parse(instructions_str: str) -> List[Instructions]:
        
        parsed = []
        for char in instructions_str:
            if char in [i.value for i in Instructions]:
                parsed.append(Instructions(char))
        return parsed
