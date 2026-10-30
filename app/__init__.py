from app.database import Base, engine
from app.models import Shipment, TelemetryLog

def init_database():
    print("Creating database tables in PostgreSQL...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    init_database()