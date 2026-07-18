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

# ================= CSS (PREMIUM UNIQUE THEME) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #030712;
    overflow-x: hidden;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 3rem;
    max-width: 1400px;
}

/* Unique Mesh Gradient Background Glows */
.bg-animation {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: -1;
    overflow: hidden;
}

.glow-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(140px);
    opacity: 0.45;
    mix-blend-mode: screen;
    animation: floatAround 20s infinite alternate ease-in-out;
}

.glow-orb:nth-child(1) {
    width: 600px;
    height: 600px;
    top: -10%, left: -10%;
    background: radial-gradient(circle, #4f46e5 0%, transparent 80%);
}

.glow-orb:nth-child(2) {
    width: 500px;
    height: 500px;
    bottom: -10%, right: -10%;
    background: radial-gradient(circle, #06b6d4 0%, transparent 80%);
}

@keyframes floatAround {
    0% { transform: translate(0px, 0px) scale(1); }
    100% { transform: translate(50px, 30px) scale(1.1); }
}

/* Responsive Grid */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
    gap: 30px;
    padding: 20px 0;
}

/* Glassmorphic Cyber-Minimalist Card */
.card {
    position: relative;
    padding: 35px 30px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(17, 24, 39, 0.7) 0%, rgba(11, 17, 30, 0.9) 100%);
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    min-height: 270px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
}

/* Card Hover Unique Effects */
.card:hover {
    transform: translateY(-8px);
    border: 1px solid rgba(79, 70, 229, 0.4);
    box-shadow: 0 30px 60px rgba(79, 70, 229, 0.15), inset 0 0 20px rgba(79, 70, 229, 0.1);
}

.card:hover .card-title {
    color: #a5b4fc;
}

/* Futuristic Floating Icon */
.card-icon {
    width: 56px;
    height: 56px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    margin-bottom: 25px;
    transition: all 0.3s ease;
}

.card:hover .card-icon {
    background: rgba(79, 70, 229, 0.15);
    border-color: rgba(79, 70, 229, 0.3);
    transform: scale(1.05) rotate(5deg);
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
    letter-spacing: -0.5px;
    transition: color 0.3s ease;
}

.card-desc {
    color: #9ca3af;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 25px;
    font-weight: 400;
}

/* Clean Minimal Button Styling */
.card-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 12px 24px;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.04);
    color: #f3f4f6;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid rgba(255, 255, 255, 0.08);
    transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    align-self: flex-start;
}

.card:hover .card-btn {
    background: #4f46e5;
    color: #ffffff;
    border-color: #4f46e5;
    box-shadow: 0 10px 25px rgba(79, 70, 229, 0.35);
}

a {text-decoration: none !important;}
</style>
""", unsafe_allow_html=True)

# ================= BACKGROUND =================
st.markdown("""
<div class="bg-animation">
    <div class="glow-orb"></div>
    <div class="glow-orb"></div>
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
