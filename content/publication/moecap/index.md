---
title: "MoE-CAP: Benchmarking Cost, Accuracy and Performance of Sparse Mixture-of-Experts Systems"
authors:
- Yinsicheng Jiang
- Yao Fu
- Yeqi Huang
- Ping Nie
- Zhan Lu
- Leyang Xue
- Congjie He
- Man-Kit Sit
- Jilong Xue
- Li Dong
- Ziming Miao
- Dayou Du
- Tairan Xu
- Kai Zou
- Edoardo Ponti
- Luo Mai
date: "2024-12-10T00:00:00Z"
doi: "https://arxiv.org/abs/2412.07067"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-12-10T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "arXiv preprint"
publication_short: "arXiv"

abstract: "The sparse Mixture-of-Experts (MoE) architecture is increasingly favored for scaling Large Language Models (LLMs) efficiently, but it depends on heterogeneous compute and memory resources. These factors jointly affect system Cost, Accuracy, and Performance (CAP), making trade-offs inevitable. Existing benchmarks often fail to capture these trade-offs accurately, complicating practical deployment decisions. To address this, we introduce MoE-CAP, a benchmark specifically designed for MoE systems. Our analysis reveals that achieving an optimal balance across CAP is difficult with current hardware; MoE systems typically optimize two of the three dimensions at the expense of the third-a dynamic we term the MoE-CAP trade-off. To visualize this, we propose the CAP Radar Diagram. We further introduce sparsity-aware performance metrics-Sparse Memory Bandwidth Utilization (S-MBU) and Sparse Model FLOPS Utilization (S-MFU)—to enable accurate performance benchmarking of MoE systems across diverse hardware platforms and deployment scenarios."

# Summary. An optional shortened abstract.
summary: "MoE-CAP introduces a comprehensive benchmark for evaluating sparse Mixture-of-Experts systems across three key dimensions: Cost, Accuracy, and Performance. The benchmark reveals fundamental trade-offs in MoE deployments and proposes sparsity-aware metrics (S-MBU and S-MFU) along with CAP Radar Diagrams to help practitioners make informed deployment decisions for large-scale MoE systems."

tags:
- Machine Learning
- Large Language Models
- Mixture of Experts
- Benchmarking
- Performance Optimization
- System Design
featured: true

links:
- name: ArXiv
  url: https://arxiv.org/abs/2412.07067
url_pdf: https://arxiv.org/pdf/2412.07067.pdf
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
  caption: 'MoE-CAP Framework Overview'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**MoE-CAP** introduces a comprehensive benchmarking framework for sparse Mixture-of-Experts systems with three main contributions:

### 1. MoE System Trade-off Analysis
- **Cost-Performance Optimized**: Systems that minimize deployment costs while maintaining high throughput
- **Accuracy-Cost Optimized**: Systems that balance model quality with budget constraints  
- **Accuracy-Performance Optimized**: Systems that maximize both model quality and inference speed

### 2. Sparsity-Aware Performance Metrics
- **Sparse Memory Bandwidth Utilization (S-MBU)**: Accounts for selective expert activation patterns in memory usage calculations
- **Sparse Model FLOPS Utilization (S-MFU)**: Measures computational efficiency considering sparse expert routing

### 3. CAP Radar Diagram Visualization
A novel visualization tool that displays the trade-offs between Cost, Accuracy, and Performance across different MoE systems and hardware configurations.

## Technical Innovation

The benchmark addresses critical gaps in existing MoE evaluation by:

- **Heterogeneous Hardware Support**: Evaluating performance across GPUs, CPUs, and mixed-tier memory systems
- **Real-world Deployment Scenarios**: Including serverless endpoints, elastic infrastructure, and spot-instance pricing
- **Comprehensive Model Coverage**: Supporting diverse MoE architectures from Switch-C to DeepSeek-R1

## Impact and Applications

MoE-CAP enables practitioners to:
- Make informed decisions about MoE system selection and deployment
- Optimize resource allocation for cost-effective LLM serving
- Understand fundamental trade-offs in sparse expert systems
- Predict performance on lower-cost hardware configurations

This work provides essential tools for the growing ecosystem of sparse MoE systems, helping bridge the gap between theoretical model capabilities and practical deployment realities. 