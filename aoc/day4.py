from typing import Sequence, List, Set, Tuple 

filepath = "../data/day4.txt"

def parse_file(filepath: str) -> Sequence[str]:
    with open(filepath) as file:
        data = file.read()
        return data.split("\n")[:-1] # ignore the newline at the end

def parse_pair(pair: str) -> Tuple[Sequence[str], Sequence[str]]:
    pair1, pair2 = pair.split(",")
    pair1, pair2 = pair1.split("-"), pair2.split("-")
    return [int(p) for p in pair1], [int(p) for p in pair2]


def contained_pairs(pairs: Sequence[str]) -> int:
    count = 0
    for pair in pairs:
        pair1, pair2 = parse_pair(pair)
        if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
            count += 1 
        elif pair2[0] <= pair1[0] and pair2[1] >= pair1[1]:
            count += 1
    return count

def main1(filepath: str) -> int:
  pairs = parse_file(filepath)  
  return contained_pairs(pairs)

assert main1(filepath) == 424

# part 2
def overlapping_pairs(pairs: Sequence[str]) -> int:
    count = 0
    for pair in pairs:
        pair1, pair2 = parse_pair(pair)
        if pair1[1] < pair2[0]:
            pass 
        elif pair2[1] < pair1[0]:
            pass 
        else:
            count += 1
    return count

def main2(filepath: str) -> int:
  pairs = parse_file(filepath)  
  return overlapping_pairs(pairs)

assert main2(filepath) == 804
