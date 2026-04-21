import streamlit as st

st.set_page_config(page_title="Smart Dashboard", layout="wide")

st.title("🚀 Smart Dashboard")

# ----------- CSS -----------
st.markdown("""
<style>

/* Background */
body {
    background: linear-gradient(135deg, #141E30, #243B55);
}

/* Card Style */
.card {
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.4s;

    backdrop-filter: blur(10px);
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);

    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}

/* Hover */
.card:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 15px 35px rgba(0,0,0,0.5);
}

/* 🎬 Animation */
@keyframes fadeUp {
    from {opacity:0; transform: translateY(60px);}
    to {opacity:1; transform: translateY(0);}
}

/* Stagger */
.c1 {animation: fadeUp 0.8s ease 0.2s forwards; opacity:0;}
.c2 {animation: fadeUp 0.8s ease 0.5s forwards; opacity:0;}
.c3 {animation: fadeUp 0.8s ease 0.8s forwards; opacity:0;}
.c4 {animation: fadeUp 0.8s ease 1.1s forwards; opacity:0;}
.c5 {animation: fadeUp 0.8s ease 1.4s forwards; opacity:0;}
.c6 {animation: fadeUp 0.8s ease 1.7s forwards; opacity:0;}

/* Colors */
.c1 {background:#ffffff; color:black;}
.c2 {background:#FFD700; color:black;}
.c3 {background:#777; color:white;}
.c4 {background:linear-gradient(135deg,#11998e,#38ef7d); color:white;}
.c5 {background:linear-gradient(135deg,#36d1dc,#5b86e5); color:white;}
.c6 {background:linear-gradient(135deg,#ff512f,#dd2476); color:white;}

/* Remove link style */
a {text-decoration:none; color:inherit;}

</style>
""", unsafe_allow_html=True)

# ----------- LINKS -----------
link1 = "https://script.google.com/macros/s/AKfycbyCr-KxEdrWdLhHXYWMLcDdK1Viciar6yJtQsaQNPFuY-X9IK41GkOiRvkV64PbatE9Kg/exec"
link2 = "https://script.google.com/macros/s/AKfycbzPaNIURbCJLA8iNRm3RA6v2OS5WlxaMURw0IIjcwLnLvBPlVJ9DJG7KxihITJ6g6mb/exec"
link3 = "https://script.google.com/macros/s/AKfycbzTMdTGQczpfnWd76rdwhj1rr_4DCMTMITYFgJZBcGrDbBSQZIHKu3mTkaXYnB5Y9VZew/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "#"

# ----------- GRID -----------

st.markdown(f"""
<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap:20px;">

<a href="{link1}" target="_blank"><div class="card c1">📊 PMY Verify Data</div></a>
<a href="{link2}" target="_blank"><div class="card c2">🏦 BOP Account</div></a>
<a href="{link3}" target="_blank"><div class="card c3">📁 ACAG Batch Data</div></a>
<a href="{link4}" target="_blank"><div class="card c4">📲 PMY Apply</div></a>
<a href="{link5}" target="_blank"><div class="card c5">📝 ACAG Apply</div></a>
<a href="{link6}" target="_blank"><div class="card c6">🚧 RDC</div></a>

</div>
""", unsafe_allow_html=True)
