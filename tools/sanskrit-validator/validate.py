#!/usr/bin/env python3
import os
import sys
import json
import re

REQUIRED_HEADERS = [
    r"# Sutra \d+ —",
    r"## 1. Sanskrit",
    r"## 2. Word-by-word",
    r"## 3. Open translation",
    r"## 4. Literal reading",
    r"## 5. Philosophical meaning",
    r"## 6. Practice instruction",
    r"## 7. Visual map",
    r"## 8. Key concepts",
    r"## 9. Cross-references",
    r"## 10. Scholarly notes",
    r"## 11. Practice cautions",
    r"## 12. Contribution status"
]

def validate_sutra_file(filepath):
    errors = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check headers
    for header in REQUIRED_HEADERS:
        if not re.search(header, content, re.IGNORECASE):
            errors.append(f"Missing or malformed header: '{header}'")

    # Check word-by-word table
    if "| Sanskrit | Root / grammar |" not in content:
        errors.append("Missing Word-by-word table structure.")

    # Check that placeholders are not left as-is
    placeholders = [
        "[Enter Devanagari here]",
        "[Enter IAST here]",
        "[Original translation created for this repository]"
    ]
    for p in placeholders:
        if p in content:
            errors.append(f"Unfilled placeholder found: '{p}'")

    return errors

def validate_json_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            json.load(f)
        return []
    except Exception as e:
        return [f"Invalid JSON file: {e}"]

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sutras_dir = os.path.join(root_dir, "texts", "vijnana-bhairava-tantra", "sutras")
    data_dir = os.path.join(root_dir, "texts", "vijnana-bhairava-tantra", "data")

    failed = False

    # 1. Validate markdown files
    if os.path.exists(sutras_dir):
        print(f"Validating Sutra Markdown files in: {sutras_dir}")
        for file in sorted(os.listdir(sutras_dir)):
            if file.endswith(".md"):
                path = os.path.join(sutras_dir, file)
                errors = validate_sutra_file(path)
                if errors:
                    failed = True
                    print(f"❌ {file}:")
                    for err in errors:
                        print(f"   - {err}")
                else:
                    print(f"✅ {file} is valid.")
    else:
        print(f"Sutras directory not found at: {sutras_dir}")
        failed = True

    # 2. Validate JSON data files
    if os.path.exists(data_dir):
        print(f"\nValidating JSON files in: {data_dir}")
        for file in sorted(os.listdir(data_dir)):
            if file.endswith(".json"):
                path = os.path.join(data_dir, file)
                errors = validate_json_file(path)
                if errors:
                    failed = True
                    print(f"❌ {file}: {errors[0]}")
                else:
                    print(f"✅ {file} parses successfully.")

    if failed:
        print("\n❌ Content validation failed.")
        sys.exit(1)
    else:
        print("\n✅ All content is valid!")
        sys.exit(0)

if __name__ == "__main__":
    main()
