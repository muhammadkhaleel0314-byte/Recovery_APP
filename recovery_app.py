import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Vision X Control Hub",
    page_icon="⚡",
    layout="wide"
)

# =========================
# COMPACT MODE
# =========================
compact = st.toggle("⚡ Compact Mode")

CARD_PADDING = "22px" if compact else "35px"
TITLE_SIZE = "58px" if compact else "82px"

# =========================
# GOOGLE FONTS
# =========================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# =========================
# PREMIUM CSS
# =========================
st.markdown(f"""
<style>

/* Hide Streamlit */
#MainMenu{{visibility:hidden;}}
footer{{visibility:hidden;}}
header{{visibility:hidden;}}

.block-container{{
max-width:1600px;
padding-top:1rem;
}}

html,body{{
overflow-x:hidden;
}}

/* =========================
BACKGROUND
========================= */

.stApp{{
background:
radial-gradient(circle at 10% 20%, rgba(0,255,255,.12), transparent 25%),
radial-gradient(circle at 90% 10%, rgba(168,85,247,.12), transparent 25%),
radial-gradient(circle at 50% 90%, rgba(236,72,153,.10), transparent 30%),
linear-gradient(135deg,#030712,#050816,#0f172a);

background-size:200% 200%;
animation:bgMove 18s ease infinite;
}}

@keyframes bgMove{{
0%{{background-position:0% 50%;}}
50%{{background-position:100% 50%;}}
100%{{background-position:0% 50%;}}
}}

/* =========================
PARTICLES
========================= */

.particles{{
position:fixed;
inset:0;
pointer-events:none;
z-index:-1;

background-image:
radial-gradient(#00f5ff 1px, transparent 1px);

background-size:80px 80px;

opacity:.08;

animation:particleMove 60s linear infinite;
}}

@keyframes particleMove{{
from{{transform:translateY(0);}}
to{{transform:translateY(-1200px);}}
}}

/* =========================
FLOATING LIGHTS
========================= */

.light{{
position:fixed;
border-radius:50%;
filter:blur(120px);
z-index:-1;
animation:float 12s ease-in-out infinite;
}}

.light1{{
width:350px;
height:350px;
background:#00f5ff33;
left:-100px;
top:-50px;
}}

.light2{{
width:300px;
height:300px;
background:#8b5cf633;
right:-80px;
bottom:-80px;
}}

.light3{{
width:250px;
height:250px;
background:#ec489933;
left:40%;
bottom:-100px;
}}

@keyframes float{{
0%{{transform:translateY(0px);}}
50%{{transform:translateY(-40px);}}
100%{{transform:translateY(0px);}}
}}

/* =========================
HERO
========================= */

.hero{{
position:relative;
overflow:hidden;

padding:70px;

border-radius:40px;

background:rgba(255,255,255,.05);

backdrop-filter:blur(25px);

border:1px solid rgba(255,255,255,.08);

box-shadow:
0 0 50px rgba(0,255,255,.08),
0 0 120px rgba(168,85,247,.08);

margin-bottom:45px;
}}

.hero::before{{
content:'';

position:absolute;

width:500px;
height:500px;

background:
linear-gradient(
45deg,
#00f5ff,
#8b5cf6,
#ff4fd8
);

border-radius:50%;

filter:blur(150px);

right:-180px;
top:-180px;

opacity:.35;
}}

.hero-title{{
font-family:'Orbitron',sans-serif;

font-size:{TITLE_SIZE};

font-weight:900;

line-height:.95;

letter-spacing:2px;

margin-bottom:15px;

background:
linear-gradient(
90deg,
#ffffff,
#00f5ff,
#a855f7
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}}

.hero-sub{{
font-family:'Rajdhani',sans-serif;

font-size:22px;

color:#cbd5e1;

margin-bottom:30px;
}}

.hero-chip{{
display:inline-block;

padding:14px 28px;

border-radius:18px;

font-weight:700;

font-family:'Rajdhani',sans-serif;

background:
linear-gradient(
90deg,
#00f5ff,
#8b5cf6
);

color:white;

box-shadow:
0 10px 30px rgba(0,245,255,.35);
}}

</style>
""", unsafe_allow_html=True)

