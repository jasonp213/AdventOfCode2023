import os


def solution(puzzle):
    ret = 0
    for row in puzzle.splitlines():
        card, number = row.split(":")
        left, right = number.split("|")
        left_set = set(map(int, left.split()))
        right_set = set(map(int, right.split()))
        winning = len(left_set & right_set)
        point = 0 if winning == 0 else 2 ** (winning - 1)
        ret += point
    return ret


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_part1.txt") as input_file:
        print(solution(input_file.read()))
