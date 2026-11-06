# Paquet de ressources — Orchestrer des agents d’IA avec Herdr

Version : 1.0.0

Ce paquet complémentaire public réunit les exemples exécutables, tests, consignes et instructions du livre. Il ne contient pas le texte payant.

## Installer et tester

Utilisez Python 3.12 depuis la racine du paquet :

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
```

Résultat de référence : 42 tests réussis avec Python 3.12 ; un avertissement de dépréciation Starlette/httpx peut apparaître. Consultez `examples/README.md` pour la correspondance avec les chapitres, le lancement du site et les exercices.

Ces ressources sont fournies pour accompagner le livre ; aucune licence open source générale n’est accordée.
