
from typing import Sequence, List, Set, Tuple 

filepath = "data/day5.txt"
Stack = List[str]

class Instruction:
    def __init__(self, data: str):
        instruction = data.split(" ")
        self.count = int(instruction[1])
        self.from_box = int(instruction[3]) - 1  # why is this not zero indexed
        self.to_box = int(instruction[5]) - 1 
    
    def __repr__(self) -> str:
        return f"moved {self.count} from {self.from_box} to {self.to_box}"

def parse_file(filepath: str) -> Sequence[str]:
    with open(filepath) as file:
        data = file.read()
        return data.split("\n")[:-1] # ignore the newline at the end

def parse_stacks_and_instructions(data: Sequence[str]) -> Tuple[Sequence[Stack], Sequence[Instruction]]:
    rows = []
    instruction_start_index = 0
    stack_count = 0
    for i, row in enumerate(data):
        if row == "":
            instruction_start_index = i + 1 
            break
        elif row[1] == "1":
            stack_count = int(row[-2])
            pass 
        else:
            rows.append(row)
    rows = rows[::-1] # start from bottom of stacks 
    stacks = [[] for _ in range(stack_count)]
    for row in rows:
        for i in range(stack_count):
            letter = row[i * 4 + 1]
            if letter != " ":
                stacks[i].append(letter)
    
    instructions = []
    for row in data[instruction_start_index:]:
        instructions.append(Instruction(row))

    return stacks, instructions 

def top_stacks(stacks: List[Stack]) -> str:
    top = "" 
    for stack in stacks:
        top += stack[-1]
    return top
        
def cratemover_9000(stacks: List[Stack], instructions: Sequence[Instruction]) -> str:
    for instruction in instructions:
        for _ in range(instruction.count):
            box = stacks[instruction.from_box].pop()
            stacks[instruction.to_box].append(box)
    return top_stacks(stacks)

def main1(filepath: str) -> str:
  data = parse_file(filepath)  
  stacks, instructions = parse_stacks_and_instructions(data)
  return cratemover_9000(stacks, instructions) 

assert main1(filepath) == "ZWHVFWQWW"


def cratemover_9001(stacks: List[Stack], instructions: Sequence[Instruction]) -> str:
    for instruction in instructions:
        boxes = stacks[instruction.from_box][- instruction.count:]
        stacks[instruction.from_box] = stacks[instruction.from_box][: - instruction.count]
        stacks[instruction.to_box].extend(boxes)
    return top_stacks(stacks)
    

def main2(filepath: str) -> str:
  data = parse_file(filepath)  
  stacks, instructions = parse_stacks_and_instructions(data)
  return cratemover_9001(stacks, instructions) 

assert main2(filepath) == "HZFZCCWWV"
