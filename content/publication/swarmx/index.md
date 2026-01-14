---
title: "SwarmX: A Scheduler Agent Framework for Large Agentic Workflow Clusters"
authors:
- Yeqi Huang
- Yanwei Ye
- Guomin Chen
- Wenhao Su
- Bin Gong
- Jialian Li
- Yao Fu
- Yinsicheng Jiang
- Xuan Sun
- Le Xu
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

abstract: "Scaling agentic workflows across clusters with tens of thousands of GPUs exposes two system requirements absent in conventional schedulers: accurately predicting complex, evolving workflow execution-time variation, and providing unified, programmable support for adopting AI across scheduling scenarios. Existing systems lack the abstractions and mechanisms needed to satisfy these requirements, leading to suboptimal efficiency and limited scalability. We present SwarmX, the first scheduler agent framework that formulates cluster scheduling as an agentic intelligence problem. Each scheduler component integrates a specialized neural predictor, a maintained memory, a tool abstraction for controlled actions, and a coordinator implementing scheduling objectives. We build practical scheduler agents using this framework and enable them to collaborate via message-based coordination to optimize end-to-end workflow performance. Large-scale production and testbed experiments (millions of CPUs and nearly a thousand GPUs) both show that SwarmX significantly outperforms state-of-the-art systems across numerous critical workflow applications."

# Summary. An optional shortened abstract.
summary: "SwarmX is the first scheduler agent framework that formulates cluster scheduling as an agentic intelligence problem. With specialized neural predictors, memory components, and message-based coordination, SwarmX achieves up to 50% P99 latency improvement and doubles throughput while managing workloads spanning millions of CPU cores and nearly a thousand GPUs."

tags:
- Cluster Scheduling
- Agentic AI
- Large-Scale Systems
- Neural Prediction
- Workflow Management
- Production Systems
- High Performance Computing
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
  caption: 'SwarmX Scheduler Agent Architecture'
  focal_point: "Smart"
  preview_only: false

projects: []

slides: ""
---

## Key Contributions

**SwarmX** introduces the first scheduler agent framework designed for large-scale agentic workflow clusters:

### 1. Scheduler Agent Architecture
Each scheduling component is expressed as an agent consisting of:
- **Specialized Neural Predictor**: Variation prediction for workflow execution
- **Memory Component**: Captures prompts, models, devices, concurrency, and past decisions
- **Tool Abstraction**: Enables controlled router/scaler actions
- **Coordinator**: Implements scheduling objectives

### 2. Practical Scheduler Agents
- **Router Agent**: Risk-aware request dispatching
- **Scaler Agent**: Resource demand forecasting
- **Message-Based Coordination**: Unified protocol for agent collaboration
- **End-to-End Optimization**: Collective workflow performance optimization

### 3. Production-Ready Design
- **Fully Distributed**: Agents operate without control-plane bottlenecks
- **Transient Resource Support**: Accommodates dynamic resource availability
- **Compatibility Layers**: Ray and ComfyUI support for existing workflows
- **Fresh Runtime Signals**: Neural predictors run on execution servers

## Performance Achievements

### Production Scale
- **Millions of CPUs**: Proven at production scale
- **Nearly 1000 GPUs**: Heterogeneous GPU cluster support
- **Hundreds of Millions of Users**: Supporting real-world workloads

### Latency and Throughput
- **50% P99 Improvement**: Up to 50% reduction in tail latency
- **2x Throughput**: Doubled throughput under identical SLOs
- **10-60% Tail-Latency Gains**: Improvement over state-of-the-art approaches

### Robustness
- **Severe Drift Handling**: Stable performance under challenging conditions
- **Detailed Analysis**: Routing, scaling, overhead, and robustness validated
- **Controlled and Production Settings**: Proven in both environments

## Technical Innovation

SwarmX addresses critical challenges in agentic workflow scheduling:

- **Execution-Time Prediction**: Accurately predicts complex, evolving workflow patterns
- **AI-Native Scheduling**: Unified, programmable AI support across scenarios
- **Modular Decomposition**: Supports pre-training, online adaptation, and interpretability

## Deployment and Impact

SwarmX has been:
- **Developed Over Two Years**: Mature, battle-tested system
- **Deployed in Production**: Managing tens of thousands of servers
- **Planned Open-Source Release**: Upon acceptance, enabling community participation

## Applications

SwarmX enables:
- **Large Agentic Workflows**: Complex multi-agent workflow orchestration
- **GPU Cluster Management**: Efficient heterogeneous resource utilization
- **Scalable AI Services**: Production-ready AI workflow deployment
- **Research Platform**: Foundation for AI for Systems research
