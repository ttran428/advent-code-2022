from typing import Mapping, Sequence, List, Set, Tuple, Dict, Iterable
from time import sleep
from utils import parse_file, parse_string, parse_by_split_lines
from collections import deque
from copy import deepcopy 

filepath = "data/day12.txt"

Point = Tuple[int, int]
Graph = List[str]
def find_point(letter: str, graph: Graph) -> Point:
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == letter:
                return (i, j)
    raise ValueError("no letter found")

def valid_coordinate(coordinate: Point, graph: Graph) -> bool:
    i, j = coordinate 
    return i in range(len(graph)) and j in range(len(graph[0]))

def get_elevation(point: Point, graph: Graph) -> int: 
    return ord(graph[point[0]][point[1]])

def possible_to_reach(curr: Point, coordinate: Point, graph: Graph) -> bool:
    return get_elevation(coordinate, graph) <= get_elevation(curr, graph) + 1 

def get_neighbors(curr: Point, graph: Graph) -> List[Point]:
    neighbors = []
    
    i, j = curr 
    coordinates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for coordinate in coordinates:
        if valid_coordinate(coordinate, graph) and possible_to_reach(curr, coordinate, graph):
            neighbors.append(coordinate)
    return neighbors     

def get_path(start: Point, end: Point, next_to_previous: Mapping[Point, Point]):
    curr = end 
    path = []
    while curr != start:
        path.append(curr)
        curr = next_to_previous[curr]
    
    return path[::-1]


def bfs(graph: List[str]) -> int:
    start = find_point("S", graph)
    end = find_point("E", graph)
   
    # assumes that there is only one S and E
    graph[start[0]] = graph[start[0]].replace("S", "a")
    graph[end[0]] = graph[end[0]].replace("E", "z")

    queue = deque() 
    queue.append(start)
    next_to_previous = {}
    seen = set() 
    while queue:
        curr = queue.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        
        if curr == end:
            path = get_path(start, end, next_to_previous)
            return len(path)

        for neighbor in get_neighbors(curr, graph):
            if neighbor not in seen:
                next_to_previous[neighbor] = curr 
                queue.append(neighbor)
    
    return float("inf")
    raise ValueError("not found end")
        



def main1(filepath: str) -> int:
    graph = parse_file(filepath)
    return bfs(graph)

assert main1(filepath) == 449


def create_graphs(data: List[str]) -> List[Graph]:
    graphs = []

    start = find_point("S", data)
    # assumes that there is only one S 
    data[start[0]] = data[start[0]].replace("S", "a")

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "a":
                graph = deepcopy(data)
                graph[i] = graph[i][:j] + "S" + graph[i][j + 1:]
                graphs.append(graph)
    return graphs

def shortest_path(graphs: List[Graph]) -> int:
    shortest = float("inf")
    for graph in graphs:
        shortest = min(shortest, bfs(graph))
    return shortest

def main2(filepath: str) -> int:
    data = parse_file(filepath)
    graphs = create_graphs(data)
    return shortest_path(graphs)

assert main2(filepath) == 443
