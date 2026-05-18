import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Modern Quick Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ---------------- PAGE TITLE ----------------
st.markdown("""
<h1 style='text-align:center;
           font-size:48px;
           font-weight:800;
           margin-bottom:5px;'>
🚀 Modern Quick Dashboard
</h1>

<p style='text-align:center;
          color:gray;
          font-size:18px;
          margin-top:0;'>
Fast Access Portal • Stylish • Responsive • Animated
</p>
""", unsafe_allow_html=True)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* ---------------- MAIN ---------------- */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* REMOVE STREAMLIT EXTRA SPACE */
.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
}

/* ---------------- BACKGROUND ---------------- */
.stApp {
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color:white;
}

/* ---------------- TOP BAR ---------------- */
.top-bar{
    width:100%;
    padding:18px 25px;
    border-radius:18px;
    background:rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
    margin-bottom:25px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 8px 30px rgba(0,0,0,0.25);
}

.top-left{
    font-size:22px;
    font-weight:700;
}

.top-right{
    font-size:15px;
    color:#d1d5db;
}

/* ---------------- GRID ---------------- */
.grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(260px,1fr));
    gap:24px;
    margin-top:10px;
}

/* ---------------- CARD ---------------- */
.card {
    position:relative;
    overflow:hidden;
    padding:30px 25px;
    border-radius:24px;
    color:white;
    text-align:center;
    transition:0.35s ease;
    cursor:pointer;
    min-height:170px;
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    box-shadow:0 8px 25px rgba(0,0,0,0.25);
}

/* Hover Effect */
.card:hover{
    transform:translateY(-10px) scale(1.03);
    box-shadow:0 15px 35px rgba(0,0,0,0.35);
}

/* Glow Circle */
.card::before{
    content:'';
    position:absolute;
    width:180px;
    height:180px;
    background:rgba(255,255,255,0.08);
    border-radius:50%;
    top:-70px;
    right:-70px;
}

/* ICON */
.icon{
    font-size:50px;
    margin-bottom:18px;
}

/* TITLE */
.card-title{
    font-size:22px;
    font-weight:700;
    margin-bottom:8px;
}

/* DESC */
.card-desc{
    font-size:14px;
    opacity:0.9;
    line-height:1.6;
}

/* BUTTON */
.open-btn{
    margin-top:20px;
    display:inline-block;
    padding:10px 22px;
    border-radius:12px;
    background:rgba(255,255,255,0.15);
    color:white;
    font-size:14px;
    font-weight:600;
    transition:0.3s;
}

.card:hover .open-btn{
    background:white;
    color:black;
}

/* ---------------- COLORS ---------------- */
.c1{
    background:linear-gradient(135deg,#3b82f6,#2563eb);
}

.c2{
    background:linear-gradient(135deg,#f59e0b,#d97706);
}

.c3{
    background:linear-gradient(135deg,#6366f1,#4f46e5);
}

.c4{
    background:linear-gradient(135deg,#10b981,#059669);
}

.c5{
    background:linear-gradient(135deg,#ec4899,#db2777);
}

.c6{
    background:linear-gradient(135deg,#ef4444,#dc2626);
}

/* ---------------- LINKS ---------------- */
a{
    text-decoration:none !important;
}

/* ---------------- ANIMATION ---------------- */
.card{
    opacity:0;
    animation:fadeUp 0.8s ease forwards;
}

.d1{animation-delay:0.1s;}
.d2{animation-delay:0.2s;}
.d3{animation-delay:0.3s;}
.d4{animation-delay:0.4s;}
.d5{animation-delay:0.5s;}
.d6{animation-delay:0.6s;}

@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(40px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* ---------------- TICKER ---------------- */
.ticker {
    margin-top:35px;
    width:100%;
    overflow:hidden;
    border-radius:16px;
    background:linear-gradient(90deg,#111827,#1f2937);
    border:1px solid rgba(255,255,255,0.08);
    padding:16px 0;
    box-shadow:0 5px 20px rgba(0,0,0,0.25);
}

.ticker-text {
    display:inline-block;
    white-space:nowrap;
    padding-left:100%;
    animation:scroll 22s linear infinite;
    font-size:18px;
    font-weight:700;
    color:#facc15;
}

@keyframes scroll{
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

/* ---------------- FOOTER ---------------- */
.footer{
    text-align:center;
    margin-top:30px;
    color:#9ca3af;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TOP BAR ----------------
st.markdown("""
<div class="top-bar">
    <div class="top-left">⚡ Quick Access Panel</div>
    <div class="top-right">Modern UI Dashboard</div>
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
<div class="card c1 d1">
    <div class="icon">📊</div>
    <div class="card-title">PMY Verify Data</div>
    <div class="card-desc">
        Verify PMY records quickly and securely.
    </div>
    <div class="open-btn">Open Portal</div>
</div>
</a>

<a href="{link2}" target="_blank">
<div class="card c2 d2">
    <div class="icon">🏦</div>
    <div class="card-title">BOP Account</div>
    <div class="card-desc">
        Access and manage BOP account services.
    </div>
    <div class="open-btn">Open Portal</div>
</div>
</a>

<a href="{link3}" target="_blank">
<div class="card c3 d3">
    <div class="icon">📁</div>
    <div class="card-title">ACAG Batch Data</div>
    <div class="card-desc">
        Check latest ACAG uploaded batch records.
    </div>
    <div class="open-btn">Open Portal</div>
</div>
</a>

<a href="{link4}" target="_blank">
<div class="card c4 d4">
    <div class="icon">📲</div>
    <div class="card-title">PMY Apply & Track</div>
    <div class="card-desc">
        Submit and track PMY applications online.
    </div>
    <div class="open-btn">Open Portal</div>
</div>
</a>

<a href="{link5}" target="_blank">
<div class="card c5 d5">
    <div class="icon">📝</div>
    <div class="card-title">ACAG Apply</div>
    <div class="card-desc">
        Apply online for ACAG scheme instantly.
    </div>
    <div class="open-btn">Open Portal</div>
</div>
</a>

<a href="{link6}" target="_blank">
<div class="card c6 d6">
    <div class="icon">🚧</div>
    <div class="card-title">QR Generator</div>
    <div class="card-desc">
        Generate QR codes with advanced features.
    </div>
    <div class="open-btn">Open Portal</div>
</div>
</a>

</div>
""", unsafe_allow_html=True)

# ---------------- TICKER ----------------
st.markdown("""
<div class="ticker">
    <div class="ticker-text">
        🔴 ACAG 31 Batch Updated Successfully • PMY Verification Active • Modern Dashboard Running Smoothly 🚀
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Developed with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
