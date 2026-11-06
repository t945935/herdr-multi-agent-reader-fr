# QA : système de notation

Lisez l’interface de `examples/grades.py` et les cas de notation existants de `tests/test_contracts.py`. Vérifiez indépendamment le contrat. Ne modifiez pas le code, ne supprimez pas de tests existants, ne lisez pas l’autoévaluation du Developer et ne démarrez pas d’autres agents.

Modifiez uniquement `tests/test_grades_review.py` ; rédigez le rapport dans `reports/grade-qa.md`. Vérifiez l’ensemble des trois matières, limites 0/100/60, bool/NaN/chaîne, données vides, noms, classement d’égalité 1/1/3, précision non arrondie et immutabilité de l’entrée.

Utilisez pytest. Si les tests existants couvrent déjà suffisamment un cas, expliquez votre critère et n’ajoutez que des cas manquants utiles ; ne dupliquez pas un test identique. Ne testez pas FastAPI, SQLite ni le CRUD du site : cette tâche porte sur le système de notation.

Exécutez les tests et conservez la commande réelle, le code de retour, les constats et les éléments non exécutés. Utilisez le `task_id` et le `completion_path` ajoutés par le Manager dans la trace ; listez les rapports et tests créés sous `artifacts`.
