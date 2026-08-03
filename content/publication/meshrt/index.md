---
title: "MeshRT: Compile-Time Governed Wafer-Scale Runtime for Low-Latency High-Throughput Inference"
authors:
- Congjie He
- Le Xu
- Zhan Lu
- Yeqi Huang
- Haocheng Xiao
- Cheng Deng
- Lingxiao Ma
- Ziming Miao
- Fan Yang
- Luo Mai
date: "2026-07-15T00:00:00Z"
doi: ""

publishDate: "2026-07-15T00:00:00Z"

publication_types: ["paper-conference"]

publication: "ACM Symposium on Operating Systems Principles (SOSP 2026)"
publication_short: "SOSP 2026"
publication_status: "accepted"

abstract: "Wafer-scale accelerators promise ultra-low-latency AI inference, but current system stacks still carry an unsustainably high cost premium. The reason is that many current and emerging inference techniques, such as batching and MoE, introduce runtime dynamism that existing wafer-scale systems cannot support efficiently. As a result, they must choose between two unsatisfactory options: accept suboptimal latency, or preserve low latency by restricting dynamic techniques, thereby limiting the models they can support and reducing aggregate throughput. This tradeoff significantly increases the cost of low-latency serving. We present MeshRT, the first wafer-scale system to achieve both ultra-low latency and high throughput for LLM inference. MeshRT achieves this via a novel system architecture design, which we call compile-time governance of runtime dynamism. This architecture features new system abstractions and mechanisms that enable MeshRT to compile dynamic events arising from LLM inference directly into per-core schedules, enabling decentralized execution with low runtime overhead. Implemented on a commodity wafer-scale accelerator, MeshRT preserves ultra-low latency while improving throughput by up to 30-68x over the state-of-the-art, and achieves 6-8x lower latency and 10-36x higher decode energy efficiency than GPU inference engines running on a large H200 GPU cluster in the low-latency regime."

summary: "MeshRT introduces compile-time governance of runtime dynamism for wafer-scale LLM inference. It preserves ultra-low latency while improving throughput by up to 30-68x, with 6-8x lower latency and 10-36x higher decode energy efficiency than H200 GPU inference engines in the low-latency regime."

tags:
- Large Language Models
- Wafer-Scale Computing
- AI Inference
- Runtime Systems
- Low-Latency Serving
- Mixture of Experts
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
  caption: 'MeshRT Runtime Architecture'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**MeshRT** is the first wafer-scale system to deliver both ultra-low latency and high throughput for LLM inference.

### Compile-Time Governance

- Compiles dynamic inference events directly into per-core schedules.
- Enables decentralized execution with low runtime overhead.
- Supports runtime dynamism introduced by techniques such as batching and MoE.

### Performance

- Preserves ultra-low latency while improving throughput by up to 30-68x over the state-of-the-art.
- Achieves 6-8x lower latency than H200 GPU inference engines in the low-latency regime.
- Improves decode energy efficiency by 10-36x over the same GPU baseline.
