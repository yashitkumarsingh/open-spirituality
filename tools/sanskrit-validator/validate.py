#!/usr/bin/env python3
import os
import sys
import json
import re

COMMON_HEADERS = [
    r"## 1. Sanskrit",
    r"## 2. Word-by-word",
    r"## 3. Open translation",
    r"## 4. Literal reading",
    r"## 5. Philosophical meaning",
    r"## 7. Visual map",
    r"## 8. Key concepts",
    r"## 9. Cross-references",
    r"## 10. Scholarly notes",
    r"## 11. Practice cautions",
    r"## 12. Contribution status"
]

VBT_HEADERS = [
    r"# Sutra \d+ —",
    r"## 6. Practice instruction"
]

ASHTAVAKRA_HEADERS = [
    r"# Chapter \d+, Verse \d+ —",
    r"## 6. Contemplative inquiry"
]

def get_required_headers(text_id):
    if text_id == "ashtavakra-gita":
        return COMMON_HEADERS + ASHTAVAKRA_HEADERS
    else:
        # Default to VBT headers
        return COMMON_HEADERS + VBT_HEADERS

def validate_sutra_file(filepath, required_headers):
    errors = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check headers
    for header in required_headers:
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
    texts_dir = os.path.join(root_dir, "texts")

    failed = False

    if not os.path.exists(texts_dir):
        print(f"❌ Texts directory not found at: {texts_dir}")
        sys.exit(1)

    text_modules = [d for d in os.listdir(texts_dir) if os.path.isdir(os.path.join(texts_dir, d))]

    for module in sorted(text_modules):
        module_path = os.path.join(texts_dir, module)
        print(f"\n==========================================")
        print(f"Validating module: {module}")
        print(f"==========================================")

        # 1. Determine text ID
        text_id = module
        metadata_path = os.path.join(module_path, "metadata.yaml")
        if os.path.exists(metadata_path):
            with open(metadata_path, "r", encoding="utf-8") as f:
                metadata_content = f.read()
                # Simple extraction for id
                match = re.search(r"^id:\s*(\S+)", metadata_content, re.MULTILINE)
                if match:
                    text_id = match.group(1)

        required_headers = get_required_headers(text_id)

        # 2. Validate markdown files
        sutras_dir = os.path.join(module_path, "sutras")
        if os.path.exists(sutras_dir):
            print(f"Validating Sutra Markdown files in: {sutras_dir}")
            for file in sorted(os.listdir(sutras_dir)):
                if file.endswith(".md"):
                    path = os.path.join(sutras_dir, file)
                    errors = validate_sutra_file(path, required_headers)
                    if errors:
                        failed = True
                        print(f"❌ {file}:")
                        for err in errors:
                            print(f"   - {err}")
                    else:
                        print(f"✅ {file} is valid.")
        else:
            print(f"⚠️ No sutras directory found for module: {module}")

        # 3. Validate JSON data files
        data_dir = os.path.join(module_path, "data")
        if os.path.exists(data_dir):
            print(f"Validating JSON files in: {data_dir}")
            for file in sorted(os.listdir(data_dir)):
                if file.endswith(".json"):
                    path = os.path.join(data_dir, file)
                    errors = validate_json_file(path)
                    if errors:
                        failed = True
                        print(f"❌ {file}: {errors[0]}")
                    else:
                        print(f"✅ {file} parses successfully.")
        else:
            print(f"⚠️ No data directory found for module: {module}")

    if failed:
        print("\n❌ Content validation failed.")
        sys.exit(1)
    else:
        print("\n✅ All content is valid!")
        sys.exit(0)

if __name__ == "__main__":
    main()
