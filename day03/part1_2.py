import os
import re


class Schematic:
    def __init__(self, puzzle: str):
        self._context = puzzle.splitlines()
        self.row_num = len(self._context)
        self.col_num = len(self._context[0])

    def sum_part_number(self):
        result = 0
        for idx, row in enumerate(self._context):
            for match in re.finditer(r"\d+", row):
                if self.is_part_number(idx, match.span()):
                    result += int(match.group())
        return result

    def is_part_number(self, idx, span) -> bool:
        top = idx - 1 if idx - 1 > 0 else 0
        bottom = idx + 2 if idx + 2 < self.row_num else self.row_num
        adjacent = ""
        for i in range(top, bottom):
            left = span[0] - 1 if span[0] - 1 > 0 else 0
            right = span[1] + 1 if span[1] + 1 < self.col_num else self.col_num
            adjacent += self._context[i][left:right]
        return bool(re.search(r"[^\d\.]", adjacent))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_part1.txt") as input_file:
        print(Schematic(input_file.read()).sum_part_number())
