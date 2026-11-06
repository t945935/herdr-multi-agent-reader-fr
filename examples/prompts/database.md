# Database

Ne modifiez que `examples/task_manager/db.py`. Fournissez `init_db`, `get_tasks`, `get_task`, `create_task`, `update_task` et `delete_task`. Les tests peuvent remplacer `DB_PATH` ; fermez toujours les connexions, utilisez des transactions en écriture et paramétrez les valeurs SQL. Ne créez des noms de colonnes dynamiques qu’à partir d’une liste autorisée fixe. Renvoyez `None`/`False` si un enregistrement manque ; ne masquez pas les exceptions de base de données en les remplaçant par une liste vide.
