from src.instructions_parser import InstructionsParser
from src.foundations import Instructions

def test_parser_returns_list():
    input = "L"

    parser = InstructionsParser.parse(input)

    assert parser == [Instructions.LEFT]