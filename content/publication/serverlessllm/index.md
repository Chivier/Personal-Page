---
title: "(OSDI 2024) ServerlessLLM: Locality-Enhanced Serverless Inference for Large Language Models"
authors:
- Yao Fu
- Leyang Xue
- Yeqi Huang
- Andrei-Octavian Brabete
- Dmitrii Ustiugov
- Yuvraj Patel
- Luo Mai
date: "2024-02-27T00:00:00Z"
doi: "https://doi.org/10.48550/arXiv.2401.14351"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-02-27T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: "This paper presents ServerlessLLM, a locality-enhanced serverless inference system for Large Language Models (LLMs). ServerlessLLM exploits the substantial capacity and bandwidth of storage and memory devices available on GPU servers, thereby reducing costly remote checkpoint downloads and achieving efficient checkpoint loading. ServerlessLLM achieves this through three main contributions: (i) fast LLM checkpoint loading via a novel loading-optimized checkpoint format design, coupled with an efficient multi-tier checkpoint loading system; (ii) locality-driven LLM inference with live migration, which allows ServerlessLLM to effectively achieve locality-driven server allocation while preserving the low latency of ongoing LLM inference; and (iii) locality-aware server allocation, enabling ServerlessLLM to evaluate the status of each server in a cluster and effectively schedule model startup time to capitalize on local checkpoint placement. Our comprehensive experiments, which include microbenchmarks and real-world traces, show that ServerlessLLM surpasses state-of-the-art systems by 10 - 200X in latency performance when running various LLM inference workloads."

# Summary. An optional shortened abstract.
summary: ServerlessLLM, a serverless inference system for Large Language Models (LLMs), enhances performance by leveraging GPU server resources efficiently. It minimizes remote checkpoint downloads, optimizes checkpoint loading, and prioritizes locality-driven server allocation for improved latency. Through innovative checkpoint design, multi-tier loading, and live migration, ServerlessLLM outperforms existing systems by 10 - 200X in latency for LLM workloads, as demonstrated in extensive experiments.

tags:
- Source Themes
featured: false

links:
- name: OSDI
  url: https://www.usenix.org/conference/osdi24/presentation/fu
url_pdf: https://www.usenix.org/system/files/osdi24-fu.pdf
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
  caption: ''
  focal_point: ""
  preview_only: false

projects:
- internal-project

slides: ""
---

