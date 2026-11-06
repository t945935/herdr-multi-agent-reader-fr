"""Chapitre 8 : valider les preuves associées aux affirmations et produire un rapport vérifiable."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    if not isinstance(data, dict) or not data.get("question"):
        raise ValueError("Une question de recherche est obligatoire")
    sources = data.get("sources", [])
    if not isinstance(sources, list) or not sources:
        raise ValueError("Des sources sont obligatoires")
    by_id = {}
    for source in sources:
        if not {"id", "url", "title", "accessed", "kind"} <= source.keys():
            raise ValueError("La fiche source est incomplète")
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("L’URL de la source doit utiliser HTTP ou HTTPS")
        if source["id"] in by_id:
            raise ValueError("L’identifiant de source est dupliqué")
        by_id[source["id"]] = source
    claims = data.get("claims", [])
    if not claims:
        raise ValueError("Des affirmations sont obligatoires")
    for claim in claims:
        if not claim.get("text") or claim.get("status") not in {"supported", "uncertain", "conflict"}:
            raise ValueError("L’affirmation est invalide")
        evidence = claim.get("evidence", [])
        if claim["status"] == "supported" and not evidence:
            raise ValueError("Une affirmation étayée doit comporter des preuves")
        for item in evidence:
            if item.get("source") not in by_id or not item.get("quote"):
                raise ValueError("La preuve doit citer une source connue et inclure une citation")
    return by_id


def render(data):
    sources = validate(data)
    lines = ["# " + data["question"], "", "## Constats et preuves", ""]
    for claim in data["claims"]:
        lines.extend([f"### {claim['text']}", "", "État: " + claim["status"], ""])
        for evidence in claim.get("evidence", []):
            source = sources[evidence["source"]]
            lines.extend([f"> {evidence['quote']}", "", f"Source : [{source['title']}]({source['url']})", ""])
    lines.extend(["## Sources", ""])
    for source in sources.values():
        lines.append(f"- {source['id']}：[{source['title']}]({source['url']})；{source['kind']}；consulté le {source['accessed']}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = render(json.loads(args.input.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report)
    print(args.output)
