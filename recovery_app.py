import streamlit as st
import streamlit as st

# Page Configuration (Fancy layout ke liye)
st.set_page_config(
    page_title="Modern Dashboard",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Fancy Styling
st.markdown("""
    <style>
    /* Main background color */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    /* Login card container */
    .login-box {
        background-color: #1e293b;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        max-width: 450px;
        margin: 50px auto;
        border: 1px solid #334155;
    }
    /* Custom Metric Cards */
    .metric-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State Initialize (Login track karne ke liye)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN SCREEN ---
if not st.session_state.logged_in:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #3b82f6;'>🚀 Welcome Back</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Login to access your premium dashboard</p>", unsafe_allow_html=True)
    
    # Input Fields
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Login Button
    if st.button("Sign In", use_container_width=True):
        if username == "admin" and password == "admin123":  # Yahan apna username/password set karein
            st.session_state.logged_in = True
            st.success("Success! Redirecting...")
            st.rerun()  # Screen refresh karke dashboard par le jayega
        else:
            st.error("Invalid Username or Password")
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- FANCY DASHBOARD SCREEN ---
else:
    # Sidebar for Navigation & Logout
    with st.sidebar:
        st.markdown("<h2 style='color: #3b82f6;'>⚙️ Control Panel</h2>", unsafe_allow_html=True)
        st.write(f"Logged in as: **Admin**")
        
        # Navigation Options
        menu = st.radio("Navigation", ["📈 Overview", "📊 Analytics", "👤 Profile Settings"])
        
        st.markdown("---")
        if st.button("🚪 Log Out", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # Main Content Area based on Menu selection
    if menu == "📈 Overview":
        st.title("🌟 Executive Dashboard")
        st.subheader("Welcome to your main control center.")
        
        # Fancy Metric Cards Layout
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div class="metric-card">
                    <p style="color: #94a3b8; margin:0;">Total Users</p>
                    <h2 style="margin:0; color: #3b82f6;">1,420</h2>
                    <span style="color: #10b981; font-size: 14px;">▲ +12% this week</span>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
                <div class="metric-card" style="border-left-color: #10b981;">
                    <p style="color: #94a3b8; margin:0;">Revenue Generated</p>
                    <h2 style="margin:0; color: #10b981;">$12,450</h2>
                    <span style="color: #10b981; font-size: 14px;">▲ +8% this month</span>
                </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
                <div class="metric-card" style="border-left-color: #f59e0b;">
                    <p style="color: #94a3b8; margin:0;">Active Sessions</p>
                    <h2 style="margin:0; color: #f59e0b;">342</h2>
                    <span style="color: #ef4444; font-size: 14px;">▼ -3% compared to yesterday</span>
                </div>
            """, unsafe_allow_html=True)

        # Dashboard Sample Charts
        st.markdown("### Recent Activities & Performance")
        chart_data = [10, 20, 15, 40, 35, 50, 60]
        st.line_chart(chart_data)

    elif menu == "📊 Analytics":
        st.title("📊 Detailed Analytics")
        st.write("Yahan aap apna mazeed data, dataframes, ya charts display kar sakte hain.")
        st.bar_chart([12, 45, 67, 23, 89])

    elif menu == "👤 Profile Settings":
        st.title("👤 Account Settings")
        st.info("Manage your password, API keys, and notification preferences here.")
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
