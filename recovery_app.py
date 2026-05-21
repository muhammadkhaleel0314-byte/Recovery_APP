import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Vision X Dashboard",
    page_icon="⚡",
    layout="wide"
)

# =========================
# MODE TOGGLE
# =========================
compact = st.toggle("⚡ Compact Mode")

CARD_PADDING = "22px" if compact else "35px"
TITLE_SIZE = "60px" if compact else "80px"

# =========================
# FONTS
# =========================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# =========================
# LINKS
# =========================
link1 = "https://script.google.com/macros/s/AKfycbzlyx-OPgSTo-FsevohLyr9UfVSyWsVZk6tUGTVQgIFCNWxw0G6PuvnrqBnj1OPkCGq8g/exec"
link2 = "https://script.google.com/macros/s/AKfycbwvtLEuEivUZGCYylcrwnF9jjbwFT7gqlQEdsAASRCiJiNolICfIIrz5BzqaqTgtSqV/exec"
link3 = "https://script.google.com/macros/s/AKfycbxP-tH7L2kN5w0ApiQfC7ZPzh0nZZGsO1-u7XcfPdx2C-nSyTHLasA2cv6eozXAujzGFw/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"

# =========================
# CSS
# =========================
st.markdown(f"""
<style>

/* Hide Streamlit */
#MainMenu, footer, header {{
visibility:hidden;
}}

.block-container {{
max-width:1500px;
padding-top:1rem;
}}

/* BACKGROUND */
.stApp {{
background:
radial-gradient(circle at 10% 20%, rgba(0,255,255,0.15), transparent 25%),
radial-gradient(circle at 80% 30%, rgba(139,92,246,0.15), transparent 25%),
linear-gradient(135deg,#050816,#070b14,#0a0f1f);
overflow-x:hidden;
}}

/* HERO */
.hero {{
padding:60px;
border-radius:35px;
background:rgba(255,255,255,0.05);
backdrop-filter:blur(20px);
border:1px solid rgba(255,255,255,0.08);
margin-bottom:40px;
}}

.hero-title {{
font-family:'Orbitron',sans-serif;
font-size:{TITLE_SIZE};
font-weight:900;
background:linear-gradient(90deg,#fff,#00e5ff,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}}

.hero-sub {{
font-family:'Rajdhani',sans-serif;
color:#cbd5e1;
font-size:20px;
}}

/* GRID */
.grid {{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
gap:25px;
}}

/* CARD */
.card {{
padding:{CARD_PADDING};
border-radius:30px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
backdrop-filter:blur(20px);
transition:0.4s;
text-decoration:none;
color:white;
}}

.card:hover {{
transform:translateY(-12px) scale(1.03);
box-shadow:0 0 25px rgba(0,255,255,0.25);
}}

.card-icon {{
font-size:40px;
margin-bottom:15px;
}}

.card-title {{
font-family:'Orbitron',sans-serif;
font-size:24px;
font-weight:700;
}}

.card-desc {{
font-family:'Rajdhani',sans-serif;
color:#cbd5e1;
margin-top:10px;
}}

.card-btn {{
margin-top:15px;
display:inline-block;
padding:10px 18px;
border-radius:12px;
background:rgba(255,255,255,0.1);
}}

/* TICKER */
.ticker {{
margin-top:30px;
padding:15px;
border-radius:20px;
background:rgba(255,255,255,0.05);
overflow:hidden;
white-space:nowrap;
animation:move 15s linear infinite;
color:#00e5ff;
}}

@keyframes move {{
0% {{transform:translateX(100%);}}
100% {{transform:translateX(-100%);}}
}}

/* STATS */
.stats {{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:20px;
margin-top:40px;
}}

.stat {{
padding:25px;
border-radius:20px;
background:rgba(255,255,255,0.05);
text-align:center;
}}

.stat h1 {{
font-family:'Orbitron';
font-size:40px;
color:white;
}}

.stat p {{
color:#cbd5e1;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown(f"""
<div class="hero">
<div class="hero-title">VISION X DASHBOARD</div>
<div class="hero-sub">Ultra Clean • Neon Modern UI • Streamlit Powered</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CARDS
# =========================
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank" class="card">
<div class="card-icon">📊</div>
<div class="card-title">PMY Verify</div>
<div class="card-desc">Verification System</div>
<div class="card-btn">Open</div>
</a>

<a href="{link2}" target="_blank" class="card">
<div class="card-icon">🏦</div>
<div class="card-title">BOP Account</div>
<div class="card-desc">Banking Access</div>
<div class="card-btn">Open</div>
</a>

<a href="{link3}" target="_blank" class="card">
<div class="card-icon">📁</div>
<div class="card-title">ACAG Batch</div>
<div class="card-desc">Batch Tracking</div>
<div class="card-btn">Open</div>
</a>

<a href="{link4}" target="_blank" class="card">
<div class="card-icon">📲</div>
<div class="card-title">PMY Apply</div>
<div class="card-desc">Application Portal</div>
<div class="card-btn">Open</div>
</a>

<a href="{link5}" target="_blank" class="card">
<div class="card-icon">📝</div>
<div class="card-title">ACAG Apply</div>
<div class="card-desc">Form System</div>
<div class="card-btn">Open</div>
</a>

<a href="{link6}" target="_blank" class="card">
<div class="card-icon">🚀</div>
<div class="card-title">QR Generator</div>
<div class="card-desc">QR Tools</div>
<div class="card-btn">Open</div>
</a>

</div>
""", unsafe_allow_html=True)

# =========================
# TICKER
# =========================
st.markdown("""
<div class="ticker">
⚡ SYSTEM ACTIVE • ALL SERVICES ONLINE • DASHBOARD RUNNING SMOOTHLY 🚀
</div>
""", unsafe_allow_html=True)

# =========================
# STATS
# =========================
st.markdown("""
<div class="stats">

<div class="stat">
<h1>06</h1>
<p>Services</p>
</div>

<div class="stat">
<h1>24/7</h1>
<p>Active</p>
</div>

<div class="stat">
<h1>99%</h1>
<p>Fast</p>
</div>

<div class="stat">
<h1>⚡</h1>
<p>Premium</p>
</div>

</div>
""", unsafe_allow_html=True)
