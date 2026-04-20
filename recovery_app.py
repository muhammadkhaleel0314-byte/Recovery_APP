import streamlit as st

st.set_page_config(page_title="My Links", layout="wide")

st.title("🚀 My Quick Links")

# ----------- CSS DESIGN -----------
st.markdown("""
<style>
.box {
    padding: 40px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

.box:hover {
    transform: scale(1.05);
}

/* Box Colors */
.box1 { 
    background: linear-gradient(135deg, #ff7e5f, #feb47b);
    color: black;   /* 👈 Black text */
}
.box2 { 
    background: linear-gradient(135deg, #36d1dc, #5b86e5);
    color: white;
}
.box3 { 
    background: linear-gradient(135deg, #11998e, #38ef7d);
    color: white;
}

/* 🔥 IMPORTANT FIX (remove blue link color) */
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

# ----------- BOXES -----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'''
        <a href="{link1}" target="_blank">
            <div class="box box1">PMY Link</div>
        </a>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
        <a href="{link2}" target="_blank">
            <div class="box box2">Account Link</div>
        </a>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
        <a href="{link3}" target="_blank">
            <div class="box box3">Coming Soon</div>
        </a>
    ''', unsafe_allow_html=True)
