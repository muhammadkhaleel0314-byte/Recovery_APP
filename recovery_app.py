import streamlit as st

# ================= LINKS =================
link1 = "https://script.google.com/macros/s/AKfycbytHXuAQ1_ps2by_3uatCoGkc_tcy5_YMQfSBMeMxw0ZrhSZlYjC8Wk_z8RgdwPTWqy/exec"
link2 = "https://script.google.com/macros/s/AKfycbwvtLEuEivUZGCYylcrwnF9jjbwFT7gqlQEdsAASRCiJiNolICfIIrz5BzqaqTgtSqV/exec"
link3 = "https://script.google.com/macros/s/AKfycbxP-tH7L2kN5w0ApiQfC7ZPzh0nZZGsO1-u7XcfPdx2C-nSyTHLasA2cv6eozXAujzGFw/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"

# ================= NEW LINKS =================
link7 = "https://script.google.com/macros/s/AKfycbxV3wH_XQL4tjXY20kVgJs80zW3P4zQ1bVsZDbSiS74YM6afkPZk2FoWAM9QVPQOfsUCQ/exec"
link8 = "#"

# ================= CSS (CYBER-GRID MINI THEME) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Plus+Jakarta+Sans:wght@400;600&display=swap');

.stApp {
    background: #080710;
    overflow-x: hidden;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 4rem;
    max-width: 1400px;
}

/* Abstract Tech Background */
.bg-animation {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: -1;
    overflow: hidden;
    background: radial-gradient(circle at 80% 20%, #151032 0%, #080710 100%);
}

.mesh-glow {
    position: absolute;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
    top: 20%;
    left: 20%;
    filter: blur(120px);
}

/* Grid Layout */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
    gap: 30px;
    padding: 20px 0;
}

/* Cyber-Minimalist Card */
.card {
    position: relative;
    padding: 35px 30px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    min-height: 260px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Sleek Hover Effect */
.card:hover {
    transform: scale(1.02);
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(99, 102, 241, 0.5);
    box-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.25);
}

.card-icon {
    width: 50px;
    height: 50px;
    border-radius: 14px;
    background: rgba(99, 102, 241, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 25px;
    color: #8b5cf6;
    border: 1px solid rgba(99, 102, 241, 0.2);
    transition: transform 0.3s ease;
}

.card:hover .card-icon {
    transform: rotate(-5deg) scale(1.1);
    background: #6366f1;
    color: white;
}

.card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
}

.card-desc {
    color: #9ca3af;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 25px;
}

/* Minimal Text Button */
.card-btn {
    font-family: 'Space Grotesk', sans-serif;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #a5b4fc;
    font-size: 14px;
    font-weight: 600;
    transition: color 0.3s ease, transform 0.3s ease;
}

.card:hover .card-btn {
    color: #ffffff;
    transform: translateX(5px);
}

a {text-decoration: none !important;}
</style>
""", unsafe_allow_html=True)

# ================= BACKGROUND =================
st.markdown("""
<div class="bg-animation">
    <div class="mesh-glow"></div>
</div>
""", unsafe_allow_html=True)

# ================= CARDS =================
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">📊</div>
        <div class="card-title">PMY Verify</div>
        <div class="card-desc">Advanced PMY verification system with secure instant access.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link2}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">🏦</div>
        <div class="card-title">BOP Account</div>
        <div class="card-desc">Manage banking details and services with smart access.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link3}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">📁</div>
        <div class="card-title">ACAG Batch</div>
        <div class="card-desc">Track and monitor latest ACAG batch processing data.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link4}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">📲</div>
        <div class="card-title">PMY Apply</div>
        <div class="card-desc">Apply online and track PMY applications instantly.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link5}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">📝</div>
        <div class="card-title">ACAG Apply</div>
        <div class="card-desc">Smart ACAG application workflow with modern interface.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link6}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">🚀</div>
        <div class="card-title">QR Generator</div>
        <div class="card-desc">Generate stylish QR codes with advanced functionality.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link7}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">🔗</div>
        <div class="card-title">New Service</div>
        <div class="card-desc">Pmy Address List: Just enter city name and download PDF list.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<!-- ================= LINK 8 CARD ================= -->
<a href="{link8}" target="_blank">
<div class="card">
    <div>
        <div class="card-icon">🌐</div>
        <div class="card-title">More Features</div>
        <div class="card-desc">Access additional upcoming services and features securely.</div>
    </div>
    <div class="card-btn">Coming Soon →</div>
</div>
</a>

</div>
""", unsafe_allow_html=True)
