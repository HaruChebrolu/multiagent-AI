# MultiAgent-AI

**Multi-Agent System for Autonomous Ceph Cluster Management**

This project implements an intelligent, multi-agent orchestration system for monitoring, analyzing, and managing Ceph storage clusters using [CrewAI](https://github.com/joaomdmoura/crewAI). At its core, a centralized `CephOrchestrator` agent coordinates a team of specialized agents to perform real-time cluster health checks, bug triage, documentation lookups, performance monitoring, and automated recommendations.

Key Features:
- 🔍 **Cluster Status Evaluation** via CephViz Agent  
- 📊 **Performance & Disk Analysis** via Observability Agent  
- 🐞 **Lookup and explain Ceph bugs** via Bug Intelligence Agent
- 📚 **Ceph Docs Lookup** via MaverickAgent  
- 🧠 **Automated performance tuning Recommendations** via Performance Agent  
- 🤖 **Hierarchical Task Planning** using CrewAI-style orchestration


🧱 Built With:
- Python, [CrewAI](https://github.com/joaomdmoura/crewAI), LangChain Tools
- Ceph CLI + SSH, Metrics via PostgreSQL, Bugzilla API, Ceph Docs Search

## Support matrix
Python - 3.11

## Flowchart
<img width="1452" alt="flowchart" src="https://github.com/user-attachments/assets/62b9a835-e1d7-4590-ba2b-041b3c5d2347" />


## Installation

1. Install `uv` package manager: https://docs.astral.sh/uv/getting-started/installation/

2. Sync dependencies:
    ```bash
    uv sync
    ```
3. Optional - if you want to use python 3.11.x when you have multiple python versions installed.
    ``` bash
    uv venv -p 3.11
    source .venv/bin/activate
    ```

## Running the code

```bash
cd src
uv run orchestration/flow.py
```


