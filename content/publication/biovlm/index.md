---
title: "BioVLM: Evidence-Enriched Data Synthesis from Biomedical Papers"
authors:
- Yeqi Huang
- Yue Chen
- Yanwei Ye
- et al.
date: "2025-05-01T00:00:00Z"
doi: ""

publishDate: "2025-03-17T00:00:00Z"

publication_types: ["paper-conference"]

publication: "Submitted to ACL 2025 System Demonstration"
publication_short: "ACL 2025 Demo (Under Review)"

abstract: "We present BioVLM, an automated pipeline that transforms biomedical papers into evidence-enriched VLM training data. Through progressive post-training (SFT + RL) on Qwen3-VL-8B, we train BioVLM-8B at under $200 cost. BioVLM-8B achieves 48.0% weighted accuracy on LAB-Bench, 12.6% above the base model and 3.8% above GPT-5.2."

summary: "BioVLM is an automated pipeline transforming biomedical papers into evidence-enriched VLM training data. Through progressive post-training on Qwen3-VL-8B, BioVLM-8B achieves 48.0% weighted accuracy on LAB-Bench, surpassing GPT-5.2 by 3.8% at under $200 training cost."

tags:
- Vision Language Models
- Biomedical AI
- Data Synthesis
- Large Language Models
featured: true

links: []
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: 'BioVLM Pipeline'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**BioVLM** introduces an automated pipeline for biomedical VLM training:

### 1. Evidence-Enriched Data Synthesis
- **Automated Pipeline**: Transforms biomedical papers into high-quality VLM training data
- **Evidence Grounding**: Training data enriched with evidence from source papers

### 2. Cost-Effective Training
- **Progressive Post-Training**: SFT + RL on Qwen3-VL-8B
- **Low Cost**: BioVLM-8B trained at under $200

### 3. Strong Performance
- **48.0% Weighted Accuracy** on LAB-Bench
- **12.6% Above Base Model** (Qwen3-VL-8B)
- **3.8% Above GPT-5.2**
