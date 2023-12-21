from .part1 import trebuchet


def test_part1():
    _input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    output = trebuchet(_input.splitlines())
    assert output == 142
