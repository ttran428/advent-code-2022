from __future__ import annotations
from typing import Mapping, Sequence, List, Set, Tuple, Dict, Iterable
from utils import parse_file, parse_string

filepath = "data/day8.txt"

def create_graph(data: Sequence[str]) -> List[List[int]]:
    graph = []
    for row in data:
        graph.append([int(tree) for tree in row])
    return graph 


def visible_from_left_right(range1: Iterable, range2: Iterable, graph: List[List[int]], visible: Set) -> None:
    range1 = list(range1)
    range2 = list(range2)
    for i in range1:
        max_height = -1 
        for j in range2:
            current_height = graph[i][j]
            if current_height > max_height:
                # breakpoint()
                visible.add((i, j))
                max_height = current_height

def visible_from_top_bottom(range1: Iterable, range2: Iterable, graph: List[List[int]], visible: Set) -> None:
    # only realized half way through that i couldn't just use one visible function sigh...
    range1 = list(range1)
    range2 = list(range2)
    for j in range1:
        max_height = -1 
        for i in range2:
            current_height = graph[i][j]
            if current_height > max_height:
                visible.add((i, j))
                max_height = current_height

def visualize(graph: List[List[int]], visible: Set) -> List[List[int]]:
    # helper method to just visualize visible tree output
    visible_graph =  [[0 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    for x, y in visible:
        visible_graph[x][y] = 1
    return visible_graph
    
def visible_trees(graph: List[List[int]]) -> Set:
    visible = set()

    visible_from_left_right(range(len(graph)), range(len(graph[0])), graph, visible)
    visible_from_left_right(range(len(graph)), reversed(range(len(graph[0]))), graph, visible)
    visible_from_top_bottom(range(len(graph)), range(len(graph[0])), graph, visible)
    visible_from_top_bottom(range(len(graph)), reversed(range(len(graph[0]))), graph, visible)

    return visible
            
def test_example() -> None:
    example = """30373
    25512
    65332
    33549
    35390"""
    data = parse_string(example)
    graph = create_graph(data)
    visible = visible_trees(graph)
    visible_graph = visualize(graph, visible)

def main1(filepath: str) -> int:
    data = parse_file(filepath)
    graph = create_graph(data)
    return len(visible_trees(graph))

assert main1(filepath) == 1859 


def get_scenic_score(graph: List[List[int]], i: int, j: int) -> int:
    tree_height = graph[i][j] 

    left = 0
    for x in reversed(range(j)):
        left += 1
        if tree_height <= graph[i][x]:
            break 

    right = 0
    for x in range(min(j +1, len(graph[0])), len(graph[0])):
        right += 1
        if tree_height <= graph[i][x]:
            break 

    up = 0
    for y in reversed(range(i)):
        up += 1 
        if tree_height <= graph[y][j]:
            break

    down = 0
    for y in range(min(i + 1, len(graph)), len(graph[0])):
        down += 1 
        if tree_height <= graph[y][j]:
            break
    return left * right * up * down 

def max_scenic_score(graph: List[List[int]]) -> int: 
    max_scenic_score = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            scenic_score = get_scenic_score(graph, i, j)
            max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score

def main2(filepath: str) -> int:
    data = parse_file(filepath)
    graph = create_graph(data)
    return max_scenic_score(graph) 

assert main2(filepath) == 332640 
