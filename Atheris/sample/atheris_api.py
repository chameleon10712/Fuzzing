"""
Sample using atheris to find bugs in a FastAPI application
"""
import atheris
from fastapi import FastAPI
from atheris_1 import get_sum_then_square_root
from atheris_str import not_kirby

with atheris.instrument_imports():
    import sys


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sum-then-sqrt/{x}/{y}")
def sum_sqrt(x: int, y: str):
    get_sum_then_square_root(x, y)


@app.get("/not-kirby/{s}")
def kirb(s: str):
    not_kirby(s)


@atheris.instrument_func
def api_fuzzy_testing(data):
    x = atheris.FuzzedDataProvider(data)
    y = atheris.FuzzedDataProvider(data)
    get_sum_then_square_root(x.ConsumeInt(4), y.ConsumeInt(4))


@atheris.instrument_func
def str_test(data):
    s = atheris.FuzzedDataProvider(data)
    not_kirby(s.ConsumeUnicodeNoSurrogates(sys.maxsize))


if __name__ == "__main__":
    # atheris.Setup(sys.argv, api_fuzzy_testing)
    # atheris.Fuzz()

    atheris.Setup(sys.argv, str_test)
    atheris.Fuzz()
