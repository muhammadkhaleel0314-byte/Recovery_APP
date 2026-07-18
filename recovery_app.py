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
link8 = "#"  # Link khali hone par reload rokne ke liye '#' lagaya hai

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at center, #0a1128 0%, #050816 100%);
    overflow-x: hidden;
    font-family: 'Inter', sans-serif;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 2rem;
    max-width: 1400px;
}

/* Background Glowing Circles */
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
    filter: blur(80px); /* Soft blur filter for beautiful glow */
    animation: float 14s infinite ease-in-out;
}

.circle:nth-child(1){
    width: 400px;
    height: 400px;
    left: -5%;
    top: 10%;
    background: rgba(0, 229, 255, 0.06);
}

.circle:nth-child(2){
    width: 350px;
    height: 350px;
    right: -5%;
    top: 30%;
    background: rgba(139, 92, 246, 0.08);
}

.circle:nth-child(3){
    width: 300px;
    height: 300px;
    left: 40%;
    bottom: 5%;
    background: rgba(59, 130, 246, 0.06);
}

@keyframes float {
    0% { transform: translateY(0px) scale(1); }
    50% { transform: translateY(-30px) scale(1.05); }
    100% { transform: translateY(0px) scale(1); }
}

/* Cards Grid Layout */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
    padding: 20px 0;
}

/* Premium Card Design */
.card {
    position: relative;
    overflow: hidden;
    padding: 30px;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    min-height: 250px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}

.card:hover {
    transform: translateY(-10px);
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(0, 229, 255, 0.3);
    box-shadow: 0 30px 60px rgba(0, 229, 255, 0.1);
}

/* Smooth color shift on hover for elements inside the card */
.card:hover .card-title {
    background: linear-gradient(to right, #ffffff, #00e5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card:hover .card-btn {
    background: linear-gradient(90deg, #00e5ff, #8b5cf6);
    color: white;
    box-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
}

.card-icon {
    width: 65px;
    height: 65px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.05);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin-bottom: 20px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    color: white;
    margin-bottom: 8px;
    transition: all 0.3s ease;
}

.card-desc {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 20px;
}

.card-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.06);
    color: #cbd5e1;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s ease;
    align-self: flex-start;
}

a {text-decoration: none !important;}
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
