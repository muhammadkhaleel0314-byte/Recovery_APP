import streamlit as st

st.set_page_config(page_title="My Links", layout="wide")

st.title("🚀 My Quick Links")

# ----------- PREMIUM CSS -----------
st.markdown("""
<style>

/* Page fade-in */
body {
    animation: fadeIn 1.2s ease-in-out;
}

@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}

/* Card style (modern glass feel) */
.box {
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.4s ease;
    box-shadow: 0 6px 15px rgba(0,0,0,0.12);
}

/* smooth hover */
.box:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 12px 25px rgba(0,0,0,0.25);
}

/* 🎯 Stagger animation (REAL SMOOTH FEEL) */
@keyframes pop {
    from {opacity:0; transform: scale(0.8);}
    to {opacity:1; transform: scale(1);}
}

.box1 { animation: pop 0.6s ease 0.2s forwards; opacity:0; }
.box2 { animation: pop 0.6s ease 0.4s forwards; opacity:0; }
.box3 { animation: pop 0.6s ease 0.6s forwards; opacity:0; }
.box4 { animation: pop 0.6s ease 0.8s forwards; opacity:0; }
.box5 { animation: pop 0.6s ease 1.0s forwards; opacity:0; }

/* Colors */
.box1 { background:#ffffff; color:black; border:1px solid #ddd; }
.box2 { background:#FFD700; color:black; }
.box3 { background:#808080; color:white; }
.box4 { background:linear-gradient(135deg,#11998e,#38ef7d); color:white; }
.box5 { background:linear-gradient(135deg,#36d1dc,#5b86e5); color:white; }

/* Remove blue link */
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

# ----------- BOXES -----------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f'<a href="{link1}" target="_blank"><div class="box box1">PMY Verify Data</div></a>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<a href="{link2}" target="_blank"><div class="box box2">Account Link</div></a>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<a href="{link3}" target="_blank"><div class="box box3">ACAG Batch Data</div></a>', unsafe_allow_html=True)

with col4:
    st.markdown(f'<a href="{link4}" target="_blank"><div class="box box4">PMY Track</div></a>', unsafe_allow_html=True)

with col5:
    st.markdown(f'<a href="{link5}" target="_blank"><div class="box box5">ACAG Apply</div></a>', unsafe_allow_html=True)
