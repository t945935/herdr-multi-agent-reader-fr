# Utiliser les exemples

Exécutez toutes les commandes depuis la racine extraite du paquet. Utilisez Python 3.12 et installez les dépendances avec `pip install -r requirements.txt`.

| Chapitre | Point d’entrée | Contrôle principal |
| --- | --- | --- |
| 1 | `calculator.py` | Opérations, division par zéro et types |
| 2 | `grades.py` | Limites, matières manquantes et égalités |
| 3 | `../scripts/probe_herdr.py --live` | Créer, lire, attendre et nettoyer un volet |
| 4 | `../scripts/team.py` | Attributions, identifiants de tâche et acceptation |
| 5 | `prompts/reviewer-a.md`, `reviewer-b.md` | Revues indépendantes et décision du Manager |
| 6 | `handoff.py` | Présence, périmètre et SHA-256 des fichiers |
| 7 | `task_manager/` | CRUD, validation, pages et persistance |
| 8 | `research.py` | Affirmations, sources, citations et incertitudes |
| 9 | `pipeline.py` | Codes de retour, délais et arrêt sur échec |
| 10 | `queue.py` | Déduplication, baux, reprise et concurrence |

Pour lancer le site :

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

Les exemples et tests n’exigent pas de compte de modèle. L’attribution réelle à des agents nécessite Herdr et une CLI configurée.
