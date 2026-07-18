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

# ================= CSS (LUXURY AURORA THEME) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cabinet+Grotesk:wght@700;800&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

.stApp {
    background: #020205;
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

/* Luxury Aurora Animated Background */
.bg-animation {
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: -1;
    overflow: hidden;
    background: #040209;
}

.aurora {
    position: absolute;
    width: 800px;
    height: 800px;
    border-radius: 50%;
    filter: blur(160px);
    opacity: 0.35;
    mix-blend-mode: screen;
    animation: aurora-move 25s infinite alternate ease-in-out;
}

.aurora-1 {
    top: -20%;
    left: -10%;
    background: radial-gradient(circle, #7c3aed 0%, transparent 70%);
}

.aurora-2 {
    bottom: -20%;
    right: -10%;
    background: radial-gradient(circle, #059669 0%, transparent 70%);
    animation-delay: -5s;
}

.aurora-3 {
    top: 40%;
    left: 50%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, #db2777 0%, transparent 70%);
    animation-delay: -10s;
}

@keyframes aurora-move {
    0% { transform: translate(0px, 0px) scale(1) rotate(0deg); }
    50% { transform: translate(80px, 50px) scale(1.15) rotate(180deg); }
    100% { transform: translate(-40px, 90px) scale(0.9) rotate(360deg); }
}

/* Grid Layout */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
    gap: 30px;
    padding: 20px 0;
}

/* Premium Matte Glass Cards */
.card {
    position: relative;
    padding: 35px 30px;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    min-height: 265px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255,255,255,0.1);
}

/* Card Hover Unique Interaction */
.card:hover {
    transform: translateY(-8px) scale(1.01);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 40px 80px rgba(0, 0, 0, 0.8), 
                0 0 40px rgba(124, 58, 237, 0.15);
}

.card:hover .card-title {
    color: #ffffff;
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}

/* Minimalist Icon Base */
.card-icon {
    width: 52px;
    height: 52px;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 25px;
    transition: all 0.4s ease;
}

.card:hover .card-icon {
    background: #ffffff;
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(255, 255, 255, 0.2);
}

/* Titles & Text styling */
.card-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 23px;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 10px;
    letter-spacing: -0.3px;
    transition: all 0.3s ease;
}

.card-desc {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 25px;
}

/* Border Glow Style Button */
.card-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 11px 22px;
    border-radius: 14px;
    background: transparent;
    color: #ffffff;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid rgba(255, 255, 255, 0.15);
    transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
    align-self: flex-start;
}

.card:hover .card-btn {
    background: #ffffff;
    color: #020205;
    border-color: #ffffff;
    box-shadow: 0 10px 20px rgba(255, 255, 255, 0.15);
}

a {text-decoration: none !important;}
</style>
""", unsafe_allow_html=True)

# ================= BACKGROUND =================
st.markdown("""
<div class="bg-animation">
    <div class="aurora aurora-1"></div>
    <div class="aurora aurora-2"></div>
    <div class="aurora aurora-3"></div>
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
