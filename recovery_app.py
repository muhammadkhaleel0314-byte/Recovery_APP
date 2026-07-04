import streamlit as st
import streamlit as st

st.error("🚫Temparory Blocked")
st.stop()
# ================= LINKS =================
link1 = "https://script.google.com/macros/s/AKfycbytHXuAQ1_ps2by_3uatCoGkc_tcy5_YMQfSBMeMxw0ZrhSZlYjC8Wk_z8RgdwPTWqy/exec"
link2 = "https://script.google.com/macros/s/AKfycbwvtLEuEivUZGCYylcrwnF9jjbwFT7gqlQEdsAASRCiJiNolICfIIrz5BzqaqTgtSqV/exec"
link3 = "https://script.google.com/macros/s/AKfycbxP-tH7L2kN5w0ApiQfC7ZPzh0nZZGsO1-u7XcfPdx2C-nSyTHLasA2cv6eozXAujzGFw/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"

# ================= NEW LINK =================
link7 = "https://script.google.com/macros/s/AKfycbxV3wH_XQL4tjXY20kVgJs80zW3P4zQ1bVsZDbSiS74YM6afkPZk2FoWAM9QVPQOfsUCQ/exec"

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background: #050816;
    overflow-x:hidden;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 1rem;
    max-width: 1500px;
}

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
}

.grid {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:28px;
}

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
}

.card-title {
    font-size:28px;
    font-weight:800;
    color:white;
}

.card-desc {
    color:#d1d5db;
    font-size:15px;
    margin-bottom:24px;
}

.card-btn {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:10px;
    padding:5px 10px;
    border-radius:20px;
    background:rgba(255,255,255,0.10);
    color:white;
    font-weight:200;
}

a {text-decoration:none !important;}
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

# ================= CARDS =================
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank">
<div class="card">
<div class="card-icon">📊</div>
<div class="card-title">PMY Verify</div>
<div class="card-desc">Advanced PMY verification system with secure instant access.</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link2}" target="_blank">
<div class="card">
<div class="card-icon">🏦</div>
<div class="card-title">BOP Account</div>
<div class="card-desc">Manage banking details and services with smart access.</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link3}" target="_blank">
<div class="card">
<div class="card-icon">📁</div>
<div class="card-title">ACAG Batch</div>
<div class="card-desc">Track and monitor latest ACAG batch processing data.</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link4}" target="_blank">
<div class="card">
<div class="card-icon">📲</div>
<div class="card-title">PMY Apply</div>
<div class="card-desc">Apply online and track PMY applications instantly.</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link5}" target="_blank">
<div class="card">
<div class="card-icon">📝</div>
<div class="card-title">ACAG Apply</div>
<div class="card-desc">Smart ACAG application workflow with modern interface.</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link6}" target="_blank">
<div class="card">
<div class="card-icon">🚀</div>
<div class="card-title">QR Generator</div>
<div class="card-desc">Generate stylish QR codes with advanced functionality.</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

<!-- ================= NEW CARD ================= -->
<a href="{link7}" target="_blank">
<div class="card">
<div class="card-icon">🔗</div>
<div class="card-title">New Service</div>
<div class="card-desc">Pmy Adress List Just enter city name and take list pdf.</div>
<div class="card-btn">Open Portal →</div>
</div>
</a>

</div>
""", unsafe_allow_html=True)
