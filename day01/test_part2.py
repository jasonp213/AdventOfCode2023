from day01.part2 import trebuchet2


def test_part2():
    puzzle_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert 281 == trebuchet2(puzzle_input.splitlines())
