---
title: "Ryze: Evidence-Enriched Data Synthesis from Biomedical Papers"
authors:
- Yeqi Huang
- Yue Chen
- Yanwei Ye
- Guanhao Su
- Luo Mai
date: "2026-06-01T00:00:00Z"
doi: "https://arxiv.org/abs/2606.00902"

publishDate: "2026-06-01T00:00:00Z"

publication_types: ["paper-conference"]

publication: "Annual Meeting of the Association for Computational Linguistics (ACL 2026), System Demonstrations"
publication_short: "ACL 2026 Demo"
publication_status: "accepted"

abstract: "We present Ryze, a fully automated system that converts biomedical papers into training datasets and specialized vision-language models. Unlike prior pipelines that discard contextual information, Ryze preserves complete supporting evidence — the visual element, its caption, the extracted structure, and the referring paragraphs — when synthesizing question-answer data. A chart/table-aware extraction pipeline reduces OCR errors through multi-stage processing, and a progress-gated training procedure combines supervised fine-tuning with reinforcement learning while automatically detecting saturation. Starting from Qwen3-VL-8B, the resulting BioVLM-8B model achieves 48.0% accuracy on LAB-Bench, surpassing GPT-5.2 by 3.8 percentage points while costing under $200 to train, and outperforms human-curated datasets at equal token budgets."

summary: "Ryze is a fully automated system that turns biomedical papers into evidence-enriched VLM training data, preserving complete supporting evidence (visual element, caption, structure, and referring text). Through chart/table-aware extraction and progress-gated SFT + RL training, the resulting BioVLM-8B model reaches 48.0% accuracy on LAB-Bench, surpassing GPT-5.2 by 3.8 points at under $200 training cost."

tags:
- Vision Language Models
- Biomedical AI
- Data Synthesis
- Large Language Models
featured: true

links:
- name: ArXiv
  url: https://arxiv.org/abs/2606.00902
- name: Demo
  url: https://ryze.12th.day
- name: Video
  url: https://youtu.be/5L2YShSaIQQ
url_pdf: 'https://arxiv.org/pdf/2606.00902'
url_code: 'https://github.com/Chivier/Ryze'
url_dataset: ''
url_poster: ''
url_project: 'https://ryze.12th.day'
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/5L2YShSaIQQ'

image:
  caption: 'Ryze Pipeline'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**Ryze** introduces a fully automated pipeline that converts biomedical papers into training data and specialized vision-language models:

### 1. Evidence-Enriched Data Synthesis
- **Complete Supporting Evidence**: Preserves the visual element, caption, extracted structure, and referring paragraphs instead of discarding context
- **Chart/Table-Aware Extraction**: Multi-stage processing reduces OCR errors
- **Full-Context QA Synthesis**: Generates question-answer data grounded in the source document

### 2. Progress-Gated Training
- **SFT + RL**: Combines supervised fine-tuning with reinforcement learning
- **Saturation Detection**: Automatically detects when training saturates
- **Cost-Effective**: BioVLM-8B trained at under $200

### 3. Strong Performance
- **48.0% Accuracy** on LAB-Bench
- **3.8 Points Above GPT-5.2**
- **Beats Human-Curated Datasets** (PubMedQA, MedQA) at equal token budgets
