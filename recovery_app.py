import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="Neo Dashboard",
    page_icon="⚡",
    layout="wide"
)

# ================= LINKS =================
link1 = "https://script.google.com/macros/s/AKfycbzlyx-OPgSTo-FsevohLyr9UfVSyWsVZk6tUGTVQgIFCNWxw0G6PuvnrqBnj1OPkCGq8g/exec"
link2 = "https://script.google.com/macros/s/AKfycbwvtLEuEivUZGCYylcrwnF9jjbwFT7gqlQEdsAASRCiJiNolICfIIrz5BzqaqTgtSqV/exec"
link3 = "https://script.google.com/macros/s/AKfycbxP-tH7L2kN5w0ApiQfC7ZPzh0nZZGsO1-u7XcfPdx2C-nSyTHLasA2cv6eozXAujzGFw/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"

# ================= CSS =================
st.markdown("""
<style>

/* ===== MAIN BACKGROUND ===== */
.stApp {
    background: #050816;
    overflow-x:hidden;
}

/* ===== REMOVE STREAMLIT ===== */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 1rem;
    max-width: 1500px;
}

/* ===== ANIMATED BACKGROUND ===== */
.bg-animation {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: -1;
    overflow: hidden;
}

.circle {
    position: absolute;
    border-radius: 50%;
    background: rgba(0,255,255,0.08);
    animation: float 14s infinite linear;
}

.circle:nth-child(1){
    width:300px;
    height:300px;
    left:5%;
    top:10%;
}

.circle:nth-child(2){
    width:250px;
    height:250px;
    right:10%;
    top:20%;
    background: rgba(168,85,247,0.10);
}

.circle:nth-child(3){
    width:200px;
    height:200px;
    left:35%;
    bottom:10%;
    background: rgba(59,130,246,0.10);
}

@keyframes float {
    0%{transform:translateY(0px) rotate(0deg);}
    50%{transform:translateY(-40px) rotate(180deg);}
    100%{transform:translateY(0px) rotate(360deg);}
}

/* ===== HERO ===== */
.hero {
    position: relative;
    padding: 55px;
    border-radius: 35px;
    overflow: hidden;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    box-shadow: 0 0 50px rgba(0,255,255,0.08);
    margin-bottom: 40px;
}

.hero::before {
    content: '';
    position: absolute;
    width: 450px;
    height: 450px;
    background: linear-gradient(45deg,#00f0ff,#8b5cf6);
    border-radius: 50%;
    filter: blur(120px);
    top: -200px;
    right: -120px;
    opacity:0.4;
}

.hero-title {
    font-size: 72px;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 12px;
    background: linear-gradient(to right,#ffffff,#00e5ff,#8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 28px;
}

.hero-btn {
    display:inline-block;
    padding:14px 28px;
    border-radius:18px;
    background: linear-gradient(90deg,#00e5ff,#8b5cf6);
    color:white;
    font-weight:700;
    box-shadow:0 10px 30px rgba(0,229,255,0.35);
}

/* ===== GRID ===== */
.grid {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:28px;
}

/* ===== CARD ===== */
.card {
    position:relative;
    overflow:hidden;
    padding:35px;
    border-radius:30px;
    background: rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    transition:0.4s ease;
    min-height:240px;
    box-shadow:0 15px 40px rgba(0,0,0,0.35);
}

.card:hover {
    transform:translateY(-15px) scale(1.03);
    border:1px solid rgba(0,229,255,0.45);
    box-shadow:0 20px 60px rgba(0,229,255,0.18);
}

.card::before {
    content:'';
    position:absolute;
    width:180px;
    height:180px;
    background:rgba(255,255,255,0.08);
    border-radius:50%;
    top:-60px;
    right:-60px;
}

.card-icon {
    width:85px;
    height:85px;
    border-radius:24px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:42px;
    margin-bottom:25px;
    background: linear-gradient(145deg,rgba(255,255,255,0.15),rgba(255,255,255,0.05));
    border:1px solid rgba(255,255,255,0.12);
}

.card-title {
    font-size:28px;
    font-weight:800;
    color:white;
    margin-bottom:10px;
}

.card-desc {
    color:#d1d5db;
    line-height:1.7;
    font-size:15px;
    margin-bottom:24px;
}

.card-btn {
    display:inline-block;
    padding:12px 24px;
    border-radius:16px;
    background:rgba(255,255,255,0.10);
    color:white;
    font-weight:700;
    transition:0.3s ease;
}

.card:hover .card-btn {
    background:white;
    color:black;
}

/* ===== COLORS ===== */
.c1{border-top:4px solid #00e5ff;}
.c2{border-top:4px solid #f59e0b;}
.c3{border-top:4px solid #8b5cf6;}
.c4{border-top:4px solid #10b981;}
.c5{border-top:4px solid #ec4899;}
.c6{border-top:4px solid #ef4444;}

/* ===== LINKS ===== */
a {
    text-decoration:none !important;
}

/* ===== TICKER ===== */
.ticker-wrap {
    margin-top:40px;
    overflow:hidden;
    border-radius:24px;
    padding:18px 0;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
}

.ticker {
    display:inline-block;
    white-space:nowrap;
    padding-left:100%;
    animation:scroll 18s linear infinite;
    font-size:20px;
    font-weight:700;
    color:#00e5ff;
}

@keyframes scroll {
    0% {transform:translateX(0);}
    100% {transform:translateX(-100%);}
}

/* ===== STATS ===== */
.stats {
    margin-top:35px;
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:22px;
}

.stat {
    padding:30px;
    border-radius:25px;
    text-align:center;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(12px);
}

.stat h1 {
    font-size:48px;
    color:white;
    margin:0;
}

.stat p {
    color:#cbd5e1;
    margin-top:8px;
}

/* ===== MOBILE ===== */
@media(max-width:768px){

.hero {
    padding:30px;
}

.hero-title {
    font-size:42px;
}

.card-title {
    font-size:24px;
}

}

</style>
""", unsafe_allow_html=True)

