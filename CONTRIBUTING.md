# Contributing to Open Spirituality

Thank you for your interest in contributing to the **Open Spirituality** project! We welcome contributions from Sanskrit scholars, spiritual practitioners, meditation teachers, developers, and designers.

To maintain the high quality and scholarly integrity of this repository, we follow strict guidelines.

## Non-Negotiable Principle: "Open Scholarship, Not Copied Spirituality"

Do **NOT** copy or reproduce text from modern copyrighted translations or commentaries (see each text module's README for specific copyrighted works and lineage references to avoid).
- Use these works as **reference scholars only**.
- When commenting or comparing, cite their views by referring to the text-specific bibliography database (e.g., `bibliography.bib`).
- All translations, grammatical analyses, and interpretations contributed to this repository must be original or in the public domain.

## How to Contribute

### 1. Sanskrit Scholars & Translators
- **Sanskrit Base Text**: Help verify the spelling and sandhi-splitting of the Sanskrit base text against canonical historical versions.
- **Word-by-word Grammar**: Help expand or refine the grammatical breakdown tables (roots, declensions, compound breakdowns).
- **Open Translation**: Suggest refinements to our translations to balance literal fidelity with readability.

### 2. Spiritual Practitioners & Teachers
- **Philosophical Meaning**: Review and expand the commentary, grounding it in traditional philosophical context (or other relevant schools).
- **Practice Instructions**: Help write and refine practical, non-exaggerated instructions for the contemplative practices.
- **Practice Cautions**: Ensure that instructions contain sensible safety advice (e.g., warning against forced breath retention or medical claims).

### 3. Designers & Visual Artists
- **Mermaid Diagrams**: Contribute or edit the ASCII/Mermaid concept maps in the markdown files.
- **SVG & Raster Graphics**: Design clean, high-resolution vector diagrams for subtle-body maps, state transitions, or concept mappings. Place the files in the text-specific visuals subdirectories.

### 4. Developers & Tool Builders
- **Data Models**: Verify that the JSON files under the `data/` subdirectories remain consistent with the markdown contents.
- **Validation Scripts**: Improve our Python content validators or template generators.
- **Web App**: Contribute to the site generator or front-end components.

## Pull Request Guidelines

1. **Verify Formatting**: Ensure your changes match the premium templates exactly.
2. **Run Validators**: Execute the local validation tool before submitting:
   ```bash
   python tools/sanskrit-validator/validate.py
   ```
3. **Cite Everything**: Make sure any scholarly claims include references to standard editions.
4. **Licensing**: By contributing, you agree that your code will be licensed under the MIT License and your literary/visual contributions under the CC BY-SA 4.0 License.
