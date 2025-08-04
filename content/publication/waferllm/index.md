---
title: "WaferLLM: Large Language Model Inference at Wafer Scale"
authors:
- Congjie He
- Yeqi Huang
- Pei Mu
- Ziming Miao
- Jilong Xue
- Lingxiao Ma
- Fan Yang
- Luo Mai
date: "2025-07-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "17th USENIX Symposium on Operating Systems Design and Implementation (OSDI 25)"
publication_short: "OSDI 2025"

abstract: "Emerging AI accelerators increasingly adopt wafer-scale manufacturing technologies, integrating hundreds of thousands of AI cores in a mesh architecture with large distributed on-chip memory (tens of GB in total) and ultra-high on-chip memory bandwidth (tens of PB/s). However, current LLM inference systems, optimized for shared memory architectures like GPUs, fail to exploit these accelerators fully. We introduce WaferLLM, the first wafer-scale LLM inference system. WaferLLM is guided by a novel PLMR model (pronounced as 'Plummer') that captures the unique hardware characteristics of wafer-scale architectures. Leveraging this model, WaferLLM pioneers wafer-scale LLM parallelism, optimizing the utilization of hundreds of thousands of on-chip cores. It also introduces MeshGEMM and MeshGEMV, the first GEMM and GEMV implementations designed to scale effectively on wafer-scale accelerators. Evaluations show that WaferLLM achieves up to 200× higher accelerator utilization than state-of-the-art methods. Leveraging a wafer-scale accelerator (Cerebras WSE2), WaferLLM delivers GEMV operations 606× faster and 16× more energy-efficient than on an NVIDIA A100 GPU. For full LLM inference, WaferLLM achieves 10-20× speedups over A100 GPU clusters running SGLang and vLLM."

# Summary. An optional shortened abstract.
summary: "WaferLLM introduces the first wafer-scale Large Language Model inference system, achieving up to 200× higher accelerator utilization and 10-20× speedups over GPU clusters. The system leverages a novel PLMR model and introduces MeshGEMM/MeshGEMV operations optimized for wafer-scale architectures with hundreds of thousands of AI cores."

tags:
- Large Language Models
- Wafer-Scale Computing
- AI Accelerators
- System Design
- High Performance Computing
- Parallel Computing
featured: true

links:
- name: OSDI 2025
  url: https://www.usenix.org/conference/osdi25/presentation/he
- name: GitHub
  url: https://github.com/MeshInfra/WaferLLM
url_pdf: ''
url_code: 'https://github.com/MeshInfra/WaferLLM'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'WaferLLM Architecture Overview'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Innovations

**WaferLLM** represents a breakthrough in large-scale AI inference, introducing the first system designed specifically for wafer-scale architectures:

### 1. PLMR Model (Plummer)
A novel performance model that captures the unique characteristics of wafer-scale architectures:
- **Distributed On-chip Memory**: Tens of GB total capacity
- **Ultra-high Memory Bandwidth**: Tens of PB/s aggregate bandwidth
- **Mesh Architecture**: Hundreds of thousands of AI cores interconnected

### 2. Wafer-Scale LLM Parallelism
Revolutionary parallelization strategy optimized for wafer-scale hardware:
- **Massive Core Utilization**: Efficiently leverages hundreds of thousands of AI cores
- **Novel Distribution Algorithms**: Optimizes workload distribution across the mesh
- **Memory Hierarchy Optimization**: Exploits distributed on-chip memory architecture

### 3. MeshGEMM and MeshGEMV
First-ever GEMM and GEMV implementations designed for wafer-scale accelerators:
- **Scalable Matrix Operations**: Optimized for mesh-connected AI cores
- **Memory-aware Computation**: Leverages distributed memory architecture
- **Energy-efficient Design**: Minimizes data movement across the mesh

## Performance Achievements

### Accelerator Utilization
- **200× higher utilization** compared to state-of-the-art methods
- Efficient scaling across hundreds of thousands of cores

### Computational Performance
- **GEMV operations**: 606× faster than NVIDIA A100 GPU
- **Energy efficiency**: 16× more energy-efficient than A100
- **Full LLM inference**: 10-20× speedups over A100 GPU clusters

### System Comparison
Outperforms existing systems:
- **SGLang**: 10-20× faster inference
- **vLLM**: 10-20× faster inference
- **GPU clusters**: Significant energy and performance advantages

## Technical Impact

WaferLLM addresses the fundamental mismatch between:
- **Current LLM systems**: Optimized for shared memory architectures (GPUs)
- **Emerging AI accelerators**: Wafer-scale distributed architectures

The system opens new possibilities for:
- **Massive-scale AI inference**: Leveraging wafer-scale manufacturing
- **Energy-efficient AI**: Reducing power consumption through optimized parallelism
- **Cost-effective deployment**: Better utilization of advanced AI hardware

## Open Source Contribution

WaferLLM is open-sourced at [https://github.com/MeshInfra/WaferLLM](https://github.com/MeshInfra/WaferLLM), enabling:
- **Research collaboration**: Advancing wafer-scale AI research
- **Industry adoption**: Practical deployment of wafer-scale systems
- **Educational use**: Learning about next-generation AI architectures

This work establishes the foundation for the next generation of AI inference systems, designed to exploit the unique advantages of wafer-scale AI accelerators. 