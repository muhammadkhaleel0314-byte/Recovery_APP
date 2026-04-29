import streamlit as st

st.set_page_config(page_title="Quick Dashboard", layout="wide")

# ----------- HEADER -----------
st.markdown("""
<h1 style='text-align:center; font-size:42px; color:white;'>
🚀 Quick Access Dashboard
</h1>
<p style='text-align:center; color:#cfcfcf; font-size:18px;'>
All your important tools in one place
</p>
""", unsafe_allow_html=True)

# ----------- CSS -----------
st.markdown("""
<style>

/* BACKGROUND */
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* GRID */
.grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(220px,1fr));
    gap:20px;
    margin-top:30px;
}

/* CARD */
.card {
    padding:30px;
    border-radius:16px;
    text-align:center;
    font-weight:bold;
    font-size:17px;
    transition:0.25s;
    backdrop-filter: blur(12px);
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.2);
    color:white;
}

/* HOVER EFFECT */
.card:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 12px 30px rgba(0,0,0,0.35);
}

/* LINKS */
a {
    text-decoration:none;
    color:inherit;
}

/* TICKER */
.ticker {
    margin-top:40px;
    overflow:hidden;
    background:black;
    color:white;
    padding:16px;
    border-radius:12px;
}

.ticker-text {
    display:inline-block;
    white-space:nowrap;
    padding-left:100%;
    animation: scroll 20s linear infinite;
    font-size:20px;
    font-weight:700;
    letter-spacing:1px;
}

/* ANIMATION */
@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

/* FOOTER */
.footer {
    margin-top:40px;
    text-align:center;
    color:#cfcfcf;
    font-size:14px;
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

# ----------- GRID BOXES -----------
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank"><div class="card">📊 PMY Verify Data</div></a>

<a href="{link2}" target="_blank"><div class="card">🏦 BOP Account</div></a>

<a href="{link3}" target="_blank"><div class="card">📁 ACAG Batch Data</div></a>

<a href="{link4}" target="_blank"><div class="card">📲 PMY Apply & Track</div></a>

<a href="{link5}" target="_blank"><div class="card">📝 ACAG Apply</div></a>

<a href="{link6}" target="_blank"><div class="card">🚧 QR Generator</div></a>

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

# ----------- FOOTER -----------
st.markdown("""
<div class="footer">
    <hr>
    Made by Khaleel 🚀
</div>
""", unsafe_allow_html=True)
