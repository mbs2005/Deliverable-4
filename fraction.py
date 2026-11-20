class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Both numbers must be integers")

        if denominator <= 0:
            raise ValueError("Denominator must be a positive number")

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
