import streamlit as st
from datetime import datetime
import random

# ================= CONFIG =================
st.set_page_config(
    page_title="NEXUS CONTROL CENTER",
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

# ================= VISITOR COUNTER =================
if "visits" not in st.session_state:
    st.session_state.visits = 0

st.session_state.visits += 1

# ================= QUOTES =================
quotes = [
    "Success comes from consistency.",
    "Stay focused and keep growing.",
    "Innovation starts with action.",
    "Small progress is still progress.",
    "Dream big. Execute bigger."
]

# ================= CSS =================
st.markdown("""
<style>

.stApp{
    background:#050816;
    overflow-x:hidden;
}

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.block-container{
    padding-top:1rem;
    max-width:1500px;
}

/* ===== Animated Background ===== */

.bg-animation{
    position:fixed;
    width:100%;
    height:100%;
    top:0;
    left:0;
    z-index:-1;
    overflow:hidden;
}

.circle{
    position:absolute;
    border-radius:50%;
    animation:float 14s infinite linear;
}

.circle:nth-child(1){
    width:300px;
    height:300px;
    background:rgba(0,229,255,0.08);
    left:5%;
    top:10%;
}

.circle:nth-child(2){
    width:250px;
    height:250px;
    background:rgba(139,92,246,0.08);
    right:10%;
    top:20%;
}

.circle:nth-child(3){
    width:220px;
    height:220px;
    background:rgba(16,185,129,0.08);
    left:40%;
    bottom:10%;
}

@keyframes float{
0%{transform:translateY(0) rotate(0deg);}
50%{transform:translateY(-40px) rotate(180deg);}
100%{transform:translateY(0) rotate(360deg);}
}

/* ===== TOP INFO BAR ===== */

.info-bar{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border-radius:20px;
    padding:15px;
    margin-bottom:20px;
    text-align:center;
    color:white;
    font-size:18px;
    font-weight:700;
}

/* ===== GREETING ===== */

.greet{
    background:linear-gradient(90deg,#00e5ff,#8b5cf6);
    padding:18px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:28px;
    font-weight:900;
    margin-bottom:25px;
    box-shadow:0 10px 30px rgba(0,229,255,.25);
}

/* ===== HERO ===== */

.hero{
    position:relative;
    overflow:hidden;
    padding:60px;
    border-radius:35px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(18px);
    margin-bottom:35px;
}

.hero:before{
    content:'';
    position:absolute;
    width:450px;
    height:450px;
    border-radius:50%;
    background:linear-gradient(45deg,#00e5ff,#8b5cf6);
    filter:blur(120px);
    right:-150px;
    top:-200px;
    opacity:.35;
}

.hero-title{
    font-size:72px;
    font-weight:900;
    background:linear-gradient(to right,#fff,#00e5ff,#8b5cf6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub{
    color:#cbd5e1;
    font-size:20px;
    margin-top:10px;
}

.hero-btn{
    display:inline-block;
    margin-top:25px;
    padding:14px 28px;
    border-radius:18px;
    background:linear-gradient(90deg,#00e5ff,#8b5cf6);
    color:white;
    font-weight:800;
}

/* ===== SEARCH ===== */

.search-box{
    margin-top:25px;
}

/* ===== STATS ===== */

.stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-top:30px;
}

.stat{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:25px;
    padding:25px;
    text-align:center;
    backdrop-filter:blur(15px);
}

.stat h1{
    color:white;
    font-size:45px;
    margin:0;
}

.stat p{
    color:#cbd5e1;
}

@media(max-width:768px){

.hero{
padding:30px;
}

.hero-title{
font-size:42px;
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

# ================= CLOCK =================

now = datetime.now()

st.markdown(f"""
<div class="info-bar">
🕒 {now.strftime("%d %B %Y | %I:%M:%S %p")}
</div>
""", unsafe_allow_html=True)

# ================= GREETING =================

hour = now.hour

if hour < 12:
    greet = "🌅 Good Morning"
elif hour < 18:
    greet = "☀️ Good Afternoon"
else:
    greet = "🌙 Good Evening"

st.markdown(f"""
<div class="greet">
{greet}
</div>
""", unsafe_allow_html=True)

# ================= HERO =================

st.markdown("""
<div class="hero">

<div class="hero-title">
NEXUS CONTROL CENTER
</div>

<div class="hero-sub">
AI Powered • Futuristic Glass UI • Premium Experience
</div>

<div class="hero-btn">
⚡ ALL SYSTEMS OPERATIONAL
</div>

</div>
""", unsafe_allow_html=True)

# ================= SEARCH =================

search = st.text_input(
    "🔍 Search Service",
    placeholder="PMY, BOP, ACAG..."
)

if search:
    st.success(f"Searching: {search}")

# ================= QUOTE =================

st.info("💡 " + random.choice(quotes))
# ================= EXTRA CSS FOR CARDS =================

st.markdown("""
<style>

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:28px;
    margin-top:30px;
}

.card{
    position:relative;
    overflow:hidden;
    padding:35px;
    border-radius:30px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(18px);
    transition:0.4s ease;
    min-height:240px;
    box-shadow:0 15px 40px rgba(0,0,0,0.35);
}

.card:hover{
    transform:translateY(-15px) scale(1.03);
    border:1px solid rgba(0,229,255,0.5);

    box-shadow:
    0 0 20px #00e5ff,
    0 0 40px #00e5ff,
    0 0 80px #8b5cf6;
}

.card:before{
    content:'';
    position:absolute;
    width:180px;
    height:180px;
    border-radius:50%;
    top:-60px;
    right:-60px;
    background:rgba(255,255,255,0.06);
}

.card-icon{
    width:85px;
    height:85px;
    border-radius:24px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:42px;
    margin-bottom:25px;

    background:linear-gradient(
    145deg,
    rgba(255,255,255,0.15),
    rgba(255,255,255,0.05)
    );

    border:1px solid rgba(255,255,255,0.12);
}

.card-title{
    font-size:28px;
    font-weight:800;
    color:white;
    margin-bottom:10px;
}

.card-desc{
    color:#d1d5db;
    line-height:1.7;
    font-size:15px;
    margin-bottom:25px;
}

.card-btn{
    display:inline-block;
    padding:12px 24px;
    border-radius:16px;
    background:rgba(255,255,255,0.10);
    color:white;
    font-weight:700;
    transition:0.3s ease;
}

.card:hover .card-btn{
    background:white;
    color:black;
}

.c1{border-top:4px solid #00e5ff;}
.c2{border-top:4px solid #f59e0b;}
.c3{border-top:4px solid #8b5cf6;}
.c4{border-top:4px solid #10b981;}
.c5{border-top:4px solid #ec4899;}
.c6{border-top:4px solid #ef4444;}

a{
    text-decoration:none !important;
}

</style>
""", unsafe_allow_html=True)

# ================= SERVICES TITLE =================

st.markdown("""
<h2 style="
color:white;
margin-top:20px;
margin-bottom:20px;">
🚀 Quick Access Services
</h2>
""", unsafe_allow_html=True)

# ================= CARDS =================

st.markdown(f"""

<div class="grid">

<a href="{link1}" target="_blank">
<div class="card c1">

<div class="card-icon">📊</div>

<div class="card-title">
PMY Verify
</div>

<div class="card-desc">
Advanced PMY verification system with secure instant access.
</div>

<div class="card-btn">
Open Portal →
</div>

</div>
</a>

<a href="{link2}" target="_blank">
<div class="card c2">

<div class="card-icon">🏦</div>

<div class="card-title">
BOP Account
</div>

<div class="card-desc">
Manage banking details and services with smart access.
</div>

<div class="card-btn">
Open Portal →
</div>

</div>
</a>

<a href="{link3}" target="_blank">
<div class="card c3">

<div class="card-icon">📁</div>

<div class="card-title">
ACAG Batch
</div>

<div class="card-desc">
Track and monitor latest ACAG batch processing data.
</div>

<div class="card-btn">
Open Portal →
</div>

</div>
</a>

<a href="{link4}" target="_blank">
<div class="card c4">

<div class="card-icon">📲</div>

<div class="card-title">
PMY Apply
</div>

<div class="card-desc">
Apply online and track PMY applications instantly.
</div>

<div class="card-btn">
Open Portal →
</div>

</div>
</a>

<a href="{link5}" target="_blank">
<div class="card c5">

<div class="card-icon">📝</div>

<div class="card-title">
ACAG Apply
</div>

<div class="card-desc">
Smart ACAG application workflow with modern interface.
</div>

<div class="card-btn">
Open Portal →
</div>

</div>
</a>

<a href="{link6}" target="_blank">
<div class="card c6">

<div class="card-icon">🚀</div>

<div class="card-title">
Recovery Dashboard
</div>

<div class="card-desc">
Recovery reports, overdue analysis and smart tracking.
</div>

<div class="card-btn">
Open Portal →
</div>

</div>
</a>

</div>

""", unsafe_allow_html=True)

# ================= SYSTEM HEALTH =================

st.markdown("""
<br>
<h3 style="color:white;">
⚡ System Health
</h3>
""", unsafe_allow_html=True)

st.progress(99)

st.success("All Systems Operational")
# ================= VISITOR COUNTER DISPLAY =================

st.markdown(f"""
<div style="
margin-top:25px;
padding:18px;
border-radius:20px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
text-align:center;
color:white;
font-size:18px;
font-weight:700;">
👥 Page Visits (Session): {st.session_state.visits}
</div>
""", unsafe_allow_html=True)

# ================= TICKER =================

st.markdown("""
<div style="
margin-top:35px;
overflow:hidden;
border-radius:24px;
padding:15px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);">

<div style="
display:inline-block;
white-space:nowrap;
padding-left:100%;
animation:scroll 18s linear infinite;
color:#00e5ff;
font-weight:800;
font-size:18px;">

⚡ ACAG Batch Updated • PMY Services Active • Recovery Dashboard Live • Secure System Running • AI Optimization Enabled 🚀

</div>

</div>

<style>
@keyframes scroll {
0% {transform:translateX(0);}
100% {transform:translateX(-100%);}
}
</style>
""", unsafe_allow_html=True)

# ================= STATS =================

st.markdown("""
<div style="
margin-top:35px;
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;">

<div style="
padding:25px;
border-radius:25px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
text-align:center;
backdrop-filter:blur(12px);">
<h1 style="color:white;font-size:45px;margin:0;">06</h1>
<p style="color:#cbd5e1;">Quick Services</p>
</div>

<div style="
padding:25px;
border-radius:25px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
text-align:center;">
<h1 style="color:white;font-size:45px;margin:0;">24/7</h1>
<p style="color:#cbd5e1;">Availability</p>
</div>

<div style="
padding:25px;
border-radius:25px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
text-align:center;">
<h1 style="color:white;font-size:45px;margin:0;">99%</h1>
<p style="color:#cbd5e1;">Performance</p>
</div>

<div style="
padding:25px;
border-radius:25px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
text-align:center;">
<h1 style="color:white;font-size:45px;margin:0;">⚡</h1>
<p style="color:#cbd5e1;">Neon UI</p>
</div>

</div>
""", unsafe_allow_html=True)

# ================= FOOTER =================

st.markdown("""
<br><br>
<div style="
text-align:center;
padding:25px;
color:#94a3b8;
font-size:14px;
border-top:1px solid rgba(255,255,255,0.08);">

⚡ NEXUS CONTROL CENTER • Built with Streamlit • Premium Glass UI • 2026

</div>
""", unsafe_allow_html=True)
