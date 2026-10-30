Here is your updated, fully polished `README.md` file. It incorporates your live Streamlit cloud demo link, updates the architecture and setup instructions to reflect your self-contained cloud deployment, and maintains the professional Forward Deployed Engineer (FDE) tone:

```markdown
# Cold-Chain Operations Copilot API

### An End-to-End Enterprise Solution for Real-Time Thermal & Spatial Telemetry Monitoring

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cold-chain-logistics-fde-project.streamlit.app/)
[![CI/CD Pipeline](https://github.com/poornima1508/cold-chain-logistics-fde-project/actions/workflows/ci.yml/badge.svg)](https://github.com/poornima1508/cold-chain-logistics-fde-project/actions)

---

## 🚀 Live Demo

Test the live interactive dashboard right now in your browser:
👉 **[https://cold-chain-logistics-fde-project.streamlit.app/](https://cold-chain-logistics-fde-project.streamlit.app/)**

---

## 1. Executive Summary & Problem Context

### The Business Problem

In high-stakes supply chain logistics—specifically pharmaceutical distribution and perishable food supply—maintaining strict thermal integrity is non-negotiable. A single degree Celsius deviation above safety thresholds during transport can ruin millions of dollars in sensitive biological shipments, leading to total product loss, regulatory audits, and critical delays in medical supply chains.

### Traditional System Failure Modes

- **Post-Hoc Anomaly Detection:** Most logistics fleets record temperature data locally on data loggers, meaning excursions are only identified *after* the cargo arrives at a distribution warehouse—when it is already too late to intervene.
- **Disconnected Data Silos:** Geographic tracking (GPS), sensor telematics (temperature/humidity), and operational compliance protocols exist in fragmented databases and PDF manuals.
- **Manual Compliance Lookup:** When an alarm triggers, fleet dispatchers must manually cross-reference complex regulatory documentation (e.g., Protocol Directive `FRU-02`) to figure out whether to adjust reefer settings, reroute the vessel, or declare cargo total loss.

---

## 2. Who We Are Solving For

This application directly empowers three operational personas within enterprise cold-chain organizations:

1. **Fleet Dispatchers & Control Tower Operators:** Need immediate alerts on real-time spatial and thermal anomalies with instant, plain-English instructions on what action to take next.
2. **Regulatory & Quality Assurance (QA) Officers:** Require automated compliance checks against legal guidelines and standard operating procedures (SOPs) without reading hundred-page manuals during an ongoing breach.
3. **Logistics Executives:** Need a reliable, maintainable platform integrated into existing database infrastructure with minimal latency and high uptime guarantees.

---

## 3. What the Forward Deployed Engineer (FDE) Did

As a **Forward Deployed Engineer (FDE)**, the core responsibility was bridging the gap between raw AI/data capabilities and a actual production environment. An FDE does not just write isolated algorithm code; they analyze operational workflows, integrate heterogeneous data streams, configure scalable storage, enforce automated testing, and deliver an end-to-end maintainable system.

### FDE Implementation Deliverables:

1. **Designed & Built the Core Application Architecture:** Formulated an intuitive, self-contained dashboard UI using **Streamlit** for zero-friction recruiter and stakeholder review.
2. **Modeled Relational & Spatial Telemetry:** Configured data structures alongside **Pydantic** to validate incoming IoT telemetry (latitude, longitude, temperature, humidity, timestamps) and maintain historical audit trails.
3. **Implemented Local RAG Reasoning:** Configured domain-specific compliance protocols (such as Protocol Directive `FRU-02`) connected to reasoning logic to evaluate thermal breaches against real policies and generate actionable risk mitigations.
4. **Containerized Infrastructure & IaC:** Orchestrated the application stack using **Docker & Docker Compose** for one-command deployment across distributed nodes.
5. **Established CI/CD Automation:** Authored a **GitHub Actions** workflow that builds container instances, verifies initialization, and performs automated validation on every main branch update.

---

## 4. End-to-End System Architecture


```

```
               [ High-Frequency IoT Sensors ]
                             │
                             ▼
               +-----------------------------+
               | Streamlit Operations Copilot|
               | (Frontend UI & Logic Engine)|
               +-----------------------------+
                 /                     \
                /                       \
               ▼                         ▼
     +-------------------+     +-------------------+
     |  Telemetry Logs   |     | Compliance RAG DB |
     | (Active Shipments |     | (Indexed SOPs &   |
     | & Excursion Data) |     | Directive FRU-02) |
     +-------------------+     +-------------------+
                                       │
                                       ▼
                               +-------------------+
                               | Actionable Output |
                               | (Mitigation Plan) |
                               +-------------------+

```

```

---

## 5. Technical Highlights & Stack Details

- **Frontend & UI:** Streamlit, Python
- **Persistence & Data Modeling:** SQLAlchemy ORM, Pydantic, PostgreSQL
- **AI / Vector Search / RAG:** ChromaDB (Vector Store), Ollama (Local LLM Inference)
- **DevOps & Infrastructure:** Docker, Docker Compose, GitHub Actions (CI/CD Pipeline)

---

## 6. Primary System Capabilities

| Feature Component | Description |
| --- | --- |
| `📦 Shipment Telemetry` | Retrieves active shipments, current spatial/thermal readings, and real-time excursion risk alerts. |
| `🤖 Compliance Copilot` | Evaluates specific shipment excursions using contextual RAG retrieval and returns recommended SOP steps. |
| `☁️ Public Cloud Deployment` | Fully accessible out-of-the-box via Streamlit Community Cloud without external backend server dependencies. |

---

## 7. Local Setup & Quickstart

### Prerequisites

- [Docker Engine](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/)
- Python 3.10+ (for local environment debugging)
- Git

### Deployment Steps

1. **Clone the repository:**
```bash
git clone [https://github.com/poornima1508/cold-chain-logistics-fde-project.git](https://github.com/poornima1508/cold-chain-logistics-fde-project.git)
cd cold-chain-logistics-fde-project

```

2. **Run Streamlit Locally (Alternative):**

```bash
pip install -r requirements.txt
streamlit run app/frontend.py

```

3. **Launch Full Docker Stack (Optional):**

```bash
docker-compose up -d --build

```

```

```
