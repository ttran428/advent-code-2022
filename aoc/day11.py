from typing import Mapping, Sequence, List, Set, Tuple, Dict, Iterable
from time import sleep
from utils import parse_file, parse_string, parse_by_split_lines

filepath = "data/day11.txt"


class Monkey:
    def __init__(self, monkey_data: Sequence[str]) -> None:
        self.id = monkey_data[0].split(" ")[1][: -1]

        item_data = monkey_data[1].split(" ")[4:]
        self.items = [int(item.replace(",", "")) for item in item_data] 


        self.test_divisor = int(monkey_data[3].split(" ")[-1])
        true_case = int(monkey_data[4].split(" ")[-1])
        false_case = int(monkey_data[5].split(" ")[-1])
        self.test = lambda x: true_case if x % self.test_divisor == 0 else false_case

        operation_data = monkey_data[2].split(" ")
        operation = operation_data[-2]
        if operation_data[-1] == "old":
            self.operation = lambda x: x * x
        else:
            value = int(operation_data[-1])
            if operation == "*":
                self.operation = lambda x: x * value 
            elif operation == "+":
                self.operation = lambda x: x + value


def parse_monkeys(data: Sequence[Sequence[str]]) -> Sequence[Monkey]:
    monkeys = []
    for monkey_data in data:
        monkeys.append(Monkey(monkey_data))
    return monkeys


def get_divisor(monkeys: Sequence[Monkey]) -> int:
    divisor = 1
    for monkey in monkeys:
        divisor *= monkey.test_divisor
    return divisor


def get_monkey_activity(monkeys: Sequence[Monkey], decrease_worry_levels: bool, rounds: int) -> Mapping[int, int]:
    monkey_activity = {i: 0 for i in range(len(monkeys))}    
    divisor = get_divisor(monkeys)
    for _ in range(rounds): 
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                if decrease_worry_levels:
                    item = item // 3
                else:
                    if monkey.test(item) != monkey.test(item % divisor):
                        breakpoint()
                    item = item % divisor 
                
                monkey_to_throw_to = monkey.test(item)
                monkeys[monkey_to_throw_to].items.append(item)

                monkey_activity[i] += 1
    return monkey_activity


def get_monkey_business(monkey_activity: Dict[int, int]) -> int:
    monkey_levels = sorted(monkey_activity.values(), reverse=True)
    return monkey_levels[0] * monkey_levels[1]




def main1(filepath: str) -> int:
    data = parse_by_split_lines(filepath)
    monkeys = parse_monkeys(data)
    monkey_activity = get_monkey_activity(monkeys, decrease_worry_levels=True, rounds=20)
    return get_monkey_business(monkey_activity)

assert main1(filepath) == 69918 


def main2(filepath: str) -> int:
    data = parse_by_split_lines(filepath)
    monkeys = parse_monkeys(data)
    monkey_activity = get_monkey_activity(monkeys, decrease_worry_levels=False, rounds=10000)

    return get_monkey_business(monkey_activity)

print(main2(filepath))
# assert main2(filepath) == 69918 


example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

data = parse_by_split_lines(example, string=True)
monkeys = parse_monkeys(data)
monkey_activity = get_monkey_activity(monkeys, decrease_worry_levels=False, rounds=20)
print(monkey_activity)
monkey_activity = get_monkey_activity(monkeys, decrease_worry_levels=False, rounds=1000)
print(monkey_activity)
