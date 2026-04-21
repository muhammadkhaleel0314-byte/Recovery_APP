import streamlit as st

st.set_page_config(page_title="My Links", layout="wide")

st.title("🚀 My Smart Dashboard")

# ----------- ADVANCED CSS -----------
st.markdown("""
<style>

/* 🌌 Animated Background */
body {
    background: linear-gradient(-45deg, #1f4037, #99f2c8, #2980b9, #6dd5fa);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ Glass Card */
.box {
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.4s ease;
    
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);

    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

/* 💡 Glow Hover */
.box:hover {
    transform: translateY(-10px) scale(1.07);
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
}

/* 🎬 Animation */
@keyframes reveal {
    from {opacity:0; transform: translateY(40px);}
    to {opacity:1; transform: translateY(0);}
}

/* ⏳ Stagger Delay */
.box1 { animation: reveal 0.8s ease 0.2s forwards; opacity:0; }
.box2 { animation: reveal 0.8s ease 0.5s forwards; opacity:0; }
.box3 { animation: reveal 0.8s ease 0.8s forwards; opacity:0; }
.box4 { animation: reveal 0.8s ease 1.1s forwards; opacity:0; }
.box5 { animation: reveal 0.8s ease 1.4s forwards; opacity:0; }
.box6 { animation: reveal 0.8s ease 1.7s forwards; opacity:0; }

/* 🎨 Text Colors */
.box1 { color:#000; background:rgba(255,255,255,0.9); }
.box2 { color:#000; background:#FFD700; }
.box3 { color:#fff; background:#555; }
.box4 { color:#fff; background:linear-gradient(135deg,#11998e,#38ef7d); }
.box5 { color:#fff; background:linear-gradient(135deg,#36d1dc,#5b86e5); }
.box6 { color:#fff; background:linear-gradient(135deg,#ff512f,#dd2476); }

/* Remove link style */
a, a:visited {
    text-decoration:none !important;
    color:inherit !important;
}

</style>
""", unsafe_allow_html=True)

# ----------- LINKS -----------
link1 = "https://script.google.com/macros/s/AKfycbyCr-KxEdrWdLhHXYWMLcDdK1Viciar6yJtQsaQNPFuY-X9IK41GkOiRvkV64PbatE9Kg/exec"
link2 = "https://script.google.com/macros/s/AKfycbzPaNIURbCJLA8iNRm3RA6v2OS5WlxaMURw0IIjcwLnLvBPlVJ9DJG7KxihITJ6g6mb/exec"
link3 = "https://script.google.com/macros/s/AKfycbzTMdTGQczpfnWd76rdwhj1rr_4DCMTMITYFgJZBcGrDbBSQZIHKu3mTkaXYnB5Y9VZew/exec"
link4 = "https://pmybals.pmyp.gov.pk/"
link5 = "https://acag.punjab.gov.pk/"
link6 = "#"

# ----------- BOXES -----------
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown(f'<a href="{link1}" target="_blank"><div class="box box1">📊 PMY Verify Data</div></a>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<a href="{link2}" target="_blank"><div class="box box2">🏦 BOP Account Detail</div></a>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<a href="{link3}" target="_blank"><div class="box box3">📁 ACAG Batch Data</div></a>', unsafe_allow_html=True)

with col4:
    st.markdown(f'<a href="{link4}" target="_blank"><div class="box box4">📲 PMY Apply & Track</div></a>', unsafe_allow_html=True)

with col5:
    st.markdown(f'<a href="{link5}" target="_blank"><div class="box box5">📝 ACAG Apply</div></a>', unsafe_allow_html=True)

with col6:
    st.markdown(f'<a href="{link6}" target="_blank"><div class="box box6">🚧 RDC (Coming Soon)</div></a>', unsafe_allow_html=True)
