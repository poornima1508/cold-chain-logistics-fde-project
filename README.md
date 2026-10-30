```markdown
# Cold-Chain Operations Copilot API

An enterprise-grade cold-chain telemetry monitoring engine and automated reasoning copilot engineered for pharmaceutical and perishable logistics. This system ingests high-frequency IoT sensor telemetry, identifies thermal excursions, cross-references spatial coordinates, and leverages Retrieval-Augmented Generation (RAG) to enforce regulatory compliance protocols (e.g., Directive `FRU-02`) in real time.

Designed for operational resilience, the platform provides automated risk assessments, actionable mitigations for fleet managers, and end-to-end containerized CI/CD validation.

---

## Technical Highlights

- **FastAPI Application Core:** Asynchronous REST architecture utilizing Pydantic for rigid schema validation and SQLAlchemy ORM for transactional consistency.
- **Relational Spatial & Telemetry Engine:** PostgreSQL backend storing granular sensor data, spatial attributes (`gps_lat`, `gps_lng`), threshold violations, and operational notes.
- **RAG-Driven Compliance Copilot:** Hybrid vector storage (ChromaDB) paired with an LLM inference engine (Ollama) to query local regulatory directives and output deterministic risk assessments.
- **Automated CI/CD Pipeline:** GitHub Actions workflow executing headless Docker image builds, integration checks, and container health verification on every push to `main`.
- **Infrastructure as Code:** Fully dockerized environment via Docker Compose orchestrating application services, local vector stores, and relational database containers.

---

## Architecture & Data Flow


```

```
                  +----------------------------------+
                  |   IoT Telemetry Stream / Client  |
                  +----------------------------------+
                                    |
                                    v
                  +----------------------------------+
                  |       FastAPI Engine Core        |
                  +----------------------------------+
                         /                  \
                        /                    \
                       v                      v
    +-----------------------+     +-----------------------+
    |     PostgreSQL DB     |     |   ChromaDB Vector     |
    |  (Telemetry Logs &    |     |  (Compliance Directives|
    |  Shipment Entities)   |     |   & Policy Docs)      |
    +-----------------------+     +-----------------------+
                                              |
                                              v
                                  +-----------------------+
                                  |   Ollama LLM Engine   |
                                  | (Automated Reasoning) |
                                  +-----------------------+
                                              |
                                              v
                                  +-----------------------+
                                  | Actionable Mitigation |
                                  |    & Alert Payload    |
                                  +-----------------------+

```

```

---

## Data Schema & Lineage

### Data Source
- **Telemetry Lineage:** Synthetic IoT sensor telemetry generated to mirror pharmaceutical cold-chain transport patterns, including sudden thermal spikes, power reefer unit failures, and multi-point spatial routing.
- **Knowledge Base:** Internal Standard Operating Procedures (SOPs) and cold-chain compliance directives, including Protocol `FRU-02` (Handling Reefers with Extended Thermal Excursions).

### Data Schema Attributes

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `shipment_id` | `String` | Unique business identifier for tracked cargo |
| `temperature` | `Float` | Real-time cargo ambient temperature (°C) |
| `humidity` | `Float` | Relative ambient humidity percentage |
| `gps_lat` | `Float` | Latitude coordinate decimal degrees |
| `gps_lng` | `Float` | Longitude coordinate decimal degrees |
| `timestamp` | `DateTime` | UTC event timestamp |
| `notes` | `Text` | Driver logs, manual events, or system-flagged anomalies |

---

## API Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/shipments` | Retrieves active shipment registry, current telemetry status, and risk flags |
| `POST` | `/telemetry` | Ingests new IoT sensor readings with schema validation and persistence |
| `POST` | `/copilot/evaluate` | Triggers RAG evaluation over a target shipment excursion to generate corrective actions |
| `GET` | `/health` | Live readiness and health check endpoint for container orchestrators |

---

## Local Development & Setup

### Prerequisites
- Docker Engine v20.10+ & Docker Compose
- Python 3.10+ (for standalone script development)
- Git

### Quickstart with Docker Compose

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/poornima1508/cold-chain-logistics-fde-project.git](https://github.com/poornima1508/cold-chain-logistics-fde-project.git)
   cd cold-chain-logistics-fde-project

```

2. **Provision local infrastructure:**
```bash
docker-compose up -d --build

```


3. **Verify running application:**
Access the interactive OpenAPI documentation at `http://localhost:8000/docs`.

---

## Continuous Integration & Automated Testing

This repository incorporates a production-grade **GitHub Actions** pipeline (`.github/workflows/ci.yml`) to guarantee build integrity:

* **Trigger:** Automated execution on `push` or `pull_request` targeting `main`.
* **Environment:** Isolated `ubuntu-latest` runner leveraging Docker Buildx.
* **Verification Strategy:** Builds the production container, provisions the microservice, waits for initialization, and runs a curl-based smoke test against `/shipments` to confirm operational health.

---

## Tech Stack

* **Application Backend:** FastAPI, Pydantic, Jinja2
* **Database & ORM:** PostgreSQL, SQLAlchemy
* **Vector Search & AI:** ChromaDB, Ollama
* **DevOps & Infrastructure:** Docker, Docker Compose, GitHub Actions

```

```
