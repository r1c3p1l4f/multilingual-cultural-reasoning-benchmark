import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit as st
import json
from datetime import datetime
import os

# --- Authentication setup ---
# Load credentials and cookie settings from Streamlit secrets
credentials = {
    "usernames": {
        username: {
            "email": email,
            "name": name,
            "password": hash
        } for username, email, name, hash in zip(
            st.secrets["credentials"]["usernames"],
            st.secrets["credentials"]["emails"],
            st.secrets["credentials"]["names"],
            st.secrets["credentials"]["password_hashes"]
        )
    }
}

cookie = {
    "name": st.secrets["cookie"]["name"],
    "key": st.secrets["cookie"]["key"],
    "expiry_days": st.secrets["cookie"]["expiry_days"]
}

authenticator = stauth.Authenticate(
    credentials, cookie["name"], cookie["key"], cookie["expiry_days"]
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("Username/password is incorrect")
    st.stop()
elif authentication_status is None:
    st.warning("Please enter your username and password")
    st.stop()

st.set_page_config(page_title="Cultural Reasoning Benchmark", layout="wide")
st.title("🧠 Multilingual Cultural Reasoning Benchmark")

st.markdown("""
This tool lets you score language model outputs for cultural reasoning using a consistent rubric. 
After scoring, each result is exported as a JSONL row for downstream analysis.
""")

# --- Prompt metadata inputs ---
with st.sidebar:
    st.header("📄 Metadata")
    model = st.text_input("Model Name", placeholder="e.g., qwen-3-8b")
    culture = st.selectbox("Cultural Context", ["Japanese", "Zulu", "German", "American", "Chinese", "Thai", "Arabic", "Other"])
    prompt_variant = st.text_input("Prompt Variant (optional)")
    include_trace = st.checkbox("Includes CoT / planner trace")
    planner_visible = st.radio("Planner Visibility", ["Yes", "No"], index=1)

st.subheader("📜 Model Output")
model_output = st.text_area("Paste full model output here", height=300)

# --- Rubric scoring ---
st.subheader("📊 Rubric")
col1, col2, col3 = st.columns(3)
with col1:
    cultural_score = st.slider("Cultural Fidelity", 1, 5, 3)
    responsibility_score = st.slider("Responsibility Framing", 1, 5, 3)
with col2:
    emotional_score = st.slider("Emotional Tone Alignment", 1, 5, 3)
    usefulness_score = st.slider("Practical Usefulness", 1, 5, 3)
with col3:
    metaphor_score = st.slider("Cultural Vocabulary / Metaphors", 1, 5, 3)

notes = st.text_area("📝 Notes / Observations", height=150)

# --- Save result ---
if "jsonl_rows" not in st.session_state:
    st.session_state.jsonl_rows = []

if st.button("✅ Add to Dataset"):
    row = {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "culture": culture,
        "prompt_variant": prompt_variant,
        "includes_trace": include_trace,
        "planner_visible": planner_visible == "Yes",
        "cultural_score": cultural_score,
        "responsibility_score": responsibility_score,
        "emotional_score": emotional_score,
        "usefulness_score": usefulness_score,
        "metaphor_score": metaphor_score,
        "notes": notes,
        "output": model_output
    }
    # Append to file for persistence
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "benchmark_outputs.jsonl")
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    st.session_state.jsonl_rows.append(row)
    st.success("Scored output added to dataset ✅")

if st.session_state.jsonl_rows:
    st.subheader("📥 Export Dataset")
    file_name = f"benchmark_outputs_{datetime.now().strftime('%Y%m%d_%H%M')}.jsonl"
    jsonl_data = "\n".join(json.dumps(row) for row in st.session_state.jsonl_rows)
    st.download_button("⬇️ Download JSONL", jsonl_data, file_name, mime="application/json")

authenticator.logout("Logout", "sidebar")
