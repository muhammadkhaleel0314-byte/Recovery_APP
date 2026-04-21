import streamlit as st
import requests
import time

st.set_page_config(page_title="Smart Dashboard", layout="wide")

st.title("🚀 Smart Dashboard")

# ----------- AUTO REFRESH -----------
st.experimental_rerun = st.runtime.scriptrunner.script_run_context.get_script_run_ctx
time.sleep(30)

# ----------- NEWS FUNCTION -----------
def get_news():
    api_key = "YOUR_API_KEY_HERE"   # 👈 yahan apni API key daalo
    
    urls = [
        f"https://newsapi.org/v2/top-headlines?country=pk&apiKey={api_key}",
        f"https://newsapi.org/v2/top-headlines?category=general&apiKey={api_key}"
    ]
    
    headlines = []
    
    try:
        for url in urls:
            res = requests.get(url).json()
            for a in res.get("articles", [])[:5]:
                headlines.append(a["title"])
        
        if headlines:
            return " 🔴 ".join(headlines[:10])
        else:
            return "⚠️ No news available"
    
    except:
        return "⚠️ News load nahi ho saki"

news_text = get_news()

# ----------- CSS -----------
st.markdown("""
<style>

/* GRID */
.grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(200px,1fr));
    gap:15px;
}

/* BOX STYLE */
.card {
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-weight:bold;
    font-size:16px;
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    transition:0.3s;
    box-shadow:0 5px 15px rgba(0,0,0,0.2);
}

.card:hover {
    transform: scale(1.05);
}

/* TICKER */
.ticker {
    margin-top:30px;
    overflow:hidden;
    background:black;
    color:white;
    padding:12px;
    border-radius:10px;
}

.ticker-text {
    display:inline-block;
    padding-left:100%;
    animation: scroll 30s linear infinite;
    font-weight:bold;
}

/* ANIMATION */
@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

/* REMOVE LINK STYLE */
a {
    text-decoration:none;
    color:inherit;
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
st.markdown(f"""
<div class="grid">

<a href="{link1}" target="_blank"><div class="card">📊 PMY Verify Data</div></a>
<a href="{link2}" target="_blank"><div class="card">🏦 BOP Account</div></a>
<a href="{link3}" target="_blank"><div class="card">📁 ACAG Batch Data</div></a>
<a href="{link4}" target="_blank"><div class="card">📲 PMY Apply</div></a>
<a href="{link5}" target="_blank"><div class="card">📝 ACAG Apply</div></a>
<a href="{link6}" target="_blank"><div class="card">🚧 RDC (Coming Soon)</div></a>

</div>
""", unsafe_allow_html=True)

# ----------- LIVE NEWS TICKER -----------
st.markdown(f"""
<div class="ticker">
    <div class="ticker-text">
        🇵🇰 BREAKING NEWS 🇵🇰 | {news_text}
    </div>
</div>
""", unsafe_allow_html=True)
