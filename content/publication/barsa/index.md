---
title: "BARSA: An Adaptive Test-Time Scaling Strategy for Mathematical Reasoning under Global Compute Budgets"
authors:
- Yufan Zhao
- Yinsicheng Jiang
- Cheng Deng
- Yeqi Huang
- Tairan Xu
- Zhan Lu
- Luo Mai
- Wenda Li
date: "2026-06-17T00:00:00Z"
doi: "https://openreview.net/forum?id=b1cuMvjwDo"

publishDate: "2026-06-17T00:00:00Z"

publication_types: ["paper-conference"]

publication: "ICML 2026 Workshop on AI for Math (AI4Math)"
publication_short: "ICML 2026 Workshop"
publication_status: "accepted"

abstract: "This paper presents our submission to the AI Mathematical Olympiad - Progress Prize 3 (AIMO 3) competition. We propose Budget-Aware Recursive Self-Aggregation (BARSA), an adaptive test-time scaling framework for mathematical reasoning under a global inference budget. BARSA extends Recursive Self-Aggregation by using answer-distribution statistics and runtime estimates to decide whether to accept the current answer or continue with another aggregation round. We evaluate BARSA on the AIMO 3 leaderboards and a curated benchmark of AI-hard problems. Our analysis shows that recursive aggregation is most effective when the correct answer appears as a minority candidate or when the answer distribution is unstable, but remains vulnerable to deceptive wrong majorities. Under a fixed time budget, BARSA improves mean accuracy and reduces score variance, outperforming the strongest majority-voting baseline and non-budget-aware RSA on public leaderboard submissions while reducing score standard deviation by more than half."

summary: "BARSA (Budget-Aware Recursive Self-Aggregation) is an adaptive test-time scaling framework for mathematical reasoning under a fixed global inference budget. It extends Recursive Self-Aggregation with answer-distribution statistics and runtime estimates to decide when to stop aggregating, improving mean accuracy and halving score variance over majority-voting and non-budget-aware RSA baselines on the AIMO 3 leaderboards."

tags:
- Test-Time Scaling
- Inference-Time Compute
- Mathematical Reasoning
- Self-Aggregation
- Large Language Models
featured: true

links:
- name: OpenReview
  url: https://openreview.net/forum?id=b1cuMvjwDo
url_pdf: 'https://openreview.net/pdf?id=b1cuMvjwDo'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: 'BARSA: Budget-Aware Recursive Self-Aggregation'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**BARSA** (Budget-Aware Recursive Self-Aggregation) is an adaptive test-time scaling framework for mathematical reasoning under a fixed global inference budget, developed for the AI Mathematical Olympiad — Progress Prize 3 (AIMO 3) competition:

### 1. Budget-Aware Recursive Aggregation
- **Extends Recursive Self-Aggregation (RSA)**: Adds a global-budget-aware stopping rule
- **Answer-Distribution Statistics**: Uses candidate-answer statistics and runtime estimates to decide whether to accept the current answer or run another aggregation round
- **Compute-Aware Scheduling**: Allocates inference compute under a fixed global time budget

### 2. When Recursive Aggregation Helps
- **Most Effective**: When the correct answer is a minority candidate or the answer distribution is unstable
- **Known Failure Mode**: Remains vulnerable to deceptive wrong majorities

### 3. Results on AIMO 3
- **Higher Mean Accuracy** and **lower score variance** under a fixed time budget
- **Outperforms** the strongest majority-voting baseline and non-budget-aware RSA on public leaderboard submissions
- **Halves Score Variance**: Reduces score standard deviation by more than half
