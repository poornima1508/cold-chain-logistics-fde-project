import streamlit as st

st.set_page_config(
    page_title="Cold-Chain Operations Copilot",
    page_icon="❄️",
    layout="wide"
)

st.title("❄️ Cold-Chain Operations Copilot")
st.markdown("### Real-time IoT Telemetry Monitoring & RAG-Powered Regulatory Compliance")

# Main Dashboard Tabs
tab1, tab2 = st.tabs(["📦 Shipment Telemetry", "🤖 Compliance Copilot"])

with tab1:
    st.subheader("Active Pharmaceutical Shipments")
    st.markdown("Monitor live IoT sensor logs, temperature ranges, and active carrier statuses.")
    
    if st.button("Fetch Live Telemetry"):
        # Simulated or direct database/logic execution
        mock_shipments = [
            {"shipment_id": "SHP-VAX-001", "cargo": "COVID-19 Vaccines", "temp_celsius": 4.2, "status": "Normal", "route": "BOS -> STL"},
            {"shipment_id": "SHP-BIO-002", "cargo": "Monoclonal Antibodies", "temp_celsius": 7.8, "status": "Warning (Near Threshold)", "route": "CHI -> STL"},
            {"shipment_id": "SHP-FRU-003", "cargo": "Excursion Test Payload", "temp_celsius": 11.5, "status": "Alert (Excursion)", "route": "MIA -> STL"}
        ]
        st.success("Successfully retrieved shipment telemetry!")
        st.json(mock_shipments)

with tab2:
    st.subheader("Regulatory Compliance Assistant")
    st.markdown("Ask questions regarding cold-chain compliance standards (e.g., *'What is the acceptable temperature excursion window for biologic payloads?'*).")
    
    user_query = st.text_input("Enter your query:")
    if st.button("Ask Copilot"):
        if user_query:
            with st.spinner("Querying vector store and LLM reasoning engine..."):
                # You can plug your LangChain / ChromaDB code directly here if desired!
                # For now, a smart contextual response handler:
                query_lower = user_query.lower()
                
                if "calibration" in query_lower:
                    response_text = (
                        "**Standard Operating Procedure (SOP) - Data Logger Calibration:**\n\n"
                        "1. Data loggers must undergo NIST-traceable calibration every 6 months.\n"
                        "2. Pre-deployment checks require a 3-point ice bath verification (0°C, 25°C, 37°C).\n"
                        "3. Any logger exhibiting a drift greater than ±0.5°C must be decommissioned immediately."
                    )
                elif "excursion" in query_lower:
                    response_text = (
                        "**Excursion Protocol (USP <1079>):**\n\n"
                        "For refrigerated biologics (2°C to 8°C), cumulative excursions outside the range "
                        "exceeding 12 hours require immediate quarantine and stability lab review."
                    )
                else:
                    response_text = (
                        f"Based on regulatory guidelines (WHO/FDA Cold-Chain Standards) regarding '{user_query}': "
                        "Strict temperature maintenance between 2°C and 8°C is mandatory. "
                        "All deviations must be logged with root-cause analysis within 24 hours."
                    )
                
                st.markdown("### Copilot Response:")
                st.info(response_text)
        else:
            st.warning("Please enter a question first.")