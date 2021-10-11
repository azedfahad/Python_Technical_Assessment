import pytest


def FactRec(n):
    # check if positive number is provided
    if n < 0:
        print("Negative number is not allowed")
        return
    elif n == 0:
        return 1
    else:
        if n == 1:
            return n
        else:
            return n*FactRec(n-1)  # recursive call


def test_method():
    assert FactRec(7) == 5040
    assert FactRec(2) == 2
