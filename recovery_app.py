import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ultra Modern Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ---------------- HIDE STREAMLIT ----------------
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* =========================
BACKGROUND
========================= */
.stApp{
    background:
    radial-gradient(circle at top left,#1e3a8a 0%,transparent 30%),
    radial-gradient(circle at bottom right,#7c3aed 0%,transparent 30%),
    linear-gradient(135deg,#050816,#0f172a,#111827);
    color:white;
    overflow-x:hidden;
}

/* =========================
MAIN CONTAINER
========================= */
.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* =========================
TOP HERO
========================= */
.hero{
    position:relative;
    overflow:hidden;
    padding:45px;
    border-radius:32px;
    background:rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(20px);
    box-shadow:0 20px 60px rgba(0,0,0,0.45);
    margin-bottom:35px;
}

.hero::before{
    content:'';
    position:absolute;
    width:500px;
    height:500px;
    background:rgba(255,255,255,0.05);
    border-radius:50%;
    top:-250px;
    right:-180px;
}

.hero-title{
    font-size:60px;
    font-weight:900;
    line-height:1.1;
    margin-bottom:10px;
    background:linear-gradient(to right,#ffffff,#60a5fa,#c084fc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub{
    font-size:18px;
    color:#d1d5db;
    margin-bottom:25px;
}

.hero-badge{
    display:inline-block;
    padding:12px 22px;
    border-radius:50px;
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.08);
    font-weight:600;
    color:#e5e7eb;
}

/* =========================
GRID
========================= */
.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:25px;
}

/* =========================
CARD
========================= */
.card{
    position:relative;
    overflow:hidden;
    padding:35px 28px;
    min-height:240px;
    border-radius:30px;
    transition:0.4s ease;
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(20px);
    box-shadow:0 15px 40px rgba(0,0,0,0.35);
}

.card:hover{
    transform:translateY(-14px) scale(1.03);
    box-shadow:0 25px 60px rgba(0,0,0,0.5);
}

/* GLOW EFFECT */
.card::before{
    content:'';
    position:absolute;
    width:220px;
    height:220px;
    background:rgba(255,255,255,0.08);
    border-radius:50%;
    top:-100px;
    right:-80px;
}

.card::after{
    content:'';
    position:absolute;
    inset:0;
    background:linear-gradient(
    130deg,
    rgba(255,255,255,0.08),
    transparent,
    transparent
    );
}

/* =========================
ICON
========================= */
.icon{
    width:80px;
    height:80px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:42px;
    border-radius:22px;
    margin-bottom:25px;
    background:rgba(255,255,255,0.12);
    border:1px solid rgba(255,255,255,0.12);
}

/* =========================
TEXT
========================= */
.card-title{
    font-size:28px;
    font-weight:800;
    margin-bottom:12px;
}

.card-desc{
    font-size:15px;
    line-height:1.7;
    color:#e5e7eb;
    margin-bottom:25px;
}

/* =========================
BUTTON
========================= */
.btn{
    display:inline-block;
    padding:13px 24px;
    border-radius:16px;
    background:white;
    color:black;
    font-weight:700;
    transition:0.3s ease;
    font-size:14px;
}

.card:hover .btn{
    transform:scale(1.08);
}

/* =========================
COLORS
========================= */
.c1{
    background:linear-gradient(145deg,#2563eb,#1d4ed8);
}

.c2{
    background:linear-gradient(145deg,#f59e0b,#ea580c);
}

.c3{
    background:linear-gradient(145deg,#7c3aed,#6d28d9);
}

.c4{
    background:linear-gradient(145deg,#10b981,#059669);
}

.c5{
    background:linear-gradient(145deg,#ec4899,#db2777);
}

.c6{
    background:linear-gradient(145deg,#ef4444,#dc2626);
}

/* =========================
LINK
========================= */
a{
    text-decoration:none !important;
    color:white !important;
}

/* =========================
FLOATING ANIMATION
========================= */
.float{
    animation:float 4s ease-in-out infinite;
}

@keyframes float{
    0%{transform:translateY(0px);}
    50%{transform:translateY(-8px);}
    100%{transform:translateY(0px);}
}

/* =========================
SCROLL TICKER
========================= */
.ticker-wrap{
    margin-top:35px;
    overflow:hidden;
    border-radius:22px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
    padding:18px 0;
}

.ticker{
    white-space:nowrap;
    display:inline-block;
    padding-left:100%;
    animation:scroll 22s linear infinite;
    font-size:20px;
    font-weight:700;
    color:#facc15;
}

@keyframes scroll{
    0%{
        transform:translateX(0);
    }
    100%{
        transform:translateX(-100%);
    }
}

/* =========================
BOTTOM STATS
========================= */
.stats{
    margin-top:35px;
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
}

.stat-box{
    padding:28px;
    border-radius:24px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
    text-align:center;
}

.stat-num{
    font-size:40px;
    font-weight:900;
}

.stat-text{
    color:#d1d5db;
    margin-top:5px;
}

/* =========================
MOBILE
========================= */
@media(max-width:768px){

.hero{
    padding:28px;
}

.hero-title{
    font-size:38px;
}

.card-title{
    font-size:24px;
}

}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero float">

<div class="hero-title">
Ultra Modern <br>Dashboard
</div>

<div class="hero-sub">
Premium Glassmorphism UI • Smooth Animations • Fast Access System
</div>

<div class="hero-badge">
⚡ All Services Online
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- LINKS ----------------
link1 = "https://script.google.com/macros/s/AKfycbyCr-KxEdrWdLhHXYWMLcDdK1Viciar6yJtQsaQNPFuY-X9IK41GkOiRvkV64PbatE9Kg/exec"
link2 = "https://script.google.com/macros/s/AKfycbzPaNIURbCJLA8iNRm3RA6v2OS5WlxaMURw0IIjcwLnLvBPlVJ9DJG7KxihITJ6g6mb/exec"
link3 = "https://script.google.com/macros/s/AKfycbxP-tH7L2kN5w0ApiQfC7ZPzh0nZZGsO1-u7XcfPdx2C-nSyTHLasA2cv6eozXAujzGFw/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"

# ---------------- CARDS ----------------
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank">
<div class="card c1">
<div class="icon">📊</div>
<div class="card-title">PMY Verify</div>
<div class="card-desc">
Secure verification system with fast processing and instant access.
</div>
<div class="btn">Launch Portal →</div>
</div>
</a>

<a href="{link2}" target="_blank">
<div class="card c2">
<div class="icon">🏦</div>
<div class="card-title">BOP Account</div>
<div class="card-desc">
Access banking tools, account details and management services.
</div>
<div class="btn">Launch Portal →</div>
</div>
</a>

<a href="{link3}" target="_blank">
<div class="card c3">
<div class="icon">📁</div>
<div class="card-title">ACAG Batch</div>
<div class="card-desc">
Check latest uploaded batches with complete processing data.
</div>
<div class="btn">Launch Portal →</div>
</div>
</a>

<a href="{link4}" target="_blank">
<div class="card c4">
<div class="icon">📲</div>
<div class="card-title">PMY Apply</div>
<div class="card-desc">
Apply online and track PMY application progress in real time.
</div>
<div class="btn">Launch Portal →</div>
</div>
</a>

<a href="{link5}" target="_blank">
<div class="card c5">
<div class="icon">📝</div>
<div class="card-title">ACAG Apply</div>
<div class="card-desc">
Complete ACAG applications with smart modern workflow system.
</div>
<div class="btn">Launch Portal →</div>
</div>
</a>

<a href="{link6}" target="_blank">
<div class="card c6">
<div class="icon">🚧</div>
<div class="card-title">QR Generator</div>
<div class="card-desc">
Create advanced QR codes instantly with modern QR engine tools.
</div>
<div class="btn">Launch Portal →</div>
</div>
</a>

</div>
""", unsafe_allow_html=True)

# ---------------- TICKER ----------------
st.markdown("""
<div class="ticker-wrap">
<div class="ticker">
🔥 ACAG Batch 31 Updated • PMY Verification Running • Modern Dashboard Active • All Systems Operational 🚀
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- STATS ----------------
st.markdown("""
<div class="stats">

<div class="stat-box">
<div class="stat-num">06</div>
<div class="stat-text">Quick Services</div>
</div>

<div class="stat-box">
<div class="stat-num">24/7</div>
<div class="stat-text">Availability</div>
</div>

<div class="stat-box">
<div class="stat-num">100%</div>
<div class="stat-text">Responsive UI</div>
</div>

<div class="stat-box">
<div class="stat-num">⚡</div>
<div class="stat-text">Fast Performance</div>
</div>

</div>
""", unsafe_allow_html=True)
