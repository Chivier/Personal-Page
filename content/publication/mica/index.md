---
title: "MICA: An Efficient Compiler for Mesh-Based AI Accelerators"
authors:
- Yeqi Huang
- Congjie He
- Haocheng Xiao
- Yanwei Ye
- Yi-Chieh Wang
- Boyao Song
- Ziming Miao
- Lingxiao Ma
- Fan Yang
- Luo Mai
date: "2026-07-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2026-01-14T00:00:00Z"

# Publication type.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "Submitted to 18th USENIX Symposium on Operating Systems Design and Implementation (OSDI 26)"
publication_short: "OSDI 2026 (Under Review)"

abstract: "AI accelerators built on mesh architectures are emerging as a scalable platform for large AI models, vector search, scientific computing, and many other performance-critical workloads. Yet their 2D mesh design introduces strict locality constraints and a vast spatial-temporal scheduling space that existing GPU and distributed compilers cannot handle. We present MICA, the first end-to-end compiler stack for mesh accelerators. MICA introduces MeshIR, a new intermediate representation that makes locality and placement explicit through region-aware tensors and kernels, and it provides a novel search framework capable of efficiently exploring temporal-spatial schedules across millions of cores. On real Cerebras and Tenstorrent accelerators, MICA delivers 3.6x performance improvements over state-of-the-art compilers and even achieves 1.4x of expert hand-tuned performance. MICA reduces challenging wafer-scale schedule search from weeks to hours, enabling easy development of various applications that run 100-200x faster than on GPUs."

# Summary. An optional shortened abstract.
summary: "MICA is the first end-to-end compiler stack for mesh-based AI accelerators. It introduces MeshIR for locality-aware compilation and a novel search framework for temporal-spatial scheduling, achieving 3.6x speedup over state-of-the-art compilers and enabling 100-200x faster applications compared to GPUs."

tags:
- AI Compilers
- Mesh Accelerators
- Wafer-Scale Computing
- High Performance Computing
- System Design
- Cerebras
- Tenstorrent
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

# Featured image
image:
  caption: 'MICA Compiler Architecture'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**MICA** introduces the first end-to-end compiler stack designed specifically for mesh-based AI accelerators:

### 1. MeshIR - Novel Intermediate Representation
- **Region-aware Tensors**: Explicit representation of data locality on mesh architectures
- **Region-aware Kernels**: Computation placement made explicit in the IR
- **Locality Constraints**: Captures the strict locality requirements of 2D mesh designs

### 2. Temporal-Spatial Schedule Search
- **Vast Search Space**: Efficiently explores scheduling across millions of cores
- **Novel Search Framework**: Handles the unique challenges of mesh architectures
- **Automated Optimization**: Reduces manual tuning effort significantly

### 3. Cross-Platform Support
- **Cerebras WSE**: Full support for wafer-scale engines
- **Tenstorrent**: Support for mesh-based AI accelerators
- **Extensible Design**: Framework adaptable to future mesh architectures

## Performance Achievements

### Compiler Efficiency
- **3.6x Speedup**: Over state-of-the-art compilers
- **1.4x of Expert Performance**: Approaches or exceeds hand-tuned implementations
- **Search Time Reduction**: Weeks to hours for wafer-scale scheduling

### Application Performance
- **100-200x Faster**: Compared to GPU implementations
- **Easy Development**: Enables rapid application development for mesh accelerators
- **Broad Applicability**: Supports AI models, vector search, scientific computing

## Technical Innovation

MICA addresses critical challenges in mesh accelerator compilation:

- **Locality Management**: First-class support for 2D mesh locality constraints
- **Scale**: Handles hundreds of thousands to millions of cores
- **Automation**: Replaces manual, error-prone optimization with automated search

## Impact and Applications

MICA enables:
- **Accessible Mesh Computing**: Lower barrier to entry for mesh accelerator development
- **Performance-Critical Workloads**: AI, vector search, scientific computing
- **Research Platform**: Foundation for future mesh compiler research
- **Production Systems**: Practical compiler for real-world deployment
