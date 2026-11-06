# Backend

Ne modifiez que `examples/task_manager/main.py`. Initialisez les tables dans le cycle de vie FastAPI ; refusez les champs inconnus et les conversions de types. La réussite POST renvoie 201, PATCH 200, DELETE 204, l’absence d’un enregistrement 404 et une entrée invalide 422. Les champs PATCH omis gardent leur valeur ; null explicite est refusé ; la description peut être effacée. Ne modifiez pas les fichiers appartenant à Database.
