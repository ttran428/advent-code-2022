from typing import Sequence 

filepath = "data/day2.txt"

def parse_file(filepath: str) -> Sequence[str]:
    with open(filepath) as file:
        data = file.read()
        return data.split("\n")

def shape_points(player: str) -> int:
    if player == "X": # roc
        return 1
    elif player == "Y": # paper
        return 2 
    else: # scissors
        return 3

def round_result(player: str, opponent: str) -> str:
    # convert to the same units of a/b/c
    same_units = {"A": "X", "B": "Y", "C": "Z"}
    opponent = same_units[opponent]
    if player == opponent:
        return "TIE"
     
    result = (player, opponent)
    if result in (("X", "Z"), ("Y", "X"), ("Z", "Y")):
         return "WIN"
    else:
        return "LOSE"

def main1(filepath: str) -> int:
    rounds = parse_file(filepath)
    return strat_points(rounds)

def strat_points(rounds: Sequence[str]) -> int:
    total = 0
    for round in rounds:
        if round == "":
            break
        opponent, player = round.split(" ")
        result = round_result(player, opponent)
        if result == "WIN":
            total += 6
        elif result == "TIE":
            total += 3 
        total += shape_points(player)

    return total

assert main1(filepath) == 15632


def main2(filepath: str) -> int:
    rounds = parse_file(filepath)
    return strat2(rounds)

def strat2(rounds: Sequence[str]) -> int:
    total = 0
    # little  bit lazy here, but converts to what shape_points wants to return the correct shape score
    lose_map = {"A": "Z", "B": "X", "C": "Y"}
    win_map = {"A": "Y", "B": "Z", "C": "X"}
    tie_map = {"A": "X", "B": "Y", "C": "Z"}
    for round in rounds:
        if round == "":
            break
        opponent, result = round.split(" ")
        if result == "X": # lose
            total += shape_points(lose_map[opponent])
        elif result == "Y": # tie
            total += 3 
            total += shape_points(tie_map[opponent])
        else: # win
            total += 6
            total += shape_points(win_map[opponent])
    return total

assert main2(filepath) == 14416
