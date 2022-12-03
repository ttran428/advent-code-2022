from typing import Sequence 
from heapq import heappush, heappop

filepath = "../data/day1.txt"

def parse_foods(filepath: str) -> Sequence[str]:
    with open(filepath) as file:
        data = file.read()
        return data.split("\n")
        
def most_n_calories(filepath: str, n: int) -> int: 
    foods = parse_foods(filepath)
    heap = []
    curr_total_calories = 0

    for calories in foods:
        if calories == "":
            heappush(heap,  -1 *curr_total_calories)
            curr_total_calories = 0
        else:
            curr_total_calories += int(calories)
    
    top_n_calories = [-1 * heappop(heap) for _ in range(n)]
    return sum(top_n_calories)

part_1_answer = most_n_calories(filepath, 1)
assert part_1_answer == 71924
part_2_answer = most_n_calories(filepath, 3)
assert part_2_answer == 210406



