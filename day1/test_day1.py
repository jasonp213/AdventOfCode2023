from .solution import trebuchet, trebuchet2


def test_trebuchet():
    _input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    output = trebuchet(_input)
    assert output == 142


def test_part2():
    puzzle_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert 281 == trebuchet2(puzzle_input)
