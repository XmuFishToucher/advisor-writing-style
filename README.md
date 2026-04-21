# Advisor Writing Style

Distill your advisor's academic writing style from PDF papers into an actionable style card for long-term writing assistance.

## How It Works

1. **Phase 1** — Parse PDF papers and extract style metrics (sentence length, passive voice ratio, hedging/assertive frequency, connector words, etc.)
2. **Phase 2** — Multi-dimensional analysis with triple validation, generating a comprehensive style card
3. **Phase 3** — Use the style card for polishing, generating, and alignment checking

## Project Structure

```
advisor-writing-style/
├── SKILL.md                          # Skill configuration (WorkBuddy)
├── advisor_style_card.md             # Generated style card (v1.0)
├── scripts/
│   └── extract_papers.py             # PDF parsing & metrics extraction
├── references/
│   ├── skill-template.md             # Style card template
│   └── style_analysis_framework.md   # Analysis framework
└── assets/                           # Reserved for sample outputs
```

## Style Card

The `advisor_style_card.md` was distilled from **22 papers** (2020–2025) published in Nature Communications, Science Advances, Advanced Materials, Advanced Functional Materials, NPG Asia Materials, etc.

It covers:
- Core style profile (macro structure, sentence fingerprint, hedging strategy)
- Per-section writing guides (Introduction / Methods / Results / Discussion / Conclusion)
- Expression DNA (connector words, signature phrases, taboos)
- Reusable sentence templates
- Honesty boundaries (confidence levels, limitations)

## Quick Start

```bash
# Install dependency
pip install pymupdf

# Parse papers
python3 scripts/extract_papers.py /path/to/pdfs --output ./parsed_papers
```

Then use the extracted metrics to generate or update the style card.

## License

MIT
