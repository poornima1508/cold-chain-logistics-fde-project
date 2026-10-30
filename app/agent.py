import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Shipment, TelemetryLog, AuditLog
from app.vector_store import get_vector_store

load_dotenv()

ollama_model = os.getenv("OLLAMA_MODEL", "llama3")
llm = OllamaLLM(model=ollama_model, base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))

def query_shipment_status(db: Session, shipment_code: str):
    shipment = db.query(Shipment).filter(Shipment.shipment_code == shipment_code).first()
    if not shipment:
        return f"Shipment {shipment_code} not found in database.", None
    
    logs_summary = []
    for log in shipment.telemetry:
        status_label = "BREACH" if log.anomaly_flag == 1 else "Normal"
        logs_summary.append(
            f"- Time: {log.timestamp}, Temp: {log.temperature_celsius}°C, Humidity: {log.humidity_percent}%, Status: {status_label}, Notes: {log.notes}"
        )
    
    context = f"""
    Shipment Code: {shipment.shipment_code}
    Product: {shipment.product_type}
    Status: {shipment.status}
    Route: {shipment.origin} -> {shipment.destination}
    Telemetry History:
    """ + "\n".join(logs_summary)
    
    return context, shipment

def search_compliance_protocols(query: str):
    vector_store = get_vector_store()
    results = vector_store.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in results])

def run_copilot_reasoning(prompt: str, shipment_code: str = None):
    db: Session = SessionLocal()
    try:
        db_context = ""
        shipment_obj = None
        if shipment_code:
            db_context, shipment_obj = query_shipment_status(db, shipment_code)
        
        compliance_context = search_compliance_protocols(prompt)
        
        system_prompt = f"""
        You are an expert Cold-Chain Operations Copilot for a Forward Deployed Engineering team.
        Your job is to analyze temperature logs, cross-reference them with official compliance regulations,
        and provide actionable, protocol-backed logistics recommendations.

        Official Compliance Guidelines (From Vector DB):
        {compliance_context}

        Live Database Telemetry Context:
        {db_context}

        User Prompt: {prompt}
        """
        
        response = llm.invoke(system_prompt)

        # Persist audit log entry for enterprise governance
        audit_entry = AuditLog(
            shipment_id=shipment_obj.id if shipment_obj else None,
            operator_prompt=prompt,
            retrieved_compliance_context=compliance_context,
            copilot_response=response
        )
        db.add(audit_entry)
        db.commit()

        return response
    finally:
        db.close()