"""Chapter 8: validate claim-to-source evidence and produce an auditable report."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    if not isinstance(data, dict) or not data.get("question"):
        raise ValueError("A research question is required")
    sources = data.get("sources", [])
    if not isinstance(sources, list) or not sources:
        raise ValueError("Sources are required")
    by_id = {}
    for source in sources:
        if not {"id", "url", "title", "accessed", "kind"} <= source.keys():
            raise ValueError("Incomplete source")
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Source URL must be HTTP(S)")
        if source["id"] in by_id:
            raise ValueError("Duplicate source id")
        by_id[source["id"]] = source
    claims = data.get("claims", [])
    if not claims:
        raise ValueError("Claims are required")
    for claim in claims:
        if not claim.get("text") or claim.get("status") not in {"supported", "uncertain", "conflict"}:
            raise ValueError("Invalid claim")
        evidence = claim.get("evidence", [])
        if claim["status"] == "supported" and not evidence:
            raise ValueError("Supported claims require evidence")
        for item in evidence:
            if item.get("source") not in by_id or not item.get("quote"):
                raise ValueError("Evidence requires a known source and a quote")
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
