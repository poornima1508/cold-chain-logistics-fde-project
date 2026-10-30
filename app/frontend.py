import streamlit as st
import requests

st.set_page_config(
    page_title="Cold-Chain Operations Copilot",
    page_icon="❄️",
    layout="wide"
)

st.title("❄️ Cold-Chain Operations Copilot")
st.markdown("### Real-time IoT Telemetry Monitoring & RAG-Powered Regulatory Compliance")

# Sidebar for navigation or settings
st.sidebar.header("Configuration")
default_url = st.secrets.get("BACKEND_URL", "http://localhost:8000")
api_base_url = st.sidebar.text_input("FastAPI Backend URL", value=default_url)

# Main Dashboard Tabs
tab1, tab2 = st.tabs(["📦 Shipment Telemetry", "🤖 Compliance Copilot"])

with tab1:
    st.subheader("Active Pharmaceutical Shipments")
    if st.button("Fetch Live Telemetry"):
        try:
            response = requests.get(f"{api_base_url}/shipments")
            if response.status_code == 200:
                shipments = response.json()
                st.success("Successfully retrieved shipment telemetry!")
                st.json(shipments)
            else:
                st.error(f"Error fetching data: Status code {response.status_code}")
        except Exception as e:
            st.error(f"Could not connect to FastAPI backend: {e}")

with tab2:
    st.subheader("Regulatory Compliance Assistant")
    st.markdown("Ask questions regarding cold-chain compliance standards (e.g., *'What is the acceptable temperature excursion window for biologic payloads?'*).")
    
    user_query = st.text_input("Enter your query:")
    if st.button("Ask Copilot"):
        if user_query:
            with st.spinner("Querying vector store and LLM reasoning engine..."):
                try:
                    payload = {"prompt": user_query}
                    res = requests.post(f"{api_base_url}/query", json=payload)
                    if res.status_code == 200:
                        st.markdown("### Copilot Response:")
                        data = res.json()
                        
                        # Look for common key variations returned by the backend
                        answer = data.get("response") or data.get("copilot_analysis") or data.get("result") or data.get("answer")
                        
                        if answer:
                            st.info(answer)
                        else:
                            # Fallback to display the raw JSON if it uses a custom key
                            st.json(data)
                    else:
                        st.warning("Connected to backend, but query route returned an unexpected status. Make sure your `/query` endpoint is defined.")
                except Exception as e:
                    st.error(f"Connection failed: {e}")
        else:
            st.warning("Please enter a question first.")