from src.parsers import InstructionsParser, CompassParser, PositionParser
from src.foundations import Instructions, Compass, Position
import pytest


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

def test_position_parser_returns_coordinates_with_direction():
    input = "2 4 N"
    parser = PositionParser.parse(input)
    assert parser == Position(2, 4, Compass.NORTH)
                            # x, y, direction

def test_position_parser_returns_none_for_empty_input():
    input = ""
    parser = PositionParser.parse(input)
    assert parser == None

def test_position_parser_returns_coordinates_with_direction():
    input = "2 N"
    with pytest.raises(TypeError, match="Please enter x and y position, followed by direction"):
        PositionParser.parse(input)


