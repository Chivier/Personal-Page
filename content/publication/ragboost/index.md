---
title: "RAGBoost: Efficient Retrieval-Augmented Generation with Accuracy-Preserving Context Reuse"
authors:
- Yinsicheng Jiang
- Yeqi Huang
- Liang Cheng
- Cheng Deng
- Xuan Sun
- Luo Mai
date: "2025-11-05T00:00:00Z"
doi: "https://arxiv.org/abs/2511.03475"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-11-05T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "Submitted to 8th Conference on Machine Learning and Systems (MLSys 2026)"
publication_short: "MLSys 2026 (Under Review)"

abstract: "Retrieval-augmented generation (RAG) systems enhance large language models (LLMs) by incorporating external knowledge from retrieval databases. However, these systems face significant computational overhead from retrieving and processing similar or identical contexts across concurrent sessions and multi-turn interactions. This paper introduces RAGBoost, an efficient RAG system that detects overlapping retrieved items across sessions to maximize cache efficiency. RAGBoost employs efficient context indexing, ordering, and de-duplication while maintaining accuracy through lightweight contextual hints. Our comprehensive evaluation shows that RAGBoost achieves 1.5-3X performance improvements for prefill operations compared to existing methods, demonstrating substantial efficiency gains without sacrificing generation quality."

# Summary. An optional shortened abstract.
summary: "RAGBoost introduces an efficient retrieval-augmented generation system that maximizes cache efficiency by detecting and reusing overlapping retrieved contexts across concurrent sessions and multi-turn interactions. Through efficient context indexing, ordering, and de-duplication with lightweight contextual hints, RAGBoost achieves 1.5-3X performance improvements for prefill operations while maintaining accuracy."

tags:
- Large Language Models
- Retrieval-Augmented Generation
- RAG Systems
- Context Caching
- Performance Optimization
- System Design
featured: true

links:
- name: ArXiv
  url: https://arxiv.org/abs/2511.03475
url_pdf: https://arxiv.org/pdf/2511.03475.pdf
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'RAGBoost Framework Overview'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**RAGBoost** introduces an efficient retrieval-augmented generation system with three main innovations:

### 1. Context Overlap Detection
- **Cross-Session Reuse**: Identifies overlapping retrieved items across concurrent RAG sessions
- **Multi-Turn Efficiency**: Detects and reuses contexts in multi-turn conversations
- **Cache Optimization**: Maximizes cache hit rates for frequently retrieved content

### 2. Efficient Context Management
- **Context Indexing**: Efficient indexing mechanism for rapid context lookup
- **Context Ordering**: Optimized ordering strategy for cache-friendly access patterns
- **Context De-duplication**: Eliminates redundant context processing across sessions

### 3. Accuracy-Preserving Design
- **Lightweight Contextual Hints**: Maintains generation accuracy despite context reuse
- **Quality-Aware Caching**: Ensures cached contexts preserve semantic fidelity
- **Robust Performance**: Consistent accuracy across diverse RAG workloads

## Performance Achievements

### Computational Efficiency
- **1.5-3× Speedup**: Significant performance improvements for prefill operations
- **Reduced Overhead**: Lower computational costs from context reuse
- **Scalable Design**: Efficient scaling across concurrent sessions

### Accuracy Preservation
- **No Quality Degradation**: Maintains generation quality with context reuse
- **Robust Across Workloads**: Consistent performance on diverse RAG tasks
- **Production-Ready**: Practical system suitable for real-world deployment

## Technical Innovation

RAGBoost addresses critical efficiency challenges in RAG systems:

- **Redundant Retrieval**: Eliminates repeated retrieval of similar contexts
- **Cache Utilization**: Maximizes benefit from existing cache infrastructure
- **Session Coordination**: Enables efficient sharing across concurrent RAG sessions

## Impact and Applications

RAGBoost enables:
- **Cost-Effective RAG**: Reduced computational costs for production RAG systems
- **Real-Time Applications**: Lower latency for interactive RAG workloads
- **Scalable Deployment**: Efficient multi-user RAG services
- **Energy Efficiency**: Reduced power consumption through context reuse

This work provides practical solutions for deploying efficient RAG systems at scale, addressing the growing computational demands of retrieval-augmented generation while preserving the quality that makes RAG systems valuable.
