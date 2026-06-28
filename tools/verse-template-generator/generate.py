#!/usr/bin/env python3
import os
import sys
import argparse

TEMPLATE_CONTENT = """# Sutra {number} — [Title/Focus]

## 1. Sanskrit

Devanāgarī:
[Enter Devanagari here]

IAST:
[Enter IAST here]

## 2. Word-by-word

| Sanskrit | Root / grammar | Literal meaning | Notes |
|---|---|---|---|
| | | | |

## 3. Open translation

[Original translation created for this repository]

## 4. Literal reading

[What the verse says directly]

## 5. Philosophical meaning

[How this relates to Bhairava, Śakti, awareness, madhya, śūnya, spanda, recognition, etc.]

## 6. Practice instruction

[A careful, non-exaggerated contemplative practice based on the verse]

## 7. Visual map

[Mermaid diagram or image link here]

## 8. Key concepts

- concept1
- concept2

## 9. Cross-references

- Related VBT verses
- Śiva Sūtras
- Spanda Kārikā
- Yoga Sūtras

## 10. Scholarly notes

Reference only. Do not copy modern copyrighted translations. Refer to bibliography.bib.

## 11. Practice cautions

[Practices should be gentle. Avoid strain, retention, hyperventilation, or medical claims.]

## 12. Contribution status

- Sanskrit checked: no
- Grammar checked: no
- Translation reviewed: no
- Visual reviewed: no
"""

def main():
    parser = argparse.ArgumentParser(description="Generate a premium markdown template for a VBT verse.")
    parser.add_argument("verse", type=int, help="Verse number to generate (e.g. 24)")
    parser.add_argument("--output-dir", default="texts/vijnana-bhairava-tantra/sutras", help="Output directory path")
    args = parser.parse_args()

    verse_str = f"{args.verse:03d}"
    filename = f"{verse_str}.md"
    filepath = os.path.join(args.output_dir, filename)

    if os.path.exists(filepath):
        print(f"Error: File {filepath} already exists. Will not overwrite.")
        sys.exit(1)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(TEMPLATE_CONTENT.format(number=args.verse))

    print(f"Created template at {filepath}")

if __name__ == "__main__":
    main()
