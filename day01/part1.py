import os
from collections.abc import Iterable


def calibration(line: str):
    digits = ""
    for charc in line:
        if charc.isdigit():
            digits += charc
    return int(digits[0] + digits[-1])


def trebuchet(lineiter: Iterable[str]):
    ret = 0
    for line in lineiter:
        ret += calibration(line)
    return ret


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/part1.txt") as input_file:
        print(trebuchet(input_file))
