import streamlit as st

st.set_page_config(page_title="My Links", layout="wide")

st.title("🚀 My Quick Links")

# ----------- CSS DESIGN -----------
st.markdown("""
<style>
.box {
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

.box:hover {
    transform: scale(1.05);
}

/* 🎨 Updated Colors */
.box1 { 
    background: #ffffff;   /* white */
    color: black;
    border: 2px solid #ddd; /* thoda visible banane ke liye */
}

.box2 { 
    background: #FFD700;   /* yellow */
    color: black;
}

.box3 { 
    background: #808080;   /* gray */
    color: white;
}

/* Remove blue link color */
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
    st.markdown(f'<a href="{link4}" target="_blank"><div class="box box3">PMY Apply & Track</div></a>', unsafe_allow_html=True)

with col5:
    st.markdown(f'<a href="{link5}" target="_blank"><div class="box box3">ACAG Apply</div></a>', unsafe_allow_html=True)
