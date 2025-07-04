from src.instructions_parser import InstructionsParser, CompassParser
from src.foundations import Instructions, Compass

def test_instructions_parser_returns_list():
    input = "L"
    parser = InstructionsParser.parse(input)
    assert parser == [Instructions.LEFT]

def test_instructions_parser_returns_filtered_list_mixed_inputs():
    input = "LMPOR"
    parser = InstructionsParser.parse(input)
    print("output:", parser)
    assert parser == [Instructions.LEFT,
                      Instructions.MOVE,
                      Instructions.RIGHT]
    
def test_instructions_parser_returns_empty_list_if_invalid_inputs():
    input = "QPAZX"
    parser = InstructionsParser.parse(input)
    assert parser == []

def test_compass_parser_returns_list():
    input = "N"
    parser = CompassParser.parse(input)
    assert parser == [Compass.NORTH]

def test_compass_parser_returns_filtered_list_of_mixed_inputs():
    input = "NP47SEZ"
    parser = CompassParser.parse(input)
    assert parser == [Compass.NORTH,
                      Compass.SOUTH,
                      Compass.EAST]
def test_compass_parser_returns_empty_list_if_invalid_inputs():
    input = 846637
    parser = CompassParser.parse(input)
    assert parser == []

