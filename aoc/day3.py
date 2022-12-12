from typing import Sequence, List, Set 

filepath = "data/day3.txt"

def parse_file(filepath: str) -> Sequence[str]:
    with open(filepath) as file:
        data = file.read()
        return data.split("\n")[:-1] # ignore the newline at the end

def get_priority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38

def create_letter_set(string: str) -> Set[str]:
        return set([letter for letter in string])

def total_priorities(rucksacks: Sequence[str]) -> int:
    duplicates = []
    for rucksack in rucksacks:
        middle_index = len(rucksack) // 2
        first_compartment = rucksack[: middle_index]
        second_compartment = rucksack[middle_index:]
        
        # store in a set: check for inclusion if any elem from second compartment exists in the first_compartment
        items = create_letter_set(first_compartment) 
        for letter in second_compartment:
            if letter in items:
               duplicates.append(letter) 
               break
    priority = 0
    for duplicate in duplicates:
        priority += get_priority(duplicate)
    return priority
        
def main1(filepath: str) -> int:
  rucksacks = parse_file(filepath)  
  return total_priorities(rucksacks)

assert main1(filepath) == 8018

### part 2

def group_total_priorities(rucksacks: List[str]) -> int:
    groups = []
    common_letters = []
    # split into groups of 3
    while rucksacks:
        groups.append([rucksacks.pop(), rucksacks.pop(), rucksacks.pop()])
    
    for group in groups:
        elf1, elf2, elf3 = group 
        # using a counter dict only works if we turn the rucksacks into sets first to avoid duplicates
        count_dict = {} 
        # first rucksack will all be the first item
        for letter in create_letter_set(elf1):
            count_dict[letter] = 1

        for letter in create_letter_set(elf2):
            if letter in count_dict:
                count_dict[letter] += 1

        for letter in create_letter_set(elf3):
            if count_dict.get(letter, -1) == 2:
                common_letters.append(letter)
                break

    priority = 0
    for letter in common_letters:
        priority += get_priority(letter)
    return priority

def main2(filepath: str) -> int:
  rucksacks = parse_file(filepath)  
  return group_total_priorities(rucksacks)


assert main2(filepath) == 2518 

