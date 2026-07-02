import streamlit as st

# ================= CODE INITIAL CONFIGURATION (MUST BE FIRST) =================
st.set_page_config(
    page_title="Premium Link Portal",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= LINKS =================
link1 = "https://script.google.com/macros/s/AKfycbytHXuAQ1_ps2by_3uatCoGkc_tcy5_YMQfSBMeMxw0ZrhSZlYjC8Wk_z8RgdwPTWqy/exec"
link2 = "https://script.google.com/macros/s/AKfycbwvtLEuEivUZGCYylcrwnF9jjbwFT7gqlQEdsAASRCiJiNolICfIIrz5BzqaqTgtSqV/exec"
link3 = "https://script.google.com/macros/s/AKfycbxP-tH7L2kN5w0ApiQfC7ZPzh0nZZGsO1-u7XcfPdx2C-nSyTHLasA2cv6eozXAujzGFw/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "https://recoveryapp-5vokdvlcfqwfefeey26nac.streamlit.app/"
link7 = "https://script.google.com/macros/s/AKfycbxV3wH_XQL4tjXY20kVgJs80zW3P4zQ1bVsZDbSiS74YM6afkPZk2FoWAM9QVPQOfsUCQ/exec"

# ================= PREMIUM UI CSS =================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
    overflow-x: hidden;
    font-family: 'Inter', sans-serif;
}
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 2rem; max-width: 1400px;}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    letter-spacing: -1px;
}
.main-subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 50px;
}

.bg-animation {position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1; overflow: hidden;}
.blur-sphere {position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.15;}
.sphere-1 {width: 400px; height: 400px; left: -10%; top: 10%; background: #00f2fe; animation: float 12s infinite ease-in-out;}
.sphere-2 {width: 500px; height: 500px; right: -5%; bottom: 5%; background: #7c3aed; animation: float 18s infinite ease-in-out reverse;}

@keyframes float {
    0% { transform: translateY(0px) scale(1); }
    50% { transform: translateY(-30px) scale(1.05); }
    100% { transform: translateY(0px) scale(1); }
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
    padding: 10px;
}
.card {
    position: relative;
    overflow: hidden;
    padding: 30px;
    border-radius: 24px;
    background: rgba(15, 23, 42, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    min-height: 250px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.card:hover {
    transform: translateY(-10px);
    border: 1px solid rgba(0, 242, 254, 0.3);
    box-shadow: 0 20px 40px rgba(0, 242, 254, 0.08);
    background: rgba(15, 23, 42, 0.65);
}

.card-icon {
    width: 65px;
    height: 65px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(0, 242, 254, 0.1) 0%, rgba(79, 172, 254, 0.1) 100%);
    border: 1px solid rgba(0, 242, 254, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin-bottom: 20px;
    transition: transform 0.3s ease;
}
.card:hover .card-icon {
    transform: rotate(5deg) scale(1.05);
}
.card-title {
    font-size: 24px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 10px;
}
.card-desc {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 25px;
    flex-grow: 1;
}
.card-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #00f2fe;
    font-weight: 600;
    transition: gap 0.2s ease;
}
.card:hover .card-btn {
    gap: 14px;
}

a { text-decoration: none !important; }
</style>
""", unsafe_allow_html=True)

# ================= BACKGROUND ANIMATION EXTRA =================
st.markdown("""
<div class="bg-animation">
    <div class="blur-sphere sphere-1"></div>
    <div class="blur-sphere sphere-2"></div>
</div>
""", unsafe_allow_html=True)

# ================= PORTAL HEADER =================
st.markdown('<div class="main-title">EXECUTIVE CONTROL PORTAL</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Secure, fast, and unified access to all verified verification modules.</div>', unsafe_allow_html=True)

# ================= MODERN CARDS GRID =================
st.markdown(f"""
<div class="grid">
    <a href="{link1}" target="_blank">
        <div class="card">
            <div>
                <div class="card-icon">📊</div>
                <div class="card-title">PMY Verify</div>
                <div class="card-desc">Advanced PMY verification system with secure real-time data tracking and validation.</div>
            </div>
            <div class="card-btn">Launch System ➔</div>
        </div>
    </a>

    <a href="{link2}" target="_blank">
        <div class="card">
            <div>
                <div class="card-icon">🏦</div>
                <div class="card-title">BOP Account</div>
                <div class="card-desc">Comprehensive banking dashboard for managing accounts, payments, and smart processing.</div>
            </div>
            <div class="card-btn">Launch System ➔</div>
        </div>
    </a>

    <a href="{link3}" target="_blank">
        <div class="card">
            <div>
                <div class="card-icon">📁</div>
                <div class="card-title">ACAG Batch</div>
                <div class="card-desc">Track, evaluate, and monitor secure database batches with advanced administrative tools.</div>
            </div>
            <div class="card-btn">Launch System ➔</div>
        </div>
    </a>

    <a href="{link4}" target="_blank">
        <div class="card">
            <div>
                <div class="card-icon">📲</div>
                <div class="card-title">PMY Apply</div>
                <div class="card-desc">Seamless portal for filing applications, checking status updates, and tracking queues.</div>
            </div>
            <div class="card-btn">Launch System ➔</div>
        </div>
    </a>

    <a href="{link5}" target="_blank">
        <div class="card">
            <div>
                <div class="card-icon">📝</div>
                <div class="card-title">ACAG Apply</div>
                <div class="card-desc">Smart registration and intake system for streamlined institutional workflows.</div>
            </div>
            <div class="card-btn">Launch System ➔</div>
        </div>
    </a>

    <a href="{link6}" target="_blank">
        <div class="card">
            <div>
                <div class="card-icon">🚀</div>
                <div class="card-title">QR Generator</div>
                <div class="card-desc">High-speed utility to generate customized matrix barcodes with embedded actions.</div>
            </div>
            <div class="card-btn">Launch System ➔</div>
        </div>
    </a>

    <a href="{link7}" target="_blank">
        <div class="card">
            <div>
                <div class="card-icon">🔗</div>
                <div class="card-title">Address Finder</div>
                <div class="card-desc">Input a city name instantly to filter records and download complete data directories in PDF format.</div>
            </div>
            <div class="card-btn">Launch System ➔</div>
        </div>
    </a>
</div>
""", unsafe_allow_html=True)
