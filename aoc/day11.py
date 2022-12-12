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
    """Deals with integer overflow: since we keep multiplying and adding numbers with no worry factor.
    But how do we keep the integers from overflowing? An appropriate guess here is to use the modspace. 


    How do we know that a mod space is a valid way to reduce numbers? It's definitely a good starting point, but how do we know we are on the right path. I think that the key insight here is that in the problem, we don't care about the actual worry levels of the items, but only whether or not `self.test` returns the correct monkey after computing `self.operation`. If the test was instead not just divisibility but "edge case: if worry_level == 10e10000 throw to monkey 7", then the mod space would not work (by itself, at least). 

    But what mod space do we choose? We need to pick one that keeps all of our operations having the same result. The operations we must maintain are: multiplication and addition (for the `self.operation`) and division (for `self.test`). 

    Noting that the operation for `self.test` is always a divisible check by the monkey's divisor, this leads us to the idea that we can use the divisor as the mod space, since for any X, X % mod % mod == X % mod. Note also that for multiplication and addition for `self.operation`, this holds true as well. Also note that this is not a full proof of why this works. I did not think of a full theorem  while doing this problem, but looked for a good proof to link afterwards, and I believe [this explanation](https://github.com/jake-gordon/aoc/blob/main/2022/D11/Explanation.md) is a formal proof that justifies this well.

    Is this the answer though? Unfortunately not, since each monkey has a different mod space. The solutiohn to this hurdle is to find the LCM of all of the divisors, but here I have opted to simply multiple all of the divisors since we don't really care about the LCM, but just the CMself.

    A fun note here is that I also tried using `math.lcm` to make sure my logic worked. And it did, but the more interesting observation is that `math.lcm(divisors)` is the same as the implementation here with multiplying all of the divisors. Why is this? Because all of the divisors are prime!"""

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
                    # read docstring for `get_divisor` to understand logic
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

assert main2(filepath) == 19573408701