# Background Elements
st.markdown("""
<div class="particles"></div>

<div class="light light1"></div>
<div class="light light2"></div>
<div class="light light3"></div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">

<div class="hero-title">
VISION X<br>
CONTROL HUB
</div>

<div class="hero-sub">
Apple-Level Luxury UI • Cyberpunk Neon Effects • Premium Dashboard Experience
</div>

<div class="hero-chip">
⚡ ALL SYSTEMS ONLINE
</div>

</div>
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
# CARD CSS
# =========================

st.markdown(f"""
<style>

.grid {{
display:grid;
grid-template-columns:
repeat(auto-fit,minmax(320px,1fr));
gap:30px;
margin-top:20px;
}}

.card {{
position:relative;
overflow:hidden;

padding:{CARD_PADDING};

border-radius:34px;

background:
rgba(255,255,255,.05);

backdrop-filter:blur(20px);

min-height:270px;

transition:.45s ease;

text-decoration:none;

border:1px solid rgba(255,255,255,.06);
}}

.card::before {{
content:'';

position:absolute;

inset:-2px;

border-radius:34px;

background:
linear-gradient(
90deg,
#00f5ff,
#8b5cf6,
#ff4fd8,
#00f5ff
);

background-size:400% 400%;

animation:borderMove 8s linear infinite;

z-index:-2;
}}

.card::after {{
content:'';

position:absolute;

inset:2px;

background:#0b1220;

border-radius:32px;

z-index:-1;
}}

@keyframes borderMove {{

0% {{
background-position:0% 50%;
}}

100% {{
background-position:400% 50%;
}}

}}

.card:hover {{

transform:
translateY(-15px)
scale(1.04);

box-shadow:
0 0 15px #00ffcc,
0 0 35px rgba(0,255,204,.45),
0 0 65px rgba(139,92,246,.30);

}}

.card-icon {{

width:90px;
height:90px;

display:flex;
align-items:center;
justify-content:center;

font-size:45px;

border-radius:26px;

margin-bottom:25px;

background:
linear-gradient(
145deg,
rgba(255,255,255,.15),
rgba(255,255,255,.05)
);

border:
1px solid rgba(255,255,255,.12);

box-shadow:
0 0 25px rgba(255,255,255,.08);

}}

.card-title {{

font-family:'Orbitron',sans-serif;

font-size:30px;

font-weight:700;

color:white;

margin-bottom:12px;

}}

.card-desc {{

font-family:'Rajdhani',sans-serif;

font-size:17px;

line-height:1.8;

color:#cbd5e1;

margin-bottom:25px;

}}

.card-btn {{

display:inline-flex;

align-items:center;

gap:10px;

padding:14px 24px;

border-radius:16px;

font-family:'Rajdhani',sans-serif;

font-weight:700;

background:
rgba(255,255,255,.08);

color:white;

transition:.3s;

}}

.card:hover .card-btn {{

background:white;
color:black;

}}

.card-btn span {{

display:inline-block;

}}

.card:hover .card-btn span {{

animation:
arrowMove .8s infinite;

}}

@keyframes arrowMove {{

0% {{
transform:translateX(0);
}}

50% {{
transform:translateX(8px);
}}

100% {{
transform:translateX(0);
}}

}}

.card-link {{
text-decoration:none !important;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# CARDS
# =========================

st.markdown(f"""

<div class="grid">

<a href="{link1}" target="_blank" class="card-link">

<div class="card">

<div class="card-icon">📊</div>

<div class="card-title">
PMY Verify
</div>

<div class="card-desc">
Advanced PMY verification portal with secure access,
fast processing and premium dashboard experience.
</div>

<div class="card-btn">
Open Portal <span>→</span>
</div>

</div>

</a>


<a href="{link2}" target="_blank" class="card-link">

<div class="card">

<div class="card-icon">🏦</div>

<div class="card-title">
BOP Account
</div>

<div class="card-desc">
Manage banking services, customer information
and account related operations quickly.
</div>

<div class="card-btn">
Open Portal <span>→</span>
</div>

</div>

</a>


<a href="{link3}" target="_blank" class="card-link">

<div class="card">

<div class="card-icon">📁</div>

<div class="card-title">
ACAG Batch
</div>

<div class="card-desc">
Monitor uploaded batches, processing updates
and workflow tracking in real time.
</div>

<div class="card-btn">
Open Portal <span>→</span>
</div>

</div>

</a>


<a href="{link4}" target="_blank" class="card-link">

<div class="card">

<div class="card-icon">📲</div>

<div class="card-title">
PMY Apply
</div>

<div class="card-desc">
Apply online and track your application
through the complete digital journey.
</div>

<div class="card-btn">
Open Portal <span>→</span>
</div>

</div>

</a>


<a href="{link5}" target="_blank" class="card-link">

<div class="card">

<div class="card-icon">📝</div>

<div class="card-title">
ACAG Apply
</div>

<div class="card-desc">
Modern application workflow with
simplified forms and smart processing.
</div>

<div class="card-btn">
Open Portal <span>→</span>
</div>

</div>

</a>


<a href="{link6}" target="_blank" class="card-link">

<div class="card">

<div class="card-icon">🚀</div>

<div class="card-title">
QR Generator
</div>

<div class="card-desc">
Generate professional QR codes with
advanced options and instant results.
</div>

<div class="card-btn">
Open Portal <span>→</span>
</div>

</div>

</a>

</div>

""", unsafe_allow_html=True)
# =========================
# FINAL CSS
# =========================

st.markdown("""
<style>

/* =========================
LUXURY TICKER
========================= */

.ticker-wrap{

margin-top:45px;

overflow:hidden;

border-radius:28px;

padding:20px 0;

background:
rgba(255,255,255,.05);

border:
1px solid rgba(255,255,255,.08);

backdrop-filter:blur(20px);

box-shadow:
0 0 40px rgba(0,255,255,.08);

}

.ticker{

display:inline-block;

white-space:nowrap;

padding-left:100%;

font-family:'Rajdhani',sans-serif;

font-size:22px;

font-weight:700;

letter-spacing:1px;

color:#00f5ff;

animation:
tickerMove 18s linear infinite;

}

@keyframes tickerMove{

0%{
transform:translateX(0);
}

100%{
transform:translateX(-100%);
}

}

/* =========================
STATS SECTION
========================= */

.stats{

display:grid;

grid-template-columns:
repeat(auto-fit,minmax(230px,1fr));

gap:25px;

margin-top:40px;

}

.stat{

position:relative;

overflow:hidden;

padding:35px;

border-radius:28px;

background:
rgba(255,255,255,.05);

border:
1px solid rgba(255,255,255,.08);

backdrop-filter:blur(20px);

transition:.4s ease;

}

.stat::before{

content:'';

position:absolute;

width:180px;
height:180px;

border-radius:50%;

background:
rgba(255,255,255,.05);

top:-80px;
right:-80px;

}

.stat:hover{

transform:
translateY(-10px);

box-shadow:
0 0 20px rgba(0,255,255,.20),
0 0 45px rgba(139,92,246,.15);

}

.stat h1{

font-family:'Orbitron',sans-serif;

font-size:64px;

font-weight:900;

color:white;

margin:0;

}

.stat p{

font-family:'Rajdhani',sans-serif;

font-size:15px;

font-weight:300;

letter-spacing:1px;

color:#cbd5e1;

margin-top:10px;

}

/* =========================
FOOTER
========================= */

.footer{

margin-top:60px;

padding:25px;

text-align:center;

border-radius:22px;

background:
rgba(255,255,255,.04);

border:
1px solid rgba(255,255,255,.08);

backdrop-filter:blur(15px);

font-family:'Rajdhani',sans-serif;

color:#94a3b8;

font-size:15px;

}

/* =========================
HOVER GLOW
========================= */

.hero:hover{

box-shadow:
0 0 60px rgba(0,255,255,.12),
0 0 140px rgba(139,92,246,.12);

}

/* =========================
RESPONSIVE
========================= */

@media(max-width:768px){

.hero{
padding:35px;
}

.hero-title{
font-size:48px !important;
}

.hero-sub{
font-size:18px;
}

.card-title{
font-size:24px;
}

.card-icon{
width:75px;
height:75px;
font-size:38px;
}

.stat h1{
font-size:46px;
}

.ticker{
font-size:18px;
}

}

</style>
""", unsafe_allow_html=True)

# =========================
# PREMIUM TICKER
# =========================

st.markdown("""
<div class="ticker-wrap">

<div class="ticker">

⚡ ACAG Batch 31 Updated • PMY Services Active •
Secure Dashboard Online • All Systems Operational •
Premium Cyber Dashboard Running • QR Generator Ready •
Banking Services Available • Vision X Control Hub Live 🚀

</div>

</div>
""", unsafe_allow_html=True)

# =========================
# STATS
# =========================

st.markdown("""

<div class="stats">

<div class="stat">
<h1>06</h1>
<p>QUICK SERVICES</p>
</div>

<div class="stat">
<h1>24/7</h1>
<p>AVAILABILITY</p>
</div>

<div class="stat">
<h1>99%</h1>
<p>FAST PERFORMANCE</p>
</div>

<div class="stat">
<h1>⚡</h1>
<p>PREMIUM EXPERIENCE</p>
</div>

</div>
