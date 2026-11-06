"""Chapter 1: a deliberately small contract for a development/review exercise."""

from math import isfinite


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Expected a number, excluding bool")
    if not isfinite(value):
        raise ValueError("Expected a finite number")
    return value


def add(a, b):
    return _number(a) + _number(b)


def subtract(a, b):
    return _number(a) - _number(b)


def multiply(a, b):
    return _number(a) * _number(b)


def divide(a, b):
    a, b = _number(a), _number(b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
