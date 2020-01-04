#!/usr/bin/python3.7

# -*- coding: utf-8 -*-

import math


def gcd(m, n):
    if type(m) is int is type(n):
        if (n or m) < 0:
            return -math.gcd(m, n)
        return math.gcd(m, n)
    # print(math.gcd(m, n))
    return _gcd(m, n)


def _gcd(m, n):
    while n:
        m, n = n, m % n
    return m


class Fraction:
    def __init__(self, a, b):
        # method of constructor
        self.numerator = a
        self.denominator = b

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __mul__(self, other_mul):
        return Fraction(self.numerator * other_mul.numerator, self.denominator * other_mul.denominator)

    def __truediv__(self, other_div):
        return Fraction(self.numerator * other_div.denominator, self.denominator * other_div.numerator)

    def __floordiv__(self, other_floordiv):
        print(other_floordiv.numerator, other_floordiv.denominator)
        return (self.numerator * other_floordiv.denominator) // (self.denominator * other_floordiv.numerator)

    def __add__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + self.denominator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator

        common_divisor = gcd(new_numerator, new_denominator)

        return Fraction(new_numerator // common_divisor, new_denominator // common_divisor)

    def __eq__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator

        return first_num == second_num


if __name__ == '__main__':
    fraction1 = Fraction(4, 5)
    print(fraction1 + Fraction(1, 8))
    print(Fraction(40, 70))
    print(Fraction(1, 6) + Fraction(1, 3))
    print(Fraction(1, 2) + Fraction(3, 4) + Fraction(1, 9) * Fraction(3, 5))
    print(Fraction(5, 7) / 10)