# ================= BACKGROUND =================
st.markdown("""
<div class="bg-animation">
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
</div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">

<div class="hero-title">
Neo Digital <br>Dashboard
</div>

<div class="hero-sub">
Futuristic Premium UI • Glassmorphism • Smooth Neon Experience
</div>

<div class="hero-btn">
⚡ SYSTEM ONLINE
</div>

</div>
""", unsafe_allow_html=True)

# ================= CARDS =================
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank">
<div class="card c1">
<div class="card-icon">📊</div>
<div class="card-title">PMY Verify</div>
<div class="card-desc">
Advanced PMY verification system with secure instant access.
</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link2}" target="_blank">
<div class="card c2">
<div class="card-icon">🏦</div>
<div class="card-title">BOP Account</div>
<div class="card-desc">
Manage banking details and services with smart access.
</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link3}" target="_blank">
<div class="card c3">
<div class="card-icon">📁</div>
<div class="card-title">ACAG Batch</div>
<div class="card-desc">
Track and monitor latest ACAG batch processing data.
</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link4}" target="_blank">
<div class="card c4">
<div class="card-icon">📲</div>
<div class="card-title">PMY Apply</div>
<div class="card-desc">
Apply online and track PMY applications instantly.
</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link5}" target="_blank">
<div class="card c5">
<div class="card-icon">📝</div>
<div class="card-title">ACAG Apply</div>
<div class="card-desc">
Smart ACAG application workflow with modern interface.
</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link6}" target="_blank">
<div class="card c6">
<div class="card-icon">🚀</div>
<div class="card-title">QR Generator</div>
<div class="card-desc">
Generate stylish QR codes with advanced functionality.
</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

</div>
""", unsafe_allow_html=True)

# ================= TICKER =================
st.markdown("""
<div class="ticker-wrap">
<div class="ticker">
⚡ ACAG Batch 31 Updated • PMY Services Active • Secure Dashboard Online • All Systems Operational 🚀
</div>
</div>
""", unsafe_allow_html=True)

# ================= STATS =================
st.markdown("""
<div class="stats">

<div class="stat">
<h1>06</h1>
<p>Quick Services</p>
</div>

<div class="stat">
<h1>24/7</h1>
<p>Availability</p>
</div>

<div class="stat">
<h1>99%</h1>
<p>Fast Performance</p>
</div>

<div class="stat">
<h1>⚡</h1>
<p>Premium UI</p>
</div>

</div>
""", unsafe_allow_html=True)
