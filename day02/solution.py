import os
from dataclasses import dataclass


@dataclass
class Bag:
    red: int = 0
    green: int = 0
    blue: int = 0

    def possible_game(self, record: str) -> int:
        """'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'"""
        info, subsets = record.split(":")
        for subset in subsets.split(";"):
            if not self.possible_subset(subset):
                return 0
        game_id = int(info.replace("Game ", ""))
        return game_id

    def possible_subset(self, subset: str) -> bool:
        for cube_desc in subset.split(","):
            num, color = cube_desc.strip().split()
            if not 0 <= int(num) <= getattr(self, color):
                return False
        return True


def compute_cube_conundrum(games_record: str) -> int:
    result = 0
    bag = Bag(red=12, green=13, blue=14)
    for record in games_record.split("\n"):
        game_id = bag.possible_game(record)
        result += game_id
    return result


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_input") as input_file:
        print(compute_cube_conundrum(input_file.read()))
