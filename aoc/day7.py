from __future__ import annotations
from typing import Mapping, Sequence, List, Set, Tuple, Dict
from utils import parse_file

filepath = "data/day7.txt"

class Tree:
    def __init__(self, name: str, value: int = 0, children: List[Tree] = []):
        self.value = value 
        self.name = name
        self.children = children 
        self.parent = None

    def add_child(self, child: Tree) -> None:
        if child.name in [child.name for child in self.children]:
            return None 
        else:
            child.parent = self 
            self.children = self.children + [child]
            # TODO: why does the line below link child.children = child?
            # self.children.append(child)
    
    def get_child(self, child_name: str) -> Tree:
        matching_children = [child for child in self.children if child.name == child_name]
        if len(matching_children) == 0:
            raise ValueError(f"No children found with {child_name=} in tree {self.name}")
        if len(matching_children) > 1:
            raise ValueError(f"multiple children found with {child_name=} in tree {self.name}")
        return matching_children[0]

    def __repr__(self):
        return f"Tree {self.name} has children {[child.name for child in self.children]}"
    
    @property
    def full_name(self) -> str:
        name = self.name
        curr_tree = self.parent 
        while curr_tree:
            name = curr_tree.name + "/" + name
            curr_tree = curr_tree.parent 
        return name

def create_tree(instructions: Sequence[str]) -> Tree:
    i = 0
    dir_tree = Tree("root")
    curr_tree = dir_tree
    while i < len(instructions):
        instruction = instructions[i]
        instruction_parts = instruction.split(" ")
        command = instruction_parts[1]
        if command == "ls":
            i += 1 
            while i < len(instructions) and instructions[i][0] != "$":
                if instructions[i][:3] == "dir":
                    _, dir = instructions[i].split(" ")
                    curr_tree.add_child(Tree(name=dir))
                else: # is a file 
                    size, file = instructions[i].split(" ")
                    curr_tree.add_child(Tree(name=file, value=int(size)))
                i += 1
        elif command == "cd":
            path = instruction_parts[2]
            if path == "/":
                curr_tree = dir_tree
            elif path == "..":
                curr_tree = curr_tree.parent 
            else:
                curr_tree = curr_tree.get_child(path)
            i += 1
        else:
            raise ValueError(f"unsupported {command=}")
    return dir_tree

def calculate_dir_sizes(dir_tree: Tree, dir_sizes: Dict[str, int]) -> int: 
    if dir_tree.children == []:
        return dir_tree.value 
    else:
        dir_size = sum([calculate_dir_sizes(child, dir_sizes) for child in dir_tree.children])
        dir_sizes[dir_tree.full_name] = dir_size
        return dir_size


def main1(filepath: str) -> int:
  instructions = parse_file(filepath)
  dir_tree = create_tree(instructions)
  dir_sizes = {}
  calculate_dir_sizes(dir_tree, dir_sizes) 
  return sum([size for size in dir_sizes.values() if size < 100000])

assert main1(filepath) == 1297159


def smallest_dir_to_delete(dir_sizes: Dict[str, int]) -> int:
    total_disk_space = 70000000
    update_space_needed = 30000000
    root_disk = dir_sizes['root']
    current_space = total_disk_space - root_disk
    minimum_space_to_delete = update_space_needed - current_space

    return min([space for space in dir_sizes.values() if space > minimum_space_to_delete])

def main2(filepath: str) -> int:
  instructions = parse_file(filepath)
  dir_tree = create_tree(instructions)
  dir_sizes = {}
  calculate_dir_sizes(dir_tree, dir_sizes) 
  return smallest_dir_to_delete(dir_sizes)

assert main2(filepath) == 3866390

