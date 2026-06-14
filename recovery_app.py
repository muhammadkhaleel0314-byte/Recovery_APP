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
}

/* hide streamlit UI */
#MainMenu, footer, header {visibility:hidden;}

.block-container{
    padding-top:1rem;
    max-width:1500px;
}

/* ===== BACKGROUND ===== */
.bg{
    position:fixed;
    width:100%;
    height:100%;
    z-index:-1;
}

.circle{
    position:absolute;
    border-radius:50%;
    animation:float 12s infinite linear;
}

.circle:nth-child(1){
    width:300px;height:300px;
    background:rgba(0,229,255,0.08);
    left:5%;top:10%;
}

.circle:nth-child(2){
    width:250px;height:250px;
    background:rgba(139,92,246,0.08);
    right:10%;top:20%;
}

.circle:nth-child(3){
    width:220px;height:220px;
    background:rgba(16,185,129,0.08);
    left:40%;bottom:10%;
}

@keyframes float{
0%{transform:translateY(0);}
50%{transform:translateY(-40px);}
100%{transform:translateY(0);}
}

/* ===== TOP BAR ===== */
.topbar{
    padding:15px;
    border-radius:20px;
    background:rgba(255,255,255,0.05);
    text-align:center;
    color:white;
    font-weight:700;
    margin-bottom:15px;
}

/* ===== GREETING ===== */
.greet{
    text-align:center;
    padding:18px;
    border-radius:20px;
    background:linear-gradient(90deg,#00e5ff,#8b5cf6);
    color:white;
    font-size:26px;
    font-weight:900;
    margin-bottom:25px;
}

/* ===== HERO ===== */
.hero{
    padding:55px;
    border-radius:30px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    margin-bottom:30px;
}

.hero-title{
    font-size:60px;
    font-weight:900;
    background:linear-gradient(to right,#fff,#00e5ff,#8b5cf6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub{
    color:#cbd5e1;
    font-size:18px;
}

/* ===== SEARCH ===== */
input{
    border-radius:12px !important;
}

/* ===== CARDS ===== */
.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:20px;
    margin-top:25px;
}

.card{
    padding:30px;
    border-radius:25px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    transition:0.3s;
    text-align:center;
}

.card:hover{
    transform:translateY(-10px);
    box-shadow:0 0 25px rgba(0,229,255,0.3);
}

.icon{
    font-size:40px;
    margin-bottom:10px;
}

.title{
    font-size:22px;
    font-weight:800;
    color:white;
}

.desc{
    color:#cbd5e1;
    font-size:14px;
    margin:10px 0;
}

.btn{
    display:inline-block;
    padding:10px 18px;
    border-radius:12px;
    background:rgba(255,255,255,0.1);
    color:white;
    font-weight:700;
}

/* ===== ULTRA CARDS ===== */
.ultra{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-top:35px;
}

.ucard{
    padding:25px;
    border-radius:20px;
    text-align:center;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
}

.num{
    font-size:40px;
    font-weight:900;
    color:white;
}

/* ===== TICKER ===== */
.ticker{
    margin-top:30px;
    padding:15px;
    border-radius:20px;
    overflow:hidden;
    background:rgba(255,255,255,0.05);
}

.scroll{
    white-space:nowrap;
    display:inline-block;
    animation:scroll 15s linear infinite;
    color:#00e5ff;
    font-weight:800;
}

@keyframes scroll{
0%{transform:translateX(0);}
100%{transform:translateX(-100%);}
}

/* ===== FOOTER ===== */
.footer{
    margin-top:40px;
    text-align:center;
    color:#94a3b8;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ================= BACKGROUND =================
st.markdown("""
<div class="bg">
<div class="circle"></div>
<div class="circle"></div>
<div class="circle"></div>
</div>
""", unsafe_allow_html=True)

# ================= CLOCK =================
now = datetime.now()

st.markdown(f"""
<div class="topbar">
🕒 {now.strftime("%d %B %Y | %I:%M:%S %p")}
</div>
""", unsafe_allow_html=True)

# ================= GREETING =================
hour = now.hour

greet = "🌙 Good Evening"
if hour < 12:
    greet = "🌅 Good Morning"
elif hour < 18:
    greet = "☀️ Good Afternoon"

st.markdown(f"""
<div class="greet">{greet}</div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
<div class="hero-title">NEXUS CONTROL CENTER</div>
<div class="hero-sub">Futuristic Glass Dashboard • Neon UI • Smart System</div>
</div>
""", unsafe_allow_html=True)

# ================= SEARCH =================
search = st.text_input("🔍 Search Service")

if search:
    st.success(f"Searching: {search}")

# ================= QUOTE =================
st.info("💡 " + random.choice(quotes))

# ================= CARDS =================
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank"><div class="card"><div class="icon">📊</div><div class="title">PMY Verify</div><div class="desc">Verification System</div><div class="btn">Open</div></div></a>

<a href="{link2}" target="_blank"><div class="card"><div class="icon">🏦</div><div class="title">BOP</div><div class="desc">Bank Portal</div><div class="btn">Open</div></div></a>

<a href="{link3}" target="_blank"><div class="card"><div class="icon">📁</div><div class="title">ACAG</div><div class="desc">Batch Data</div><div class="btn">Open</div></div></a>

<a href="{link4}" target="_blank"><div class="card"><div class="icon">📲</div><div class="title">PMY Apply</div><div class="desc">Online Apply</div><div class="btn">Open</div></div></a>

<a href="{link5}" target="_blank"><div class="card"><div class="icon">📝</div><div class="title">ACAG Apply</div><div class="desc">Application</div><div class="btn">Open</div></div></a>

<a href="{link6}" target="_blank"><div class="card"><div class="icon">🚀</div><div class="title">Recovery</div><div class="desc">Dashboard</div><div class="btn">Open</div></div></a>

</div>
""", unsafe_allow_html=True)

# ================= ULTRA STATS =================
st.markdown(f"""
<div class="ultra">

<div class="ucard"><div class="num">99%</div><p>System Health</p></div>

<div class="ucard"><div class="num">06</div><p>Services</p></div>

<div class="ucard"><div class="num">24/7</div><p>Active</p></div>

<div class="ucard"><div class="num">{st.session_state.visits}</div><p>Visits</p></div>

</div>
""", unsafe_allow_html=True)

# ================= TICKER =================
st.markdown("""
<div class="ticker">
<div class="scroll">
⚡ System Online • ACAG Updated • PMY Active • Recovery Live • AI Dashboard Running 🚀
</div>
</div>
""", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
⚡ NEXUS CONTROL CENTER • Built with Streamlit • 2026
</div>
""", unsafe_allow_html=True)
