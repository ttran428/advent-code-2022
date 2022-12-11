from typing import Mapping, Sequence, List, Set, Tuple, Dict, Iterable
from utils import parse_file, parse_string

filepath = "../data/day10.txt"


def get_register_values(instructions: Sequence[str]) -> Sequence[int]:
    register_x = 1
    register_values = []
    for instruction in instructions: 
        if instruction == "noop":
            register_values.append(register_x) 
        elif "addx" in instruction:
            _, val = instruction.split(" ") 
            val = int(val)
            register_values.append(register_x)
            register_values.append(register_x)
            register_x += val
        else:
            raise ValueError("Instruction not understood")
        

    return register_values

def main1(filepath: str) -> int:
    instructions = parse_file(filepath)
    register_values = get_register_values(instructions)    
    indices = [20, 60, 100, 140, 180, 220]
    return sum([register_values[index - 1] * index for index in indices])

assert main1(filepath) == 14520 


def find_sprite(register_values: Sequence[int], start_idx: str) -> Sequence[str]:
    visible_sprite = []
    for draw_position, register in enumerate(register_values[start_idx: start_idx + 40]):
        if draw_position in [register - 1, register, register + 1]:
            visible_sprite.append("#")
        else:
            visible_sprite.append(".")
    return visible_sprite

def main2(filepath: str) -> None:
    instructions = parse_file(filepath)
    register_values = get_register_values(instructions)    
    for i in range(0, 240, 40):
        print(find_sprite(register_values, i))


print(main2(filepath))
