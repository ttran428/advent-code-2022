from typing import Mapping, Sequence, List, Set, Tuple, Dict, Iterable, Union
from time import sleep
from utils import parse_file, parse_string, parse_by_split_lines
from collections import deque
from copy import deepcopy 
import json

filepath = "data/day13.txt"


Packet = List[Union[List, int]] 
Pair = Tuple[Packet, Packet]

def parse_packet(packet_data: str) -> Packet:
    return json.loads(packet_data)

def parse_pairs(data: Sequence[Sequence[str]]) -> List[Pair]:
    pairs = []
    for pair_data in data:
        pair = (parse_packet(pair_data[0]), parse_packet(pair_data[1]))
        pairs.append(pair)
    return pairs

def in_correct_order(pair: Pair) -> bool:
    packet1, packet2 = pair 

    for item1, item2 in zip(packet1, packet2):
        if isinstance(item1, int) and isinstance(item2, int):
            if item2 < item1:
                return False 
        elif isinstance(item1, list) and isinstance(item2, list):
            if not in_correct_order((item1, item2)):
                return False
        elif isinstance(item1, list) and isinstance(item2, int):
            if not in_correct_order((item1, [item2])):
                return False 
        elif isinstance(item1, int) and isinstance(item2, list):
            if not in_correct_order(([item1], item2)):
                return False 
        else:
            raise ValueError("Case not understood")

    breakpoint()
    return len(packet1) <= len(packet2)


def find_correct_pairs(pairs: List[Pair]) -> List[int]:
    correct_indices = []
    for i, pair in enumerate(pairs):
        if in_correct_order(pair):
            correct_indices.append(i + 1)
    return correct_indices

def main1(filepath: str) -> int:
    example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    # data = parse_by_split_lines(filepath)
    data = parse_by_split_lines(example,string=True)
    pairs = parse_pairs(data) 

    in_correct_order(pairs[1]) 

    # correct_pairs = find_correct_pairs(pairs)
    breakpoint()
    return sum(correct_pairs)


print(main1(filepath))
    
# assert main1(filepath) == 449
