import streamlit as st

st.set_page_config(page_title="Quick Dashboard", layout="wide")

st.title("🚀 My Quick Link's Dashboard")

# ----------- SESSION STATE MESSAGE -----------
if "msg" not in st.session_state:
    st.session_state.msg = ""

# ----------- CSS -----------
st.markdown("""
<style>

.grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(200px,1fr));
    gap:18px;
}

.card {
    padding:26px;
    border-radius:14px;
    text-align:center;
    font-weight:600;
    font-size:16px;
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
    cursor:pointer;
}

/* COLORS */
.c1 { background:#f1f3f5; color:#111; }
.c2 { background:#ffe066; color:#111; }
.c3 { background:#868e96; color:white; }
.c4 { background:#40c057; color:white; }
.c5 { background:#339af0; color:white; }
.c6 { background:#ff6b6b; color:white; }

</style>
""", unsafe_allow_html=True)

# ----------- LINKS -----------
link1 = "https://script.google.com/macros/s/AKfycbyCr-KxEdrWdLhHXYWMLcDdK1Viciar6yJtQsaQNPFuY-X9IK41GkOiRvkV64PbatE9Kg/exec"
link2 = "https://script.google.com/macros/s/AKfycbzPaNIURbCJLA8iNRm3RA6v2OS5WlxaMURw0IIjcwLnLvBPlVJ9DJG7KxihITJ6g6mb/exec"
link3 = "https://script.google.com/macros/s/AKfycbzTMdTGQczpfnWd76rdwhj1rr_4DCMTMITYFgJZBcGrDbBSQZIHKu3mTkaXYnB5Y9VZew/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"

# ----------- BUTTONS GRID -----------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 PMY Verify Data"):
        st.write(f"Open: {link1}")

with col2:
    if st.button("🏦 BOP Account"):
        st.write(f"Open: {link2}")

with col3:
    if st.button("📁 ACAG Batch Data"):
        st.write(f"Open: {link3}")

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("📲 PMY Apply & Track"):
        st.write(f"Open: {link4}")

with col5:
    if st.button("📝 ACAG Apply"):
        st.write(f"Open: {link5}")

with col6:
    if st.button("🚧 QR Generator"):
        st.session_state.msg = "❌ You can not use this option"

# ----------- MESSAGE SHOW -----------
if st.session_state.msg:
    st.error(st.session_state.msg)
