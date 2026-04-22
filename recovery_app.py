import streamlit as st

st.set_page_config(page_title="My Quick Link's Dashboard", layout="wide")

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
    padding:28px;
    border-radius:15px;
    text-align:center;
    font-weight:bold;
    font-size:10px;
    transition:1.9s;
    box-shadow:0 6px 15px rgba(0,0,0,0.15);
}

/* HOVER */
.card:hover {
    transform: translateY(-6px) scale(1.04);
}

/* COLORS */
.c1 { background:#f8f9fa; color:black; }
.c2 { background:#ffd54f; color:black; }
.c3 { background:#9e9e9e; color:white; }
.c4 { background:#4caf50; color:white; }
.c5 { background:#2196f3; color:white; }
.c6 { background:#ff5722; color:white; }

/* LINKS */
a {
    text-decoration:none;
    color:inherit;
}

/* TICKER */
.ticker {
    margin-top:30px;
    overflow:hidden;
    background:black;
    color:white;
    padding:12px;
    border-radius:10px;
}

.ticker-text {
    display:inline-block;
    white-space:nowrap;
    padding-left:100%;
    animation: scroll 30s linear infinite;
    font-size:20px;
    font-weight:1000;
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

# ----------- CLEAN TICKER (FIXED) -----------
st.markdown("""
<div class="ticker">
    <div class="ticker-text">
        🔴  
        You don’t realize the weight of something until it’s no longer yours.”
“People change, not because they want to, but because life leaves them no choice.”
“The hardest battles are fought in the mind, where no one can see.” 
        🌍  |
    </div>
</div>
""", unsafe_allow_html=True)
