# Developer : contrat de notation

Lisez d’abord les cas de notation dans `examples/grades.py` et `tests/test_contracts.py`. Modifiez uniquement `examples/grades.py` ; ne changez ni les tests existants, ni le site, et ne lancez aucun autre agent.

Contrat : exactement trois matières — Français, Histoire et Mathématiques. Les notes sont des `int`/`float` finis ; refuser bool, chaînes, matières absentes ou supplémentaires et valeurs hors de 0 à 100. Une moyenne de 60 est suffisante. Une liste vide renvoie une liste vide. Classer selon les totaux non arrondis avec classement par compétition, conserver l’ordre d’entrée en cas d’égalité et ne pas modifier l’entrée.

Conserver les interfaces `calculate_total`, `calculate_average`, `get_grade` et `rank_students`. Vérifier le contrat et ne corriger que si nécessaire. S’il est déjà conforme, conserver l’implémentation et rapporter les contrôles au lieu de réécrire pour créer une différence.

Exécuter `.venv/bin/python -m pytest -q tests/test_contracts.py -k 'ranking or scores'`. Écrire la commande réelle, le code de retour, les fichiers modifiés et les points non résolus dans `reports/grade-developer.md`. Utiliser le `task_id` et le `completion_path` ajoutés par le Manager pour la trace d’achèvement.
