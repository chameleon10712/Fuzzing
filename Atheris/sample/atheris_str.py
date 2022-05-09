"""Sample using atheris with string inputs (single and multiple inputs)"""

import atheris
import sys


@atheris.instrument_func
def not_kirby(s: str):
    """Returns True as long as the given text is not 'kirby'"""
    if len(s) < 5:
        return True

    if s[0] == "k":
        if s[1] == "i":
            if s[2] == "R":
                if s[3] == "b":
                    if s[4] == "Y":
                        raise ValueError(f"{s} is not accepted by this function.")

    return True


@atheris.instrument_func
def not_kirby_okay(s: str, other: str):
    """Returns True as long as the given text is not 'kirby'"""
    if len(s) < 5:
        return True

    if not other or len(other) < 4:
        return True

    if s[0] == "k" and other[0] == "o":
        if s[1] == "i" and other[1] == "k":
            if s[2] == "R" and other[2] == "a":
                if s[3] == "b" and other[3] == "y":
                    if s[4] == "Y":
                        error = (
                            f"{s} is not accepted by this function. Other is: {other}"
                        )
                        print(error)
                        raise ValueError(error)

    return True


@atheris.instrument_func
def test_one_input(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    random_str = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    not_kirby(random_str)


@atheris.instrument_func
def test_two_inputs(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)

    half = int(len(input_bytes) / 2)
    random_str = fdp.ConsumeUnicodeNoSurrogates(half)  # turn 1st half of bytes to str
    other = fdp.ConsumeUnicodeNoSurrogates(half)  # turn 2nd half of bytes to str

    # skip empty inputs
    if not random_str or not other:
        return

    not_kirby_okay(random_str, other)


if __name__ == "__main__":
    # atheris.Setup(sys.argv, test_one_input)
    atheris.Setup(sys.argv, test_two_inputs)
    atheris.Fuzz()
