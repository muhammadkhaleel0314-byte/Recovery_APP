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

/* Basic box */
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

/* Hover effect */
.box:hover {
    transform: translateY(-6px) scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,0.25);
}

/* 🔥 SEQUENTIAL ANIMATION (IMPORTANT PART) */
@keyframes pop {
    from {opacity:0; transform: translateY(30px);}
    to {opacity:1; transform: translateY(0);}
}

/* 👇 ONE BY ONE DELAY */
.box1 { animation: pop 0.8s ease 0.2s forwards; opacity:0; }
.box2 { animation: pop 0.8s ease 1.0s forwards; opacity:0; }
.box3 { animation: pop 0.8s ease 1.8s forwards; opacity:0; }
.box4 { animation: pop 0.8s ease 2.6s forwards; opacity:0; }
.box5 { animation: pop 0.8s ease 3.4s forwards; opacity:0; }

/* Colors */
.box1 { background:#ffffff; color:black; border:1px solid #ddd; }
.box2 { background:#FFD700; color:black; }
.box3 { background:#808080; color:white; }
.box4 { background:linear-gradient(135deg,#11998e,#38ef7d); color:white; }
.box5 { background:linear-gradient(135deg,#36d1dc,#5b86e5); color:white; }

/* Remove link blue */
a, a:visited {
    text-decoration:none !important;
    color:inherit !important;
}

</style>
""", unsafe_allow_html=True)
