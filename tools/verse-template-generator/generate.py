#!/usr/bin/env python3
import os
import sys
import argparse

VBT_TEMPLATE = """# Sutra {number} — [Title/Focus]

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

ASHTAVAKRA_TEMPLATE = """# Chapter {chapter}, Verse {number} — [Title/Focus]

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

[How this relates to self-inquiry, witness consciousness (sākṣī), māyā, liberation (mukti), Vivartavāda, etc.]

## 6. Contemplative inquiry

[Practical steps for self-inquiry, meditation, and witnessing]

## 7. Visual map

[Mermaid diagram or image link here]

## 8. Key concepts

- concept1
- concept2

## 9. Cross-references

- Upanishads
- Bhagavad Gita
- Avadhuta Gita
- Ribhu Gita

## 10. Scholarly notes

Reference only. Do not copy modern copyrighted translations. Refer to bibliography.bib.

## 11. Practice cautions

[Avoid pseudo-dispassion/suppression, dry intellectual escapism, or spiritual pride.]

## 12. Contribution status

- Sanskrit checked: no
- Grammar checked: no
- Translation reviewed: no
- Visual reviewed: no
"""

def main():
    parser = argparse.ArgumentParser(description="Generate a premium markdown template for scripture verses.")
    parser.add_argument("verse", type=int, help="Verse number to generate (e.g. 24)")
    parser.add_argument("--text", choices=["vbt", "ashtavakra"], default="vbt", help="The text module target (vbt or ashtavakra)")
    parser.add_argument("--chapter", type=int, default=1, help="Chapter number (applicable for Ashtavakra Gita, default: 1)")
    
    args = parser.parse_args()
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    if args.text == "ashtavakra":
        output_dir = os.path.join(root_dir, "texts", "ashtavakra-gita", "sutras")
        template = ASHTAVAKRA_TEMPLATE
    else:
        output_dir = os.path.join(root_dir, "texts", "vijnana-bhairava-tantra", "sutras")
        template = VBT_TEMPLATE

    verse_str = f"{args.verse:03d}"
    filename = f"{verse_str}.md"
    filepath = os.path.join(output_dir, filename)

    if os.path.exists(filepath):
        print(f"Error: File {filepath} already exists. Will not overwrite.")
        sys.exit(1)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template.format(number=args.verse, chapter=args.chapter))

    print(f"Created template at {filepath}")

if __name__ == "__main__":
    main()
