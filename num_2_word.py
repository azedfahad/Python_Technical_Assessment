import pytest


def NumToWords(num):
    """convert num to word"""
    num = int(num)  # cast input number to integer
    assert num <= 999999  # assert that the maximum input number is less than 999999

    # create list of words
    one_to_nineteen = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                       'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                       'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    pivots = {100: 'Hundred', 1000: 'Thousand'}

    # just output the word if the input number is less than 20
    if num < 20:
        return one_to_nineteen[num]

    # concatenate words if the input number is less than 100
    if num < 100:
        # num // 10 => get the number in tens
        # num % 10 => get the smallest digit
        return tens[(num // 10) - 2] + ('' if num % 10 == 0 else ' ' + one_to_nineteen[num % 10])

    # find the appropriate pivot - 'Thousand' in 603,550
    pivot = max([key for key in pivots.keys() if key <= num])

    # punctuation to use
    punct = " "
    if pivot == 1000:
        punct = ", "
    elif pivot == 100:
        punct = " and "

    # recursive call
    return NumToWords((num // pivot)) + ' ' + pivots[pivot] + (
        '' if num % pivot == 0 else punct + NumToWords(num % pivot))


def test_method():
    assert NumToWords(44554) == "Forty Four Thousand, Five Hundred and Fifty Four"
    assert NumToWords(123.5543) == "One Hundred and Twenty Three"
    assert NumToWords(117.34) == "One Hundred and Seventeen"
