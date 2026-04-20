import streamlit as st

st.set_page_config(page_title="My Links", layout="wide")

st.title("🚀 My Quick Links")

# ----------- CSS ANIMATION -----------
st.markdown("""
<style>

/* Page fade */
body {
    animation: fadeIn 0.8s ease-in-out;
}

@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}

/* Base box */
.box {
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 5px 12px rgba(0,0,0,0.12);
}

/* Hover */
.box:hover {
    transform: translateY(-6px) scale(1.05);
}

/* ========= ANIMATIONS ========= */
@keyframes fromRight {
    from {opacity:0; transform: translateX(120px);}
    to {opacity:1; transform: translateX(0);}
}

@keyframes fromLeft {
    from {opacity:0; transform: translateX(-120px);}
    to {opacity:1; transform: translateX(0);}
}

@keyframes fromTop {
    from {opacity:0; transform: translateY(-120px);}
    to {opacity:1; transform: translateY(0);}
}

@keyframes fromBottom {
    from {opacity:0; transform: translateY(120px);}
    to {opacity:1; transform: translateY(0);}
}

@keyframes fadeOnly {
    from {opacity:0;}
    to {opacity:1;}
}

/* ========= APPLY ANIMATION ========= */
.box1 { animation: fromRight 1.2s ease-in-out forwards; opacity:0; }
.box2 { animation: fromLeft 1.2s ease-in-out forwards; opacity:0; }
.box3 { animation: fromTop 1.2s ease-in-out forwards; opacity:0; }
.box4 { animation: fromBottom 1.2s ease-in-out forwards; opacity:0; }
.box5 { animation: fadeOnly 1.5s ease-in-out forwards; opacity:0; }

/* ========= COLORS ========= */
.box1 { background:#ffffff; color:black; border:1px solid #ddd; }
.box2 { background:#FFD700; color:black; }
.box3 { background:#808080; color:white; }
.box4 { background:linear-gradient(135deg,#11998e,#38ef7d); color:white; }
.box5 { background:linear-gradient(135deg,#36d1dc,#5b86e5); color:white; }

/* remove link blue */
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
