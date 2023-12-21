from collections.abc import Iterable

from day01.part1 import calibration

NUMBER_MAP = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def trebuchet2(lineiter: Iterable[str]):
    ret = 0
    for line in lineiter:
        for k, v in NUMBER_MAP.items():
            line = line.replace(k, v)
        ret += calibration(line)
    return ret
