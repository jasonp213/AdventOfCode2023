from .solution import trebuchet


def test_trebuchet():
    _input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    output = trebuchet(_input)
    assert output == 142
