import streamlit as st

st.set_page_config(page_title="My Links", layout="wide")

st.title("🚀 My Quick Links")

# ----------- CSS DESIGN + ANIMATION -----------
st.markdown("""
<style>

/* 🔥 Slide Animation */
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
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

    /* Animation */
    animation: slideUp 0.6s ease forwards;
}

/* ⏱️ Delay for each box (one by one effect) */
.box1 { animation-delay: 0.1s; }
.box2 { animation-delay: 0.3s; }
.box3 { animation-delay: 0.5s; }
.box4 { animation-delay: 0.7s; }
.box5 { animation-delay: 0.9s; }

/* Hover Effect */
.box:hover {
    transform: scale(1.08);
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}

/* Click Effect */
.box:active {
    transform: scale(0.95);
}

/* 🎨 Colors */
.box1 { 
    background: #ffffff;
    color: black;
    border: 2px solid #ddd;
}

.box2 { 
    background: #FFD700;
    color: black;
}

.box3 { 
    background: #808080;
    color: white;
}

.box4 { 
    background: linear-gradient(135deg, #11998e, #38ef7d);
    color: white;
}

.box5 { 
    background: linear-gradient(135deg, #36d1dc, #5b86e5);
    color: white;
}

/* Remove blue link */
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
