# Instructions for AI Coding Assistants (Agents)

All AI agents working in this repository must strictly adhere to the following rules, best practices, and guidelines before generating content, modifying files, or creating new translations/commentaries.

To support the scalability of **Open Spirituality** (which starts with the Vijñāna Bhairava Tantra but will grow to include other texts like the Shiva Sutras), this document is divided into **Global Rules** (repository-wide) and **Text-Specific Rules**.

---

# Part I: Global Repository Guidelines
These rules apply to all files, modules, and subdirectories in this repository.

## 1. The Core Principle: "Open Scholarship, Not Copied Spirituality"

Do **NOT** copy or reproduce copyrighted modern translations, commentaries, or course materials (e.g., Jaideva Singh, Swami Lakshmanjoo, Christopher Wallis, Bettina Bäumer, Mark Dyczkowski, Lilian Silburn, etc.) into the repository.
- Use them strictly as **comparison/reference scholars**.
- Cite their views by referencing their entries in the central bibliography file of each text module.
- If short comparative quotations (a single sentence or short phrase) are required to highlight a specific linguistic dispute, they must be properly attributed and conform strictly to the "Fair Use" doctrine for educational research.
- All translations, grammatical tables, and commentaries generated must be original and written for this project.

## 2. Universal Tone & Neutrality

- Maintain a highly scholarly, objective, yet respectful and contemplative tone.
- Avoid dogmatic, cult-like language, or promoting a single lineage/guru as exclusively correct.
- If different traditional commentaries conflict, document both viewpoints and label speculative arguments clearly.

## 3. Pre-Commit Validation

Before completing any task that adds or edits text or data files:
1. You **MUST** run the validation tool locally to prevent syntax errors and schema deviations:
   ```bash
   python tools/sanskrit-validator/validate.py
   ```
2. Any errors (missing headers, unfilled placeholders, or JSON parsing exceptions) must be fixed before concluding your work.

---

# Part II: Text-Specific Guidelines
These rules apply only when generating or modifying content inside specific text subdirectories.

## A. Vijñāna Bhairava Tantra (VBT) — `texts/vijnana-bhairava-tantra/`

### A.1 Sanskrit Source & Orthography
- Only use public-domain Sanskrit sources for base Devanagari and IAST transliterations, specifically the **Kashmir Series of Texts and Studies (KSTS) No. IX, 1918 edition**.
- Do not perform bulk digital replication of databases from the Muktabodha Digital Library without verifying their database license limits.
- Ensure sandhi-split precision. Always double-check Devanagari strings to ensure no mixed-character Latin symbols (e.g., `तद्वirudhyate`) creep into the JSON indexes or markdown headers.

### A.2 Mandatory Structure for Sutras & Dharanas
Every new verse markdown file added under `texts/vijnana-bhairava-tantra/sutras/` must strictly adhere to the 12-section premium template. Do not omit any sections:
1. **Sanskrit** (Devanāgarī and IAST)
2. **Word-by-word** grammatical breakdown table
3. **Open translation** (original, readable, non-infringing translation)
4. **Literal reading** (direct syntactic meaning)
5. **Philosophical meaning** (Trika / Kashmir Shaiva context, madhya, śūnya, spanda, etc.)
6. **Practice instruction** (contemplative or somatic technique guide)
7. **Visual map** (Mermaid flowchart showing concept relationships or breathing cycles)
8. **Key concepts** (bulleted vocabulary list matching glossary keys)
9. **Cross-references** (standardized connections to Shiva Sutras, Spanda Karika, etc.)
10. **Scholarly notes** (comparative academic details with citations)
11. **Practice cautions** (safety advice: no forced breathing, strain, or medical claims)
12. **Contribution status** (checklist verifying what has been peer-reviewed)

### A.3 Somatic Safety & Lineage Focus
- **Somatic & Practice Safety**: All practice guidelines (Section 11) must include realistic, non-exaggerated safety advice. Warn against forced breath suspension, straining, or hyperventilation. The system must remain safe for experimental contemplators.
- **Lineage Respect & Madhya Focus**: Treat the Trika tradition with deep respect. Ground breathing exercises in the concept of *Madhya* (resting in the effortless center/gap between breaths) rather than forced mechanical timing. Acknowledge the role of grace (śaktipāta) and study limits.
