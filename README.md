# FinOps-SRE Sentinel Framework

An enterprise-grade, fault-tolerant cloud infrastructure telemetry ingestion and cost-anomaly orchestration subsystem built with Python 3.13+. This framework showcases strict Pydantic v2 data contracts, decoupled architecture protocols, defensive failure isolation boundaries, and fully automated continuous integration.

---

## 🎯 Project Overview & Purpose

In modern cloud-native environments, infrastructure tracking pipelines are constantly inundated with massive volumes of raw metric data streams. Traditional monitoring setups often suffer from two major vulnerabilities: **cascading application crashes** caused by malformed data inputs, and **uncontrolled cloud spend (cloud-bleed)** due to delayed anomaly detection.

The **FinOps-SRE Sentinel Framework** is engineered as a high-availability middle-tier broker that ingest real-time system metrics, runs them through strict validation enclaves, and dispatches them across an intelligent multi-agent profile routing layer. By sitting seamlessly between infrastructure metric streams and upstream analytical consumers, it serves as an unbreakable operational guardrail.

### Where This System Can Be Implemented
*   **Multi-Cloud FinOps Observability Platforms:** To ingest, sanitize, and unify incoming telemetry streams (AWS, GCP, Azure) into a standard corporate data contract.
*   **Kubernetes Cluster Autonomous SRE Controllers:** As the high-availability ingestion engine for custom agents tracking real-time microservice performance and container scaling behavior.
*   **Enterprise Billing & Cost Governance Gates:** Positioned in front of analytical dashboards to block, log, and alert on irregular resource utilization patterns or runaway cluster configurations before costs spiral.

---

## 💰 Core Business Benefits & Accomplishments

Implementing this architectural paradigm achieves critical real-world site reliability and cost governance outcomes:

| Core SRE Dimension | Architectural Implementation | Tangible Operational Benefit |
| :--- | :--- | :--- |
| **Absolute Fault Isolation** | Decoupled routing boundaries isolate downstream agent failures and handle runtime anomalies gracefully. | **Zero Cascading Downtime:** An agent timeout, signature error, or execution crash cannot propagate upward to bring down the telemetry ingestion pipeline. |
| **Proactive Cost Control** | Real-time tracking of localized running costs directly inside the infrastructure schema layer (`billing_rate_hourly_usd`). | **Mitigation of Cloud Bleed:** Runaway cluster nodes or zombie cloud resources are trapped at the ingestion gate before triggering catastrophic invoice overruns. |
| **Strict Schema Enclaves** | Explicit boundary checks block validation breaches (such as hallucinated metric states or out-of-bounds metrics). | **Prstine Data Integrity:** Downstream machine learning models and tracking tools are entirely shielded from corrupt telemetry data or prompt-drift anomalies. |
| **Predictable Deployments** | Root-anchored path configurations combined with isolated continuous integration (CI) runtimes. | **High Engineering Velocity:** Path alignment is preserved across all environments, ensuring instant test compilation from a developer's machine to the cloud. |

---

## 🛡️ Engineering Design & Architectural Boundaries

### 1. Strict Structural Data Contracts (`app/schemas.py`)
To prevent malformed data streams or AI prompt hallucinations from poisoning the system, ingestion is bound to strict type validation models. Utilizing **Pydantic v2**, the engine enforces strict limits at the exact moment of model instantiation (e.g., verifying `cpu_utilization_pct` falls strictly within a `0.0` to `100.0` range). Any anomalous input is instantly rejected with a structured validation error before it ever pollutes the execution thread.

### 2. High-Availability Failure Isolation (`app/engine.py`)
The `CoreOrchestrator` implements an abstract, protocol-based routing matrix (`IAgent`) to dispatch processed metrics across multi-agent profiles (Cohere, Qwen, DeepSeek, Llama). Rather than allowing individual agent runtime crashes to bring down the central application, the dispatch loop is wrapped in a strict try/except boundary. If an execution route encounters an exception or an ad-hoc dictionary breakdown, the failure is caught, the specific agent is dynamically flagged as `FAILED`, and a sanitized, structured JSON-ready error envelope is returned.

### 3. Native Path Mapping and Test Discovery (`pytest.ini`)
The workspace environment utilizes a root-level `pytest.ini` anchor that configures native `pythonpath = .` rules. This completely eliminates directory look-back constraints and package-caching errors common to Windows PowerShell environments, ensuring absolute compilation predictability across both local terminals and cloud runtimes.

---

## 📁 Repository Blueprint

The workspace strictly adheres to professional Python repository standards, isolating application modules from test dependencies:

```text
C:\WWORKING_folder\ProjectFolders\App
├── .github/
│   └── workflows/
│       └── test.yml                 # GitHub Actions CI automated suite
├── app/
│   ├── __init__.py                  # Package initialization anchor
│   ├── __main__.py                  # Direct framework simulation driver
│   ├── core_agents.py               # Autonomous SRE/FinOps agent logic
│   ├── engine.py                    # Orchestrator core & failure isolation
│   ├── model_profiles.py            # Free model matrix configuration
│   └── schemas.py                   # Strict Pydantic telemetry models
├── tests/
│   ├── __init__.py                  # Test module package indicator
│   └── test_integration_suite.py    # Happy-path & guardrail validation tests
├── .gitignore                       # System protection exclusions (.venv, cache)
└── pytest.ini                       # Natively mapped root python pathing
```

---

## 🛠️ Verification & Direct Execution

Follow these steps to run and test the sentinel pipeline inside an isolated virtual environment (`.venv`):

### 1. Run the Direct Simulation Stream
Execute the main entry point to view the infrastructure bootstrap sequence, a successful production routing trace, and the defensive validation engine blocking malformed metrics in real-time:
```powershell
python -m app
```

### 2. Run the Comprehensive Test Suite
Execute the integration test suite via `pytest` to confirm your system guardrails remain 100% green:
```powershell
python -m pytest tests/test_integration_suite.py -v
```

---

## 🤖 Continuous Integration Workflow (`.github/workflows/test.yml`)

The framework features a production-grade **GitHub Actions CI Pipeline** configured to trigger on every single code `push` and `pull_request` to the main branches. 

The pipeline spins up an isolated, cloud-hosted `ubuntu-latest` Linux container, implements rapid `pip` dependency caching, installs core components (`pydantic`, `pytest`), mounts the working directory path explicitly, and runs the entire suite automatically to enforce zero-regression codebase health.
