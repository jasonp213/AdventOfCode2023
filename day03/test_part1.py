import textwrap

from day03.part1 import sum_adjacent


def test_sum_of_adjacent():
    _puzzle = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598.."""
    puzzle = textwrap.dedent(_puzzle)
    assert sum_adjacent(puzzle) == 4361
