#!/usr/bin/env python

import importlib
import sys


def main():
    print("Attempting to load module", sys.argv[1])
    try:
        day_module = importlib.import_module(sys.argv[1])
    except ModuleNotFoundError as e:
        print(e)
        return
    with open(sys.argv[2]) as input_file:
        text_blob = input_file.read()
        print("Part 1 Solution:", day_module.part1_solve(text_blob))
        print("Part 2 Solution:", day_module.part2_solve(text_blob))


if __name__ == "__main__":
    main()
