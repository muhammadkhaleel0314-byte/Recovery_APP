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
link8 = "https://script.google.com/macros/s/AKfycby0KPJpLMZRefof7j36uPISPxNeuUzG6SvsPg1UoS0Y5yGSmUcXJScwqj0M4YH0xg6q/exec"

# ================= AUDIO & JAVASCRIPT CONTROLLER =================
# Yeh script har card click par bina kisi delay ke sound play karegi
st.markdown("""
<audio id="click-sound" preload="auto">
    <source src="https://assets.mixkit.co/active_storage/sfx/2568/2568-84.wav" type="audio/wav">
</audio>

<script>
function playSound() {
    var sound = document.getElementById("click-sound");
    sound.currentTime = 0;
    sound.play();
}
</script>
""", unsafe_allow_html=True)

# ================= CSS (MINIMAL & FLAT THEME) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(180deg, #0b0f19 0%, #06080c 100%);
    overflow-x: hidden;
    font-family: 'Inter', sans-serif;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 3rem;
    max-width: 1400px;
}

/* Responsive Clean Grid */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
    gap: 24px;
    padding: 20px 0;
}

/* Minimal Flat Card */
.card {
    padding: 30px;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.25s ease-in-out;
    min-height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
}

/* Subtle Hover Effect */
.card:hover {
    background: rgba(255, 255, 255, 0.04);
    border-color: rgba(255, 255, 255, 0.15);
    transform: translateY(-4px);
}

.card-icon {
    font-size: 28px;
    margin-bottom: 16px;
}

.card-title {
    font-size: 20px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 8px;
}

.card-desc {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.5;
    margin-bottom: 20px;
}

/* Simple Clean Link Button */
.card-btn {
    display: inline-flex;
    align-items: center;
    color: #38bdf8;
    font-size: 14px;
    font-weight: 500;
    transition: color 0.2s ease;
}

.card:hover .card-btn {
    color: #ffffff;
}

a {text-decoration: none !important;}
</style>
""", unsafe_allow_html=True)

# ================= CARDS WITH AUDIO TRIGGER =================
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank" onclick="playSound()">
<div class="card">
    <div>
        <div class="card-icon">📊</div>
        <div class="card-title">PMY Verify</div>
        <div class="card-desc">Advanced PMY verification system with secure instant access.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link2}" target="_blank" onclick="playSound()">
<div class="card">
    <div>
        <div class="card-icon">🏦</div>
        <div class="card-title">BOP Account</div>
        <div class="card-desc">Manage banking details and services with smart access.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link3}" target="_blank" onclick="playSound()">
<div class="card">
    <div>
        <div class="card-icon">📁</div>
        <div class="card-title">ACAG Batch</div>
        <div class="card-desc">Track and monitor latest ACAG batch processing data.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link4}" target="_blank" onclick="playSound()">
<div class="card">
    <div>
        <div class="card-icon">📲</div>
        <div class="card-title">PMY Apply</div>
        <div class="card-desc">Apply online and track PMY applications instantly.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link5}" target="_blank" onclick="playSound()">
<div class="card">
    <div>
        <div class="card-icon">📝</div>
        <div class="card-title">ACAG Apply</div>
        <div class="card-desc">Smart ACAG application workflow with modern interface.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link6}" target="_blank" onclick="playSound()">
<div class="card">
    <div>
        <div class="card-icon">🚀</div>
        <div class="card-title">QR Generator</div>
        <div class="card-desc">Generate stylish QR codes with advanced functionality.</div>
    </div>
    <div class="card-btn">Open Portal →</div>
</div>
</a>

<a href="{link7}" target="_blank" onclick="playSound()">
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
<a href="{link8}" target="_blank" onclick="playSound()">
<div class="card">
    <div>
        <div class="card-icon">🌐</div>
        <div class="card-title">Bop Verify List</div>
        <div class="card-desc">Access additional and features securely.</div>
    </div>
    <div class="card-btn">→</div>
</div>
</a>

</div>
""", unsafe_allow_html=True)
