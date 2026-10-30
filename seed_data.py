from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models import Shipment, TelemetryLog

def seed():
    db = SessionLocal()

    # Check if we already seeded
    if db.query(Shipment).first():
        print("Database already contains data!")
        db.close()
        return

    print("Seeding sample cold-chain data...")

    # Shipment 1: Vaccines (Strict cold-chain: 2°C to 8°C)
    shipment1 = Shipment(
        shipment_code="SHP-VAX-001",
        origin="Boston Hub",
        destination="Chicago Clinic",
        product_type="Pfizer Vaccines",
        status="In Transit"
    )

    # Shipment 2: Fresh Produce (Allowed range: 4°C to 12°C)
    shipment2 = Shipment(
        shipment_code="SHP-FRU-002",
        origin="Miami Port",
        destination="Atlanta Distribution",
        product_type="Organic Strawberries",
        status="Alert"
    )

    db.add_all([shipment1, shipment2])
    db.commit()

    # Add telemetry logs for Shipment 1 (Normal)
    log1 = TelemetryLog(
        shipment_id=shipment1.id,
        temperature_celsius=4.5,
        humidity_percent=45.0,
        gps_lat=42.3601,
        gps_lng=-71.0589,
        anomaly_flag=0,
        notes="Temperature optimal within cold chain specifications."
    )

    # Add telemetry logs for Shipment 2 (Breach!)
    log2 = TelemetryLog(
        shipment_id=shipment2.id,
        temperature_celsius=14.2,  # Breach! Too warm for strawberries
        humidity_percent=88.5,
        gps_lat=25.7617,
        gps_lng=-80.1918,
        anomaly_flag=1,
        notes="WARNING: Temperature excursion detected in compartment B."
    )

    db.add_all([log1, log2])
    db.commit()
    db.close()
    print("Seed data inserted successfully!")

if __name__ == "__main__":
    seed()
