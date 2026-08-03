---
title: "Wavel: A Fast and Efficient Compilation System for Wafer-Scale Accelerators"
authors:
- Yeqi Huang
- Congjie He
- Haocheng Xiao
- Yanwei Ye
- Yi-Chieh Wang
- Boyao Song
- Yangshen Deng
- Ziming Miao
- Lingxiao Ma
- Fan Yang
- Luo Mai
date: "2026-07-15T00:00:00Z"
doi: ""

publishDate: "2026-07-15T00:00:00Z"

publication_types: ["paper-conference"]

publication: "ACM Symposium on Operating Systems Principles (SOSP 2026)"
publication_short: "SOSP 2026"
publication_status: "accepted"

abstract: "Wafer-scale accelerators offer a new scaling point for AI infrastructure, but they also create a new compilation regime: communication cost varies sharply with location, and the space of possible placements and execution schedules is enormous. Existing GPU, distributed, and vendor compilation systems largely retain a sharding-oriented view and therefore fail to fully leverage these emerging accelerators, leaving the dominant physical scheduling decisions unresolved. We make a key observation: at wafer scale, the central complexity of compilation shifts from finding a logical shard plan to constructing an executable schedule that fixes placement, layout alignment, and execution ordering. Based on this observation, we present Wavel, a fast and efficient compilation system for wafer-scale accelerators. Wavel introduces MeshIR to make executable schedules explicit, constructs them through two legal locality-preserving primitives, CUT and TUNE, and uses physical cost evaluation with structured pruning to keep search practical. Implemented on top of MLIR and evaluated on Cerebras WSE-3 and Tenstorrent Blackhole, Wavel matches and often surpasses expert manual designs, delivering 1.3x-1.4x higher throughput than WaferLLM and up to 2.97x speedup over automatic baselines, while reducing schedule search from hours or weeks to minutes or seconds."

summary: "Wavel makes executable wafer-scale schedules explicit through MeshIR, CUT, and TUNE. It achieves up to 3.6x speedup over state-of-the-art compilers, 1.3x-1.4x higher throughput than WaferLLM, and up to 2.97x speedup over automatic baselines, while reducing schedule search from hours or weeks to minutes or seconds."

tags:
- AI Compilers
- Wafer-Scale Computing
- Mesh Accelerators
- MLIR
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

image:
  caption: 'Wavel Compilation System'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**Wavel** is a fast and efficient compilation system for wafer-scale accelerators.

### Executable Schedules with MeshIR

- Makes placement, layout alignment, and execution ordering explicit.
- Shifts wafer-scale compilation from logical sharding to physical schedule construction.

### Locality-Preserving Search

- Constructs legal schedules using the CUT and TUNE primitives.
- Combines physical cost evaluation with structured pruning to keep search practical.

### Performance

- Evaluated on Cerebras WSE-3 and Tenstorrent Blackhole.
- Achieves up to 3.6x speedup over state-of-the-art compilers.
- Delivers 1.3x-1.4x higher throughput than WaferLLM and up to 2.97x speedup over automatic baselines.
- Reduces schedule search from hours or weeks to minutes or seconds.
