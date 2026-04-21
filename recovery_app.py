import streamlit as st

st.set_page_config(page_title="My Quick Link's Dashboard", layout="wide")

st.title("🚀 Smart Dashboard")

# ----------- CSS -----------
st.markdown("""
<style>

/* Card */
.card {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-weight: bold;
    transition: 0.3s;
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.card:hover {
    transform: scale(1.05);
}

/* Grid */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px,1fr));
    gap: 15px;
}

/* 🎬 TICKER STYLE */
.ticker {
    margin-top: 30px;
    overflow: hidden;
    white-space: nowrap;
    box-sizing: border-box;
    background: black;
    color: white;
    padding: 10px 0;
    border-radius: 10px;
}

/* Moving text */
.ticker-text {
    display: inline-block;
    padding-left: 100%;
    animation: scrollText 20s linear infinite;
    font-size: 18px;
    font-weight: bold;
}

/* Animation */
@keyframes scrollText {
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
link6 = "#"

# ----------- BOXES -----------

st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank"><div class="card">📊 PMY Verify Data</div></a>
<a href="{link2}" target="_blank"><div class="card">🏦 BOP Account</div></a>
<a href="{link3}" target="_blank"><div class="card">📁 ACAG Batch Data</div></a>
<a href="{link4}" target="_blank"><div class="card">📲 PMY Apply</div></a>
<a href="{link5}" target="_blank"><div class="card">📝 ACAG Apply</div></a>
<a href="{link6}" target="_blank"><div class="card">🚧 RDC</div></a>

</div>
""", unsafe_allow_html=True)

# ----------- TICKER (FLAGS + TEXT) -----------

st.markdown("""
<div class="ticker">
    <div class="ticker-text">
        🇵🇰 Pakistan Zindabad 🇵🇰 &nbsp;&nbsp;&nbsp;
        🇮🇷 Iran Zindabad 🇮🇷 &nbsp;&nbsp;&nbsp;
        🇵🇸 Palestine Zindabad 🇵🇸 &nbsp;&nbsp;&nbsp;
        🔴 Breaking: New Updates Coming Soon... &nbsp;&nbsp;&nbsp;
        📢 System Running Smoothly &nbsp;&nbsp;&nbsp;
    </div>
</div>
""", unsafe_allow_html=True)
