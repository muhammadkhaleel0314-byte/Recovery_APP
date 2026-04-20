import streamlit as st

st.set_page_config(page_title="My Links", layout="wide")

st.title("🚀 My Quick Links")

# ----------- CSS + ANIMATIONS -----------
st.markdown("""
<style>

/* 🔥 Animations */
@keyframes slideLeft {
    from {opacity:0; transform:translateX(-100px);}
    to {opacity:1; transform:translateX(0);}
}

@keyframes slideRight {
    from {opacity:0; transform:translateX(100px);}
    to {opacity:1; transform:translateX(0);}
}

@keyframes slideUp {
    from {opacity:0; transform:translateY(100px);}
    to {opacity:1; transform:translateY(0);}
}

@keyframes slideDown {
    from {opacity:0; transform:translateY(-100px);}
    to {opacity:1; transform:translateY(0);}
}

/* 💃 Dance animation */
@keyframes dance {
    0%   {opacity:0; transform:scale(0.5) rotate(-10deg);}
    50%  {transform:scale(1.1) rotate(10deg);}
    75%  {transform:scale(0.95) rotate(-5deg);}
    100% {opacity:1; transform:scale(1) rotate(0);}
}

.box {
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* 🎯 Apply animations */
.box1 { animation: slideLeft 0.6s ease forwards; }
.box2 { animation: slideRight 0.6s ease forwards; }
.box3 { animation: slideUp 0.6s ease forwards; }
.box4 { animation: slideDown 0.6s ease forwards; }
.box5 { animation: dance 0.8s ease forwards; }

/* Hover */
.box:hover {
    transform: scale(1.08);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}

/* Colors */
.box1 { background:#ffffff; color:black; border:2px solid #ddd;}
.box2 { background:#FFD700; color:black;}
.box3 { background:#808080; color:white;}
.box4 { background:linear-gradient(135deg,#11998e,#38ef7d); color:white;}
.box5 { background:linear-gradient(135deg,#36d1dc,#5b86e5); color:white;}

/* Remove link blue */
a, a:visited {
    color: inherit !important;
    text-decoration: none !important;
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
    st.markdown(f'<a href="{link1}" target="_blank"><div class="box box1">PMY All Verify Data</div></a>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<a href="{link2}" target="_blank"><div class="box box2">Account Link</div></a>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<a href="{link3}" target="_blank"><div class="box box3">ACAG All Batch Data</div></a>', unsafe_allow_html=True)

with col4:
    st.markdown(f'<a href="{link4}" target="_blank"><div class="box box4">PMY Apply & Track</div></a>', unsafe_allow_html=True)

with col5:
    st.markdown(f'<a href="{link5}" target="_blank"><div class="box box5">ACAG Apply</div></a>', unsafe_allow_html=True)
