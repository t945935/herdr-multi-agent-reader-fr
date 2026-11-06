"""Chapitre 1 : contrat volontairement restreint pour un exercice de développement et de revue."""

from math import isfinite


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Une valeur numérique est attendue ; bool est exclu")
    if not isfinite(value):
        raise ValueError("Une valeur finie est attendue")
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
        raise ZeroDivisionError("La division par zéro est impossible")
    return a / b
