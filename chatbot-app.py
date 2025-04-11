import streamlit as st
import requests

# --- Config ---
OLLAMA_BASE_URL = "https://your-unique-subdomain.trycloudflare.com"  # or your tunnel domain
TAGS_URL = f"{OLLAMA_BASE_URL}/api/tags"
GENERATE_URL = f"{OLLAMA_BASE_URL}/api/generate"

# --- Page Settings ---
st.set_page_config(page_title="Ollama Chat", layout="centered")
st.title("🧠 Ollama Chat Interface")

# --- Fetch Models ---
@st.cache_data
def fetch_models():
    try:
        response = requests.get(TAGS_URL)
        if response.status_code == 200:
            data = response.json()
            models = [model["name"] for model in data.get("models", [])]
            return models
        else:
            st.error(f"Failed to fetch models: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error fetching models: {e}")
        return []

# --- UI: Select Model ---
models = fetch_models()
if not models:
    st.warning("No models available. Please load a model into Ollama.")
    st.stop()

selected_model = st.selectbox("📦 Choose a model:", models)

# --- UI: Prompt Input ---
prompt = st.text_area("💬 Enter your prompt:", height=200)

if st.button("🚀 Generate Response"):
    if not prompt.strip():
        st.warning("Prompt cannot be empty.")
    else:
        with st.spinner("Generating response..."):
            payload = {
                "model": selected_model,
                "prompt": prompt,
                "stream": False
            }
            try:
                response = requests.post(GENERATE_URL, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    st.markdown("### ✅ Response")
                    st.write(result.get("response", "No response received."))
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
