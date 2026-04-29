import streamlit as st

st.set_page_config(page_title="Quick Dashboard", layout="wide")

st.title("🚀 My Quick Link's Dashboard")

# ----------- CSS -----------
st.markdown("""
<style>

/* GRID */
.grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(200px,1fr));
    gap:18px;
}

/* CARD */
.card {
    padding:26px;
    border-radius:14px;
    text-align:center;
    font-weight:600;
    font-size:16px;
    transition:0.2s;
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* HOVER */
.card:hover {
    transform: translateY(-5px);
    box-shadow:0 10px 22px rgba(0,0,0,0.2);
}

/* COLORS (slightly modern tones) */
.c1 { background:#f1f3f5; color:#111; }
.c2 { background:#ffe066; color:#111; }
.c3 { background:#868e96; color:white; }
.c4 { background:#40c057; color:white; }
.c5 { background:#339af0; color:white; }
.c6 { background:#ff6b6b; color:white; }

/* LINKS */
a {
    text-decoration:none;
    color:inherit;
}

/* TICKER */
.ticker {
    margin-top:30px;
    overflow:hidden;
    background:#111;
    color:white;
    padding:14px;
    border-radius:10px;
}

.ticker-text {
    display:inline-block;
    white-space:nowrap;
    padding-left:100%;
    animation: scroll 25s linear infinite;
    font-size:18px;
    font-weight:600;
}

/* ANIMATION */
@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

</style>
""", unsafe_allow_html=True)

# ----------- LINKS -----------
link1 = "https://script.google.com/macros/s/AKfycbyCr-KxEdrWdLhHXYWMLcDdK1Viciar6yJtQsaQNPFuY-X9IK41GkOiRvkV64PbatE9Kg/exec"
link2 = "https://script.google.com/macros/s/AKfycbzPaNIURbCJLA8iNRm3RA6v2OS5WlxaMURw0IIjcwLnLvBPlVJ9DJG7KxihITJ6g6mb/exec"
link3 = "https://script.google.com/macros/s/AKfycbzTMdTGQczpfnWd76rdwhj1rr_4DCMTMITYFgJZBcGrDbBSQZIHKu3mTkaXYnB5Y9VZew/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"

# ----------- BOXES -----------
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank"><div class="card c1">📊 PMY Verify Data</div></a>
<a href="{link2}" target="_blank"><div class="card c2">🏦 BOP Account</div></a>
<a href="{link3}" target="_blank"><div class="card c3">📁 ACAG Batch Data</div></a>
<a href="{link4}" target="_blank"><div class="card c4">📲 PMY Apply & Track</div></a>
<a href="{link5}" target="_blank"><div class="card c5">📝 ACAG Apply</div></a>
<a href="{link6}" target="_blank"><div class="card c6">🚧 QR Generator</div></a>

</div>
""", unsafe_allow_html=True)

# ----------- TICKER -----------
st.markdown("""
<div class="ticker">
    <div class="ticker-text">
        🔴 Silence is the best answer for all questions | 😊 Smiling is the best reaction in every situation 🌍
    </div>
</div>
""", unsafe_allow_html=True)
