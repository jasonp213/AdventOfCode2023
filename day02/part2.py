import os

from day02.part1 import Bag


def compute_cube_conundrum2(games_record: str) -> int:
    result = 0

    for record in games_record.split("\n"):
        bag = Bag()
        bag.subset_fewest(record)
        result += bag.power()
    return result


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_input") as input_file:
        print(compute_cube_conundrum2(input_file.read()))
