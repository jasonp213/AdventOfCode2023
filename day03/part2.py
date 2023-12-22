import os
import re
from collections import defaultdict


class Schematic:
    def __init__(self, puzzle: str):
        self.asterisk_gears = defaultdict(list)
        self._context = puzzle.splitlines()
        self.row_num = len(self._context)
        self.col_num = len(self._context[0])

    def sum_part_number(self):
        for idx, row in enumerate(self._context):
            for match in re.finditer(r"\d+", row):
                self.set_if_asterisk(idx, match.span(), int(match.group()))
        return self.compute_asterisk()

    def set_if_asterisk(self, idx, span, value):
        top = idx - 1 if idx - 1 > 0 else 0
        bottom = idx + 2 if idx + 2 < self.row_num else self.row_num
        for i in range(top, bottom):
            left = span[0] - 1 if span[0] - 1 > 0 else 0
            right = span[1] + 1 if span[1] + 1 < self.col_num else self.col_num
            part_string = self._context[i][left:right]
            for aster in re.finditer(r"\*", part_string):
                self.asterisk_gears[(i, left + aster.start())].append(value)

    def compute_asterisk(self):
        return sum(gear[0] * gear[1] for gear in self.asterisk_gears.values() if len(gear) == 2)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_part2.txt") as input_file:
        print(Schematic(input_file.read()).sum_part_number())
