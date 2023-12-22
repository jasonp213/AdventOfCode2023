import textwrap

from day03.part2 import Schematic


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
    puzzle = textwrap.dedent(_puzzle).strip()
    assert Schematic(puzzle).sum_part_number() == 467835
