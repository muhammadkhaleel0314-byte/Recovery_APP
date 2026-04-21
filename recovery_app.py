import streamlit as st

st.set_page_config(page_title="Smart Dashboard", layout="wide")

st.title("🚀 Smart Dashboard")

# ----------- CSS -----------
st.markdown("""
<style>

/* GRID */
.grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(200px,1fr));
    gap:18px;
}

/* CARD STYLE */
.card {
    padding:28px;
    border-radius:18px;
    text-align:center;
    font-weight:bold;
    font-size:17px;
    transition:0.3s;
    box-shadow:0 6px 18px rgba(0,0,0,0.15);
}

/* HOVER */
.card:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow:0 12px 25px rgba(0,0,0,0.3);
}

/* 🎨 IMPROVED COLORS */
.c1 { background:#f5f5f5; color:black; }
.c2 { background:#ffd54f; color:black; }
.c3 { background:#757575; color:white; }
.c4 { background:linear-gradient(135deg,#00c853,#64dd17); color:white; }
.c5 { background:linear-gradient(135deg,#00b0ff,#2962ff); color:white; }
.c6 { background:linear-gradient(135deg,#ff6f00,#ff1744); color:white; }

/* REMOVE LINK STYLE */
a {
    text-decoration:none;
    color:inherit;
}

/* 🎬 TICKER */
.ticker {
    margin-top:30px;
    overflow:hidden;
    background:black;
    color:white;
    padding:12px;
    border-radius:12px;
}

.ticker-text {
    display:inline-block;
    padding-left:100%;
    animation: scroll 20s linear infinite;
    font-size:18px;
    font-weight:bold;
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
link6 = "#"

# ----------- BOXES -----------
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank"><div class="card c1">📊 PMY Verify Data</div></a>
<a href="{link2}" target="_blank"><div class="card c2">🏦 BOP Account</div></a>
<a href="{link3}" target="_blank"><div class="card c3">📁 ACAG Batch Data</div></a>
<a href="{link4}" target="_blank"><div class="card c4">📲 PMY Apply & Track</div></a>
<a href="{link5}" target="_blank"><div class="card c5">📝 ACAG Apply</div></a>
<a href="{link6}" target="_blank"><div class="card c6">🚧 RDC (Coming Soon)</div></a>

</div>
""", unsafe_allow_html=True)

# ----------- RUNNING TEXT -----------
st.markdown("""
<div class="ticker">
    <div class="ticker-text">
        🇵🇰 Pakistan Zindabad 🇵🇰 | 💚 Pak Army Zindabad 💚 | 🌙 Pakistan Our Pride |
        🕌 Unity • Faith • Discipline | 🤝 Strong Nation Strong Future |
        🇵🇰 We Love Pakistan 🇵🇰
    </div>
</div>
""", unsafe_allow_html=True)
