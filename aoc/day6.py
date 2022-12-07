from typing import Sequence, List, Set, Tuple 
from utils import parse_file

filepath = "../data/day6.txt"

def start_marker(buffer: str, distinct_count: int) -> int:
    window = [] 
 
    i = 0
    while i < len(buffer):
        next_letter = buffer[i]
        if next_letter in window:
            for _ in range(len(window)):
                window_letter = window.pop(0)
                if window_letter == next_letter:
                    window.append(next_letter)
                    break 
        else:
            if len(window) == distinct_count - 1:
                return i  + 1
            
            else:
                window.append(next_letter)

        i += 1
    return 0 

def main1(filepath: str) -> str:
  data = parse_file(filepath)  
  return start_marker(data[0], distinct_count=4) 

assert main1(filepath) == 1080

def main2(filepath: str) -> str:
  data = parse_file(filepath)  
  return start_marker(data[0], distinct_count=14) 

assert main2(filepath) == 3645
