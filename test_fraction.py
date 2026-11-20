from fraction import Fraction


def test_equal():
    a = Fraction(1, 2)
    b = Fraction(2, 4)
    assert a == b


def test_not_equal():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    assert a != b


def test_less_than():
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    assert a < b


def test_less_equal():
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    assert a <= b


def test_greater_than():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    assert a > b


def test_greater_equal():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    assert a >= b


def test_addition():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    result = a + b
    assert result.numerator == 5
    assert result.denominator == 6


def test_subtraction():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    result = a - b
    assert result.numerator == 1
    assert result.denominator == 6


def test_string():
    a = Fraction(1, 2)
    assert str(a) == "1/2"


def test_invalid_denominator():
    try:
        Fraction(1, 0)
        assert False
    except ValueError:
        assert True