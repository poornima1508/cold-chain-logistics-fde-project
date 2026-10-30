from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    shipment_code = Column(String, unique=True, index=True)
    product_type = Column(String)
    origin = Column(String)
    destination = Column(String)
    status = Column(String, default="In Transit")

    telemetry = relationship("TelemetryLog", back_populates="shipment", cascade="all, delete-orphan")
    audits = relationship("AuditLog", back_populates="shipment", cascade="all, delete-orphan")

class TelemetryLog(Base):
    __tablename__ = "telemetry_logs"

    id = Column(Integer, primary_key=True, index=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    temperature_celsius = Column(Float)
    humidity_percent = Column(Float)
    anomaly_flag = Column(Integer, default=0) # 0 = Normal, 1 = Breach
    gps_lat = Column(Float, nullable=True)
    gps_lng = Column(Float, nullable=True)
    notes = Column(String, nullable=True)

    shipment = relationship("Shipment", back_populates="telemetry")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    operator_prompt = Column(Text)
    retrieved_compliance_context = Column(Text)
    copilot_response = Column(Text)

    shipment = relationship("Shipment", back_populates="audits")