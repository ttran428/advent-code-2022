from typing import Sequence

def parse_file(filepath: str) -> Sequence[str]:
    with open(filepath) as file:
        data = file.read()
        return data.split("\n")[:-1] # ignore the newline at the end

def parse_string(data: str) -> Sequence[str]:
    return data.split("\n")

def parse_by_split_lines(filepath: str, string: bool = False) -> Sequence[Sequence[str]]:
    if string:
        data = parse_string(filepath)
    else:
        data = parse_file(filepath)
    sections = []
    section = []
    for row in data:
        if row != "": 
            section.append(row)
        else:
            sections.append(section)
            section = []
    if section:
        sections.append(section)
    return sections
