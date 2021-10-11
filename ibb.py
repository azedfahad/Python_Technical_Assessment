import pytest


def is_prime(num):
    """check if it is a prime number"""
    if num > 1:
        for j in range(2, int(num/2)+1):
            if (num % j) == 0:
                return False
        return True
    else:
        return False


def IbbleBibbleBobble(n):
    # check if the input n is positive
    if n < 0:
        print("Only positive number is allowed")
        return

    for i in range(n + 1):
        if i > 1 and is_prime(i):
            print("ibble")
        elif i % 2 == 0:
            print("bibble")
        else:
            print("bobble")


def test_method(capsys):
    IbbleBibbleBobble(23)
    captured = capsys.readouterr()

    assert captured.out == "bibble\nbobble\nibble\nibble\nbibble\nibble\nbibble\nibble" \
                           "\nbibble\nbobble\nbibble\nibble\nbibble\nibble\nbibble\nbobble" \
                           "\nbibble\nibble\nbibble\nibble\nbibble\nbobble\nbibble\nibble\n"
