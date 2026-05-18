import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="Quantum Dashboard",
    page_icon="⚡",
    layout="wide"
)

# ================= LINKS =================
link1 = "https://script.google.com/macros/s/AKfycbyCr-KxEdrWdLhHXYWMLcDdK1Viciar6yJtQsaQNPFuY-X9IK41GkOiRvkV64PbatE9Kg/exec"
link2 = "https://script.google.com/macros/s/AKfycbzPaNIURbCJLA8iNRm3RA6v2OS5WlxaMURw0IIjcwLnLvBPlVJ9DJG7KxihITJ6g6mb/exec"
link3 = "https://script.google.com/macros/s/AKfycbxP-tH7L2kN5w0ApiQfC7ZPzh0nZZGsO1-u7XcfPdx2C-nSyTHLasA2cv6eozXAujzGFw/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"

# ================= STYLE =================
st.markdown("""
<style>

/* ===== MAIN ===== */
.stApp {
    background:
    radial-gradient(circle at top left,#00f5ff22,transparent 25%),
    radial-gradient(circle at bottom right,#8b5cf622,transparent 25%),
    linear-gradient(135deg,#020617,#050816,#0f172a);
    overflow-x:hidden;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    max-width:1500px;
    padding-top:1rem;
}

/* ===== FLOATING LIGHTS ===== */
.light{
    position:fixed;
    border-radius:50%;
    filter:blur(90px);
    z-index:-1;
    animation:float 12s infinite ease-in-out;
}

.l1{
    width:350px;
    height:350px;
    background:#00e5ff33;
    top:-80px;
    left:-50px;
}

.l2{
    width:300px;
    height:300px;
    background:#8b5cf633;
    bottom:-80px;
    right:-50px;
}

@keyframes float{
0%{transform:translateY(0px);} 
50%{transform:translateY(-35px);} 
100%{transform:translateY(0px);} 
}

/* ===== HERO ===== */
.hero{
    position:relative;
    overflow:hidden;
    padding:65px;
    border-radius:40px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.10);
    backdrop-filter:blur(20px);
    box-shadow:
    0 0 60px rgba(0,229,255,0.10),
    0 0 120px rgba(139,92,246,0.10);
    margin-bottom:40px;
}

.hero::before{
    content:'';
    position:absolute;
    width:500px;
    height:500px;
    background:linear-gradient(45deg,#00e5ff,#8b5cf6);
    filter:blur(140px);
    border-radius:50%;
    top:-250px;
    right:-100px;
    opacity:0.4;
}

.hero-title{
    font-size:85px;
    font-weight:1000;
    line-height:0.95;
    margin-bottom:18px;
    background:linear-gradient(to right,#ffffff,#00e5ff,#a855f7);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub{
    font-size:22px;
    color:#d1d5db;
    margin-bottom:28px;
}

.hero-chip{
    display:inline-block;
    padding:14px 26px;
    border-radius:18px;
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.08);
    color:white;
    font-weight:700;
    box-shadow:0 0 25px rgba(0,229,255,0.15);
}

/* ===== GRID ===== */
.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
    gap:30px;
}

/* ===== CARD ===== */
.card{
    position:relative;
    overflow:hidden;
    padding:38px;
    border-radius:34px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(18px);
    transition:0.45s ease;
    min-height:260px;
    box-shadow:0 15px 45px rgba(0,0,0,0.35);
}

.card:hover{
    transform:translateY(-16px) scale(1.03) rotate(-1deg);
    border:1px solid rgba(0,229,255,0.45);
    box-shadow:
    0 0 35px rgba(0,229,255,0.25),
    0 0 70px rgba(139,92,246,0.15);
}

.card::before{
    content:'';
    position:absolute;
    width:220px;
    height:220px;
    border-radius:50%;
    background:rgba(255,255,255,0.08);
    top:-70px;
    right:-70px;
}

.card::after{
    content:'';
    position:absolute;
    inset:0;
    background:linear-gradient(130deg,rgba(255,255,255,0.10),transparent,transparent);
}

.icon{
    width:90px;
    height:90px;
    border-radius:26px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:45px;
    margin-bottom:25px;
    background:rgba(255,255,255,0.10);
    border:1px solid rgba(255,255,255,0.12);
    box-shadow:0 0 25px rgba(255,255,255,0.08);
}

.title{
    font-size:30px;
    font-weight:900;
    color:white;
    margin-bottom:12px;
}

.desc{
    color:#d1d5db;
    line-height:1.8;
    font-size:15px;
    margin-bottom:25px;
}

.btn{
    display:inline-block;
    padding:14px 26px;
    border-radius:18px;
    background:linear-gradient(90deg,#00e5ff,#8b5cf6);
    color:white;
    font-weight:800;
    font-size:14px;
    box-shadow:0 10px 30px rgba(0,229,255,0.25);
    transition:0.3s ease;
}

.card:hover .btn{
    transform:scale(1.08);
}

/* ===== COLORS ===== */
.c1{border-top:5px solid #00e5ff;}
.c2{border-top:5px solid #f59e0b;}
.c3{border-top:5px solid #8b5cf6;}
.c4{border-top:5px solid #10b981;}
.c5{border-top:5px solid #ec4899;}
.c6{border-top:5px solid #ef4444;}

/* ===== LINKS ===== */
a{
    text-decoration:none !important;
}

/* ===== TICKER ===== */
.ticker-wrap{
    margin-top:45px;
    overflow:hidden;
    border-radius:28px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    padding:20px 0;
    backdrop-filter:blur(10px);
}

.ticker{
    display:inline-block;
    white-space:nowrap;
    padding-left:100%;
    animation:scroll 18s linear infinite;
    font-size:22px;
    font-weight:800;
    color:#00e5ff;
}

@keyframes scroll{
0%{transform:translateX(0);} 
100%{transform:translateX(-100%);} 
}

/* ===== FOOTER STATS ===== */
.stats{
    margin-top:40px;
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:24px;
}

.stat{
    padding:35px;
    border-radius:28px;
    text-align:center;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(12px);
    transition:0.3s ease;
}

.stat:hover{
    transform:translateY(-10px);
    box-shadow:0 0 30px rgba(0,229,255,0.15);
}

.stat h1{
    color:white;
    font-size:52px;
    margin:0;
}

.stat p{
    color:#cbd5e1;
    margin-top:10px;
    font-size:15px;
}

/* ===== MOBILE ===== */
@media(max-width:768px){
.hero{padding:35px;}
.hero-title{font-size:48px;}
.title{font-size:25px;}
}

</style>
""", unsafe_allow_html=True)

