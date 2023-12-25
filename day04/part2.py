import os


def solution(puzzle):
    scratchcards = puzzle.splitlines()
    ret = [1] * len(scratchcards)
    for idx, row in enumerate(scratchcards):
        card, number = row.split(":")
        left, right = number.split("|")
        left_set = set(map(int, left.split()))
        right_set = set(map(int, right.split()))
        winning = len(left_set & right_set)

        card_num = ret[idx]
        for j in range(1, winning + 1):
            if j + idx < len(ret):
                ret[j + idx] += card_num

    return sum(ret)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_part1.txt") as input_file:
        print(solution(input_file.read()))
