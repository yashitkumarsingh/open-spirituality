# Open Spirituality

An open-source, citation-first, visual and practice-aware spiritual knowledge system.

The goal of this project is not to replace living teachers, lineages, or critical scholarly editions. Rather, it is to build a transparent, open, respectful, and technically excellent learning resource for seekers, students, Sanskrit learners, designers, and developers.

The system is structured as a collection of modular text directories (starting with the **Vijñāna Bhairava Tantra** as the first flagship module) under the `texts/` folder.

## Principles

- **Source-First**: We build upon historical, public-domain, or fully authorized Sanskrit base texts.
- **Open Translation**: All translations and word-by-word grammatical analyses are original works created for this repository and released under open content licenses.
- **No Copyright Pollution**: We do not reproduce modern copyrighted translations. We compare them only as scholarly references and cite them properly.
- **Clear Distinction**: We maintain strict, clear distinctions between the base text, literal readings, philosophical interpretations, and contemplative practices.
- **Lineage Respect & Scholarly Humility**: We document multiple interpretations, traditional commentaries, and lineage perspectives without pushing a singular dogma.
- **Visual Clarity**: Each practice or concept is accompanied by diagrams (e.g., concept maps, breath pacing guides, subtle-body maps) to assist understanding.
- **Machine-Readable**: All verses and practices are structured as JSON data models to enable downstream applications, translation tooling, and semantic search.

## Repository Architecture

```text
open-spirituality/
  README.md
  LICENSE.md
  CITATION.cff
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  GOVERNANCE.md

  texts/
    vijnana-bhairava-tantra/
      README.md
      metadata.yaml
      source-policy.md
      bibliography.bib
      sanskrit/
        devanagari.md
        iast.md
        verse-index.json
      sutras/
        001.md
        ...
      dharanas/
        001-breath-between-in-out.md
        ...
      themes/
        breath.md
        ...
      visuals/
        source/
        exported/
      data/
        sutras.json
        dharanas.json
        glossary.json
        taxonomy.json
        cross-references.json

  tools/
    sanskrit-validator/
    verse-template-generator/
```

## License Models

This repository uses a split-licensing model to protect and encourage both software development and content sharing:
- **Code & Software**: Licensed under the [MIT License](LICENSE.md#mit-license).
- **Original Content & Explanations**: Licensed under the [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License](LICENSE.md#creative-commons-attribution-sharealike-40-international).
- **Sanskrit Source Text**: Sourced from historical public-domain editions and manuscripts (e.g., KSTS 1918 for the VBT) and maintained as public domain/source-specific.

## Getting Started

To explore the first flagship text, navigate to the [Vijñāna Bhairava Tantra module](texts/vijnana-bhairava-tantra/README.md).

For contributions, please read [CONTRIBUTING.md](CONTRIBUTING.md).
For code of conduct rules, please see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
To understand how decisions are made, check [GOVERNANCE.md](GOVERNANCE.md).

---

## Important Disclaimers

> [!WARNING]
**Legal & Medical Disclaimer**:
This repository contains descriptions of ancient somatic, breathing, and psychological exercises. These descriptions are provided strictly for educational, historical, and scholarly research purposes. Some techniques (e.g., breath suspension) carry physiological and psychological risks. Practicing these techniques is at the user's sole risk. Consult a qualified medical practitioner before undertaking any breathing or intensive sensory meditation exercises. The contributors to this repository accept no liability for any adverse physical or mental effects resulting from the practice of these techniques.

> [!NOTE]
**Spiritual Limitations**:
In accordance with traditional contemplative lineage traditions, written texts serve merely as maps. Theoretical study cannot replace direct transmission of grace (śaktipāta) or initiation (dīkṣā) by a living teacher. Seekers are encouraged to approach these materials as scholarly guides rather than a substitute for qualified teacher-student guidance.