# ================= FLOATING LIGHTS =================
st.markdown("""
<div class='light l1'></div>
<div class='light l2'></div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class='hero'>

<div class='hero-title'>
Quantum <br>Dashboard
</div>

<div class='hero-sub'>
Ultra Premium Futuristic Interface • Neon Glassmorphism • Luxury Modern Experience
</div>

<div class='hero-chip'>⚡ SYSTEM ACTIVE</div>

</div>
""", unsafe_allow_html=True)

# ================= CARDS =================
st.markdown(f"""
<div class='grid'>

<a href='{link1}' target='_blank'>
<div class='card c1'>
<div class='icon'>📊</div>
<div class='title'>PMY Verify</div>
<div class='desc'>
Secure PMY verification portal with instant smart processing.
</div>
<div class='btn'>Launch Portal →</div>
</div>
</a>

<a href='{link2}' target='_blank'>
<div class='card c2'>
<div class='icon'>🏦</div>
<div class='title'>BOP Account</div>
<div class='desc'>
Modern banking access system with advanced management tools.
</div>
<div class='btn'>Launch Portal →</div>
</div>
</a>

<a href='{link3}' target='_blank'>
<div class='card c3'>
<div class='icon'>📁</div>
<div class='title'>ACAG Batch</div>
<div class='desc'>
Track and monitor ACAG batch uploads with futuristic UI.
</div>
<div class='btn'>Launch Portal →</div>
</div>
</a>

<a href='{link4}' target='_blank'>
<div class='card c4'>
<div class='icon'>📲</div>
<div class='title'>PMY Apply</div>
<div class='desc'>
Apply online and monitor PMY applications instantly.
</div>
<div class='btn'>Launch Portal →</div>
</div>
</a>

<a href='{link5}' target='_blank'>
<div class='card c5'>
<div class='icon'>📝</div>
<div class='title'>ACAG Apply</div>
<div class='desc'>
Advanced ACAG application workflow with smooth interface.
</div>
<div class='btn'>Launch Portal →</div>
</div>
</a>

<a href='{link6}' target='_blank'>
<div class='card c6'>
<div class='icon'>🚀</div>
<div class='title'>QR Generator</div>
<div class='desc'>
Create beautiful QR codes with premium generation engine.
</div>
<div class='btn'>Launch Portal →</div>
</div>
</a>

</div>
""", unsafe_allow_html=True)

# ================= TICKER =================
st.markdown("""
<div class='ticker-wrap'>
<div class='ticker'>
⚡ ACAG Batch 31 Updated • PMY Verification Running • Quantum Dashboard Online • Premium UI Experience 🚀
</div>
</div>
""", unsafe_allow_html=True)

# ================= STATS =================
st.markdown("""
<div class='stats'>

<div class='stat'>
<h1>06</h1>
<p>Smart Services</p>
</div>

<div class='stat'>
<h1>24/7</h1>
<p>Availability</p>
</div>

<div class='stat'>
<h1>⚡</h1>
<p>Ultra Fast</p>
</div>

<div class='stat'>
<h1>100%</h1>
<p>Modern UI</p>
</div>

</div>
""", unsafe_allow_html=True)
