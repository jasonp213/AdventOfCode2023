import os


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


class State:
    def __init__(self):
        self.value_lookup = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
        }
        self.state_map = {k: list(v) for k, v in self.value_lookup.items()}

    def add(self, charc: str) -> int:
        if charc in "123456789":
            self.reset_all()
            return int(charc)

        result = 0
        for k, v in self.state_map.items():
            if charc == v[0]:
                v.pop(0)
                if len(v) == 0:
                    self.reset_k(k)
                    result = k
            else:
                self.reset_k(k)

        return result

    def reset_all(self):
        for key in self.state_map:
            self.reset_k(key)

    def reset_k(self, key):
        if len(self.value_lookup[key]) != len(self.state_map[key]):
            self.state_map[key] = list(self.value_lookup[key])


def calibration2(perline: str) -> int:
    state = State()
    digits = []
    for charc in perline:
        ret = state.add(charc)
        if ret:
            digits.append(ret)

    if len(digits) == 1:
        return 10 * digits[0] + digits[0]
    elif len(digits) >= 2:
        return 10 * digits[0] + digits[-1]
    else:
        raise RuntimeError(f"Unknown line: {perline}")


def trebuchet2(puzzle_input: str) -> int:
    """
    no pass lower than the right
    i have no idea of this
    """
    ret = 0
    for line in iter(puzzle_input.split("\n")):
        calibration_ = calibration2(line)
        # print(f"num: {calibration_} of '{line}'")
        ret += calibration_

    return ret


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/puzzle_input") as input_file:
        # print(trebuchet(input_file.read()))
        print(trebuchet2(input_file.read()))
