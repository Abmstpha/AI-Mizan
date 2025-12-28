
## Mizan-AI

Mizan-AI is an evaluation-oriented dataset designed to test how well Large Language Models (LLMs) handle Hassaniya Arabic, a low-resource Arabic variety spoken mainly in Mauritania and surrounding regions.

The project focuses on capability assessment, not fine-tuning. It provides carefully designed prompts to probe understanding, generation, and linguistic competence in Hassaniya across multiple modalities.

⸻

## Motivation

Most LLM benchmarks focus on high-resource languages or standardized dialects (MSA, English, French). Hassaniya is largely absent from evaluation datasets, which leads to:
 • Overestimated multilingual performance
 • Silent failure modes in African and Maghrebi dialects
 • No visibility into reasoning vs memorization behavior

Mizan-AI exists to expose those gaps.

⸻

## Scope

This repository contains prompt-based evaluation datasets, not model outputs.

The goal is to measure:
 • Comprehension
 • Generation quality
 • Dialect awareness
 • Code-switching behavior
 • Robustness to non-standard orthography

⸻

## Dataset Structure

The dataset is consolidated into a single spreadsheet validation file, designed for paired-sentence evaluation.

Mizan-AI/
│
├── data/
│   ├── mizan_benchmark.xlsx    # Master evaluation sheet
│   └── mizan_benchmark.csv     # Text-based version for version control
│
├── docs/                       # Documentation
├── scripts/                    # Utility scripts
└── README.md

### Evaluation Columns

The Excel file contains the following structure:

| Column | Description |
|--------|-------------|
| `sentence` | The input prompt (Hassaniya or English) |
| `eval_type` | `understanding` (Hassaniya input) or `generation` (English input) |
| `chatgpt` | Score/Output for ChatGPT |
| `gemini` | Score/Output for Gemini |
| `claude` | Score/Output for Claude |
| `grok` | Score/Output for Grok |
| `mistral` | Score/Output for Mistral |
| `llama` | Score/Output for Llama |
| `notes` | Human observations, corrections, or score justifications |

### Methodology

1. **Understanding**: The `sentence` is in **Hassaniya**. The model must interpret it (e.g., translate, summarize, or answer questions).
2. **Generation**: The `sentence` is in **English**. The model must generate the equivalent **Hassaniya** output.

Since we have paired sentences (Hassaniya <-> English), the "ground truth" for one is simply the other version.

⸻

## Prompt Design Principles

 • Multiple valid answers when appropriate
 • No forced standardization (orthography varies on purpose)
 • Dialect-first, not MSA-derived
 • Designed for evaluation, not demo quality

⸻

## What This Is Not

 • Not a translation dataset
 • Not a training corpus
 • Not standardized Arabic
 • Not optimized for leaderboard gaming

⸻

## Intended Use

 • LLM benchmarking
 • Dialect robustness analysis
 • Research on low-resource language evaluation
 • Comparative model studies (open vs proprietary)

⸻

## Contribution

All contributions should be added directly to `data/mizan_benchmark.csv` (or the Excel file). Please ensure:

1. You provide the sentence text.
2. You specify the evaluation type (`understanding` or `generation`).
