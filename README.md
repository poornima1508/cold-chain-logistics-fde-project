# Cold-Chain Operations Copilot

### An End-to-End Enterprise Solution for Real-Time Thermal & Spatial Telemetry Monitoring

---

## 🚀 Live Demo

Test the live interactive dashboard right in your browser:
👉 **[https://cold-chain-logistics-fde-project.streamlit.app/](https://cold-chain-logistics-fde-project.streamlit.app/)**

---

## 1. The Business Problem

When shipping sensitive items like vaccines, biologics, or perishable food, keeping strict temperature control is non-negotiable. If a cargo container or truck gets too warm, millions of dollars in sensitive medical payloads can be ruined instantly, leading to total product loss and major supply chain delays.

### Traditional System Failure Modes:

* **Post-Hoc Detection:** Most fleets record temperatures locally on data loggers, meaning excursions are only found *after* the cargo arrives—when it is too late to intervene.
* **Fragmented Data Silos:** GPS tracking, sensor telematics, and legal compliance manuals live in separate, disconnected systems.
* **Manual Compliance Lookups:** When an alarm triggers, dispatchers have to manually search through complex compliance manuals (like USP guidelines) to figure out how to handle the emergency.

---

## 2. Who This App Is For

* **Fleet Dispatchers:** Operators who need immediate alerts on spatial and thermal anomalies with clear, step-by-step instructions on what to do next.
* **Quality Assurance (QA) Officers:** Teams who need automated compliance verification against standard operating procedures (SOPs) without reading hundred-page rulebooks during an active breach.

---

## 3. What I Built as a Forward Deployed Engineer (FDE)

As a Forward Deployed Engineer, my goal was to build a complete production-ready system that bridges raw backend data processing with an intuitive interface.

### Key Engineering Deliverables:

1. **Asynchronous Backend API:** Built a high-performance RESTful API using **FastAPI** to ingest high-frequency IoT sensor data with minimal latency.
2. **Relational & Spatial Data Modeling:** Configured **PostgreSQL** alongside **SQLAlchemy ORM** and **Pydantic** to validate incoming metrics (temperature, humidity, latitude, longitude) and maintain historical audit trails.
3. **Local RAG Compliance Engine:** Set up a vector storage pipeline in **ChromaDB** to index official compliance directives (such as Protocol Directive `FRU-02`). Connected this retrieval step to **Ollama** for local LLM inference, evaluating thermal breaches against real policies to generate actionable recovery steps.
4. **Interactive User Interface:** Developed a clean frontend using **Streamlit** to provide zero-friction access for stakeholders and recruiters.
5. **Containerization & CI/CD:** Orchestrated the entire stack using **Docker & Docker Compose** for consistent deployment, backed by a **GitHub Actions** pipeline for automated smoke testing.

---

## 4. System Architecture

```
                   [ High-Frequency IoT Sensors ]
                                 │
                                 ▼
                   +-----------------------------+
                   |  FastAPI Ingestion Engine   |
                   |   (Validation & Routing)    |
                   +-----------------------------+
                     /                         \
                    /                           \
                   ▼                             ▼
         +-------------------+         +-------------------+
         |   PostgreSQL DB   |         |  ChromaDB Vector  |
         | (Telemetry Logs & |         | (Indexed SOPs &   |
         | Shipment States)  |         | Directive FRU-02) |
         +-------------------+         +-------------------+
                                                 │
                                                 ▼
                                       +-------------------+
                                       | Ollama LLM Engine |
                                       | (RAG Reasoning)   |
                                       +-------------------+
                                                 │
                                                 ▼
                                       +-------------------+
                                       | Actionable Output |
                                       | (Mitigation Plan) |
                                       +-------------------+

```

---

## 5. Technology Stack

* **Backend & API:** FastAPI, Uvicorn, Pydantic, Jinja2
* **Database & ORM:** PostgreSQL, SQLAlchemy
* **AI & Vector Search:** ChromaDB, Ollama (Local LLM)
* **Frontend UI:** Streamlit
* **DevOps & CI/CD:** Docker, Docker Compose, GitHub Actions

---

## 6. Primary API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/shipments` | Retrieves all active shipments, current spatial/thermal readings, and risk alerts. |
| `POST` | `/telemetry` | Ingests live IoT sensor metrics (`temperature`, `humidity`, `gps_lat`, `gps_lng`) with strict typing. |
| `POST` | `/copilot/evaluate` | Evaluates a specific shipment excursion using local RAG and returns recommended SOP steps. |
| `GET` | `/health` | Live readiness probe endpoint used by container orchestrators and CI/CD pipelines. |

---

## 7. Local Setup & Quickstart

### Prerequisites

* [Docker Engine](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/)
* Python 3.10+
* Git

### Installation Steps

1. **Clone the repository:**

```bash
git clone https://github.com/poornima1508/cold-chain-logistics-fde-project.git
cd cold-chain-logistics-fde-project

```

2. **Launch Full Docker Stack (FastAPI + PostgreSQL + ChromaDB + Ollama):**

```bash
docker-compose up -d --build

```

3. **Run the Streamlit Frontend Locally:**

```bash
pip install -r requirements.txt
streamlit run app/frontend.py

```

4. **Access the Application:**

* **API Documentation (Swagger):** `http://localhost:8000/docs`
* **Interactive UI:** `http://localhost:8501` (or via the [Live Cloud Demo](https://cold-chain-logistics-fde-project.streamlit.app/))
