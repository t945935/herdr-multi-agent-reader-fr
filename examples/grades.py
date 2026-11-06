"""Shared chapter 2/4/5/6 contract; competition ranking uses unrounded totals."""

from collections.abc import Mapping
from math import isfinite

SUBJECTS = frozenset({"Français", "Histoire", "Mathématiques"})


def validate_scores(scores):
    if not isinstance(scores, Mapping) or set(scores) != SUBJECTS:
        raise ValueError("les notes doivent contenir exactement Français, Histoire et Mathématiques")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Les notes doivent être numériques, et non de type bool")
        if not isfinite(value) or not 0 <= value <= 100:
            raise ValueError("Les notes doivent être finies et comprises entre 0 et 100")
    return scores


def calculate_total(scores):
    return sum(validate_scores(scores).values())


def calculate_average(scores):
    return calculate_total(scores) / 3


def get_grade(average):
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise ValueError("La moyenne doit être numérique")
    if not isfinite(average) or not 0 <= average <= 100:
        raise ValueError("La moyenne doit être comprise entre 0 et 100")
    return "Réussi" if average >= 60 else "Échec"


def rank_students(students):
    if not isinstance(students, list):
        raise ValueError("La liste d’élèves est invalide")
    rows = []
    for student in students:
        if not isinstance(student, Mapping):
            raise ValueError("Chaque élève doit être un objet")
        name = student.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Le nom de l’élève est obligatoire")
        total = calculate_total(student.get("scores"))
        average = total / 3
        rows.append({"name": name.strip(), "scores": dict(student["scores"]),
                     "total": total, "average": average, "grade": get_grade(average)})
    rows.sort(key=lambda row: row["total"], reverse=True)
    previous = None
    rank = 0
    for index, row in enumerate(rows, 1):
        if previous is None or row["total"] != previous:
            rank = index
        previous = row["total"]
        row["rank"] = rank
    return rows
