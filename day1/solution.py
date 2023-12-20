def calibration(line: str):
    digits = []
    for charc in line:
        if charc in "0123456789":
            digits.append(charc)
    if len(digits) == 1:
        return int(digits[0] * 2)
    elif len(digits) >= 2:
        return int(digits[0] + digits[-1])
    else:
        raise RuntimeError(f"Unknown line: {line}")


def trebuchet(_input: str) -> int:
    ret = 0
    for line in iter(_input.split("\n")):
        ret += calibration(line)

    return ret


if __name__ == "__main__":
    import sys

    print(f"Result: {trebuchet(sys.argv[1])}")
