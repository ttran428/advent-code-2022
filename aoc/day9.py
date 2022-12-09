
from typing import Mapping, Sequence, List, Set, Tuple, Dict, Iterable
from utils import parse_file, parse_string

filepath = "../data/day9.txt"

Coordinate = Tuple[int, int]

def parse_instructions(data: Sequence[str]) -> Sequence[str]:
    instructions = []
    for row in data:
        direction, count = row.split(" ")
        count = int(count)
        for _ in range(count):
            instructions.append(direction)

    return instructions

def move_coordinate(head: Coordinate, instruction: str) -> Coordinate:
    if instruction == "U":
        return (head[0], head[1] + 1)
    if instruction == "D":
        return (head[0], head[1] - 1)
    if instruction == "L":
        return (head[0] - 1, head[1])
    if instruction == "R":
        return (head[0] + 1, head[1])

def move_tail(tail: Coordinate, head: Coordinate) -> Coordinate:
    # if in length one, return tail 
    if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1: 
        return tail
    # if on same plane then just move coordinate 
    if abs(tail[0] - head[0]) == 0 and abs(tail[1] - head[1]) == 2:
        if head[1] > tail[1]:
            return (tail[0], tail[1] + 1)
        else:
            return (tail[0], tail[1] - 1)
    elif abs(tail[0] - head[0]) == 2 and abs(tail[1] - head[1]) == 0:
        if head[0] > tail[0]:
            return (tail[0] + 1, tail[1])
        else:
            return (tail[0] - 1, tail[1])

    if head[0] > tail[0] and head[1] > tail[1]:
        return (tail[0] + 1, tail[1] + 1)
    elif head[0] < tail[0] and head[1] > tail[1]:
        return (tail[0] - 1, tail[1] + 1)
    elif head[0] > tail[0] and head[1] < tail[1]:
        return (tail[0] + 1, tail[1] - 1)
    elif head[0] < tail[0] and head[1] < tail[1]:
        return (tail[0] - 1, tail[1] - 1)

    raise ValueError("try again")


def tail_visited(instructions: Sequence[str]) -> Set[Coordinate]:
    head = (0,0)
    tail = (0,0)

    visited = set()
    visited.add(tail)

    for instruction in instructions:
        head = move_coordinate(head, instruction)
        tail = move_tail(tail, head)

        visited.add(tail)

    return visited


example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

data = parse_string(example)
instructions = parse_instructions(data)
ted = tail_visited(instructions)



def main1(filepath: str) -> int:
    data = parse_file(filepath)
    instructions = parse_instructions(data)
    return len(tail_visited(instructions))
assert main1(filepath) == 5683 



def ten_knots_visited(instructions: Sequence[str]) -> Set[Coordinate]:
    knots = [(0,0) for _ in range(10)]

    visited = set()
    visited.add((0,0))
    
    for instruction in instructions:
        for i in range(len(knots)):
            if i == 0:
                knots[i] = move_coordinate(knots[i], instruction)
            else:
                knots[i] = move_tail(knots[i], knots[i - 1])

            if i == 9:
                visited.add(knots[i])
    return visited


example = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

data = parse_string(example)
instructions = parse_instructions(data)
ted = ten_knots_visited(instructions)


def main2(filepath: str) -> int:
    data = parse_file(filepath)
    instructions = parse_instructions(data)
    return len(ten_knots_visited(instructions))

assert main2(filepath) == 2372 
