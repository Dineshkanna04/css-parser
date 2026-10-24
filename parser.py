import json
import sys
from pathlib import Path

import tinycss2


def parse_css(file_path):
    """Parse a CSS file and extract structured information."""

    path = Path(file_path)
    css_text = path.read_text(encoding="utf-8")

    rules = tinycss2.parse_stylesheet(
        css_text,
        skip_comments=True,
        skip_whitespace=True
    )

    parsed_rules = []

    for rule in rules:
        if rule.type == "error":
            print(f"CSS parsing error: {rule.message}")
            continue

        if rule.type != "qualified-rule":
            continue

        selector = tinycss2.serialize(rule.prelude).strip()

        declarations = tinycss2.parse_declaration_list(
            rule.content,
            skip_comments=True,
            skip_whitespace=True
        )

        properties = {}

        for declaration in declarations:
            if declaration.type != "declaration":
                continue

            value = tinycss2.serialize(
                declaration.value
            ).strip()

            if declaration.important:
                value += " !important"

            properties[declaration.name] = value

        parsed_rules.append({
            "selector": selector,
            "declarations": properties
        })

    return parsed_rules


def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "style.css"

    try:
        result = parse_css(file_path)
        print(json.dumps(result, indent=2))

    except FileNotFoundError:
        print(f"Error: CSS file not found: {file_path}")
        sys.exit(1)

    except OSError as error:
        print(f"Error reading CSS file: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()