# Cold-Chain Operations Copilot

### Real-Time IoT Telemetry Monitoring & AI-Powered Regulatory Compliance

**Live Demo:** [https://cold-chain-logistics-fde-project.streamlit.app/](https://cold-chain-logistics-fde-project.streamlit.app/)

---

## 1. What This Project Is About

When shipping sensitive items like vaccines, biologics, or perishable food, keeping the right temperature is critical. If a truck or cargo container gets too warm, millions of dollars in medical supplies can be ruined instantly.

Most logistics systems only record temperatures locally on data loggers. That means operators usually find out a shipment spoiled *after* it reaches its destination—when it is too late to fix it.

This project is a complete prototype built to solve that problem. It combines **live IoT sensor tracking** with an **AI compliance assistant** so logistics teams can catch temperature spikes immediately and know exactly what rules to follow to save the cargo.

---

## 2. Who Is This For?

* **Fleet Operators:** People monitoring active shipments who need instant alerts if a container's temperature or location goes out of bounds.
* **Quality Assurance (QA) Officers:** Teams responsible for following strict regulatory standards (like USP guidelines) who need quick answers during a thermal emergency instead of digging through 100-page rulebooks.

---

## 3. What I Built (The Engineering Work)

As the developer on this project, I handled the end-to-end implementation to make sure it functions as a reliable, production-ready tool:

1. **Self-Contained Frontend UI:** Built an interactive dashboard using **Streamlit** so anyone can open the app instantly in a browser and test the telemetry or compliance features without complex server setups.
2. **Telemetry Data Handling:** Structured data models using **Pydantic** to validate incoming IoT metrics (temperatures, GPS coordinates, humidity, and timestamps) and flag excursion risks in real time.
3. **RAG-Powered Compliance Assistant:** Built a retrieval system that indexes official regulatory documents and standard operating procedures (SOPs). When a temperature alarm triggers, the assistant reads the rules and generates a clear, step-by-step recovery plan.
4. **Cloud Deployment:** Packaged and deployed the entire application to the public cloud so it is instantly accessible for reviews and recruiter demos.

---

## 4. Key Features & How They Work

| Tab / Feature | What It Does |
| --- | --- |
| **📦 Shipment Telemetry** | Displays active shipments, live temperatures, route details (e.g., Boston to St. Louis), and flags whether cargo is normal, near a threshold, or in excursion alert. |
| **🤖 Compliance Copilot** | A search box where users can ask compliance questions (like *"How long can refrigerated vaccines stay outside the 2°C to 8°C range?"*) and get instant answers grounded in standard operating procedures. |

---

## 5. Technology Stack

* **Frontend & Logic:** Streamlit, Python
* **Data Validation & Modeling:** Pydantic, SQLAlchemy
* **AI & Search:** Vector storage concepts and local reasoning logic for regulatory manuals
* **Deployment & CI/CD:** Streamlit Community Cloud, GitHub Actions
