import streamlit as st
import time
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Happy 19th! 🎂",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 🎨 CSS STYLING (Pink Theme + Neon Nav) ---
st.markdown("""
    <style>
    /* 1. Hide default Sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* 2. Main Background: Romantic Pink Gradient */
    .stApp {
        background: linear-gradient(120deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        /* Alternative Darker Pink if text is hard to read: */
        /* background: linear-gradient(to right, #b92b27, #1565c0); */ 
        /* Let's stick to a vibrant Pink-Red mix */
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* 3. Top Navigation Bar Styling */
    div[data-testid="stHorizontalBlock"] {
        background-color: rgba(255, 255, 255, 0.15); /* Glass effect */
        padding: 10px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        margin-bottom: 30px;
    }

    /* Nav Buttons */
    button[kind="secondary"] {
        background: transparent !important;
        border: none !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease-in-out;
    }

    /* Hover Effect */
    button[kind="secondary"]:hover {
        color: #ffe6e6 !important;
        text-shadow: 0 0 10px #ffffff, 0 0 20px #ff00de;
        transform: translateY(-2px);
    }

    /* 4. Text Styling */
    h1 {
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    p {
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🧭 TOP NAVIGATION BAR ---
with st.container():
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns(9)
    with c1: st.page_link("Home.py", label="Home", icon="🏠")
    with c2: st.page_link("pages/1_📸_Gallery.py", label="Gallery", icon="📸")
    with c3: st.page_link("pages/2_🎶_Music.py", label="Music", icon="🎵")
    with c4: st.page_link("pages/3_💌_Letters.py", label="Letters", icon="💌")
    with c5: st.page_link("pages/4_✨_Daily_Dose.py", label="Daily", icon="✨")
    with c6: st.page_link("pages/5_🎂_Celebration.py", label="Party", icon="🎂")
    with c7: st.page_link("pages/6_⏳_Timeline.py", label="Time", icon="⏳")
    with c8: st.page_link("pages/7_💖_Grateful.py", label="WhyYou", icon="💖")
    with c9: st.page_link("pages/8_🎮_Games.py", label="Game", icon="🎮")

st.divider()


# --- 🎂 MAIN BIRTHDAY CONTENT ---

st.title("HAPPY 19th BIRTHDAY! 👸")

st.markdown(
    """
    <div style='text-align: center; font-size: 1.6rem; margin-bottom: 20px; font-weight: bold;'>
    To the girl who owns my heart... <br>
    Welcome to Chapter 19.
    </div>
    """, 
    unsafe_allow_html=True
)

# Layout: Text on Left, Photo on Right
c1, c2 = st.columns([1.5, 1])

with c1:
    st.write("### ✨ Why this exists?")
    st.write("""
    The world got a little brighter 19 years ago because you arrived.
    And ever since you entered my life, everything has been in HD.
    
    Instead of a regular store-bought gift, I wanted to give you something that is truly **'Me'**.
    **Code.** Because sometimes words aren't enough, but effort speaks volumes.
    
    Every pixel and every line of code here is written just for you.
    Explore it, this is your personal **Digital Wonderland**.
    """)
    
    st.write("")
    st.write("")
    if st.button("🎈 Tap for a Birthday Wish 🎈"):
        st.balloons()
        st.toast("Happy Birthday Queen! 👑")
        time.sleep(1)
        st.toast("May your year be as beautiful as you are! ✨")

with c2:
    # IMAGE LOGIC
    # Make sure 'pic5.jpeg' is inside 'images' folder
    try:
        st.image("images/pic5.jpeg", caption="The Birthday Girl 💖", use_container_width=True)
    except:
        st.error("Image not found! Check if file is named 'pic5.jpeg' inside 'images' folder.")

st.write("---")
st.markdown("<center>👆 <b>Use the Navigation Bar above to open your gifts!</b></center>", unsafe_allow_html=True)
