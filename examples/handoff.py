"""Chapitre 6 : valider une trace de transfert explicite, pas une affirmation rédigée par un agent."""

import argparse
import hashlib
import json
from pathlib import Path


def validate(record, root):
    required = {"task_id", "from", "to", "completed", "next", "artifacts"}
    if not isinstance(record, dict) or not required <= record.keys():
        raise ValueError("Des champs obligatoires du transfert manquent")
    if any(not isinstance(record[key], str) or not record[key].strip()
           for key in ["task_id", "from", "to", "completed", "next"]):
        raise ValueError("Les champs textuels du transfert ne peuvent pas être vides")
    if not isinstance(record["artifacts"], list) or not record["artifacts"]:
        raise ValueError("Le transfert doit répertorier des artefacts")
    root = Path(root).resolve()
    for artifact in record["artifacts"]:
        if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
            raise ValueError("Chaque artefact doit avoir un chemin et une empreinte sha256")
        path = (root / artifact["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("Le chemin de l’artefact doit désigner un fichier du projet")
        if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("L’empreinte de l’artefact ne correspond pas")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(json.loads(args.record.read_text()), args.root)
    print("transfert accepté")
