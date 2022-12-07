from typing import Sequence

def parse_file(filepath: str) -> Sequence[str]:
    with open(filepath) as file:
        data = file.read()
        return data.split("\n")[:-1] # ignore the newline at the end
