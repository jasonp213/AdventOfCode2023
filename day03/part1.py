import os
import re
from collections import namedtuple

CloseInterval = namedtuple("CloseInterval", "left right")
CloseInterval.__contains__ = lambda self, _key: self.left <= _key <= self.right


def sum_adjacent(puzzle: str) -> int:
    pre_symbol = []  # the pre row symbol place like '...*......' -> [3]
    pre_number_map = {}  # pre row number adjacent range except added  '467..114..' -> {(-1, 3): 467, (4, 8): 114}
    result = 0
    for _, line in enumerate(puzzle.splitlines()):
        cur_symbol = []
        for symbol in re.finditer(r"[^a-zA-Z0-9\.]", line):
            cur_symbol.append(symbol.span()[0])

        cur_number_map = {}
        for number in re.finditer(r"\d+", line):
            ext_interval = CloseInterval(number.span()[0] - 1, number.span()[1])
            cur_number_map[ext_interval] = int(number.group())

        adjacent_sum = sum_of_interval_map(cur_number_map, list(set(pre_symbol + cur_symbol))) + sum_of_interval_map(
            pre_number_map, cur_symbol
        )
        result += adjacent_sum

        pre_number_map = cur_number_map
        pre_symbol = cur_symbol
        # print(f"{idx}: '{line}', ret: {result}, adj: {adjacent_sum}")

    return result


def sum_of_interval_map(number_map: dict[CloseInterval, int], symbol_place: list[int]) -> int:
    result = 0
    for symbol in symbol_place:
        for interval in list(number_map.keys()):
            if symbol in interval:
                result += number_map[interval]
    return result


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_part1.txt") as input_file:
        print(sum_adjacent(input_file.read()))
