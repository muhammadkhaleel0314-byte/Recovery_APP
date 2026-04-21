import streamlit as st

st.set_page_config(page_title="Smart Dashboard", layout="wide")

st.title("🚀 Smart Dashboard")

# ----------- AOS + STYLE -----------
st.markdown("""
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

<style>
body {
    background: linear-gradient(135deg, #141E30, #243B55);
    color: white;
}

/* Card Style */
.card {
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    margin: 10px;

    backdrop-filter: blur(12px);
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);

    transition: 0.3s;
}

/* Hover */
.card:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

/* Colors */
.c1 {background:#fff; color:black;}
.c2 {background:#FFD700; color:black;}
.c3 {background:#777;}
.c4 {background:linear-gradient(135deg,#11998e,#38ef7d);}
.c5 {background:linear-gradient(135deg,#36d1dc,#5b86e5);}
.c6 {background:linear-gradient(135deg,#ff512f,#dd2476);}

/* Remove link style */
a {text-decoration:none; color:inherit;}
</style>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>
setTimeout(function(){
    AOS.init({
        duration: 1200,
        once: true
    });
}, 500);
</script>
""", unsafe_allow_html=True)

# ----------- LINKS -----------
link1 = "https://script.google.com/macros/s/AKfycbyCr-KxEdrWdLhHXYWMLcDdK1Viciar6yJtQsaQNPFuY-X9IK41GkOiRvkV64PbatE9Kg/exec"
link2 = "https://script.google.com/macros/s/AKfycbzPaNIURbCJLA8iNRm3RA6v2OS5WlxaMURw0IIjcwLnLvBPlVJ9DJG7KxihITJ6g6mb/exec"
link3 = "https://script.google.com/macros/s/AKfycbzTMdTGQczpfnWd76rdwhj1rr_4DCMTMITYFgJZBcGrDbBSQZIHKu3mTkaXYnB5Y9VZew/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "#"

# ----------- GRID UI -----------
st.markdown(f"""
<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap:20px;">

<a href="{link1}" target="_blank">
<div class="card c1" data-aos="fade-right">📊 PMY Verify Data</div>
</a>

<a href="{link2}" target="_blank">
<div class="card c2" data-aos="fade-left">🏦 BOP Account</div>
</a>

<a href="{link3}" target="_blank">
<div class="card c3" data-aos="fade-up">📁 ACAG Batch Data</div>
</a>

<a href="{link4}" target="_blank">
<div class="card c4" data-aos="zoom-in">📲 PMY Apply</div>
</a>

<a href="{link5}" target="_blank">
<div class="card c5" data-aos="flip-left">📝 ACAG Apply</div>
</a>

<a href="{link6}" target="_blank">
<div class="card c6" data-aos="zoom-out">🚧 RDC</div>
</a>

</div>
""", unsafe_allow_html=True)
