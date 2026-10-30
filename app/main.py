import os
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Shipment, TelemetryLog
from app.agent import run_copilot_reasoning

app = FastAPI(
    title="Cold-Chain Operations Copilot API",
    description="FDE-style logistics & telemetry monitoring product with UI and Vector RAG",
    version="3.0.0",
)

# Robust absolute pathing for templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

class CopilotQuery(BaseModel):
    prompt: str
    shipment_code: str = None


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serve the end-to-end product dashboard UI."""
    return templates.TemplateResponse(request, "index.html", {"request": request})


@app.get("/shipments")
def get_shipments(db: Session = Depends(get_db)):
    """Retrieve all tracked shipments and their current statuses."""
    shipments = db.query(Shipment).all()
    return [
        {
            "id": s.id,
            "shipment_code": s.shipment_code,
            "product_type": s.product_type,
            "origin": s.origin,
            "destination": s.destination,
            "status": s.status
        }
        for s in shipments
    ]


@app.get("/shipments/{shipment_id}/telemetry")
def get_shipment_telemetry(shipment_id: int, db: Session = Depends(get_db)):
    """Retrieve shipment details along with all historical telemetry and anomaly flags."""
    shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")

    return {
        "shipment_code": shipment.shipment_code,
        "product": shipment.product_type,
        "status": shipment.status,
        "origin": shipment.origin,
        "destination": shipment.destination,
        "telemetry_logs": [
            {
                "timestamp": log.timestamp,
                "temperature_celsius": log.temperature_celsius,
                "humidity_percent": log.humidity_percent,
                "anomaly_flag": log.anomaly_flag,
                "notes": log.notes,
            }
            for log in shipment.telemetry
        ],
    }


@app.post("/copilot/analyze")
def analyze_shipment_with_copilot(query: CopilotQuery):
    """Run local AI reasoning augmented with SQL database telemetry and ChromaDB vector compliance context."""
    try:
        analysis = run_copilot_reasoning(prompt=query.prompt, shipment_code=query.shipment_code)
        return {
            "shipment_code": query.shipment_code,
            "prompt": query.prompt,
            "copilot_analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query")
def query_alias(query: CopilotQuery):
    """Alias endpoint for /query to gracefully support frontends looking for /query."""
    return analyze_shipment_with_copilot(query)