import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Celebration! 🎂",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 🎨 CSS STYLING ---
st.markdown("""
    <style>
    /* Hide Sidebar */
    [data-testid="stSidebar"] { display: none; }
    
    /* Background */
    .stApp {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Navbar Styling */
    div[data-testid="stHorizontalBlock"] {
        background-color: rgba(255, 255, 255, 0.15);
        padding: 10px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        margin-bottom: 30px;
    }
    button[kind="secondary"] {
        background: transparent !important;
        border: none !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease-in-out;
    }
    button[kind="secondary"]:hover {
        color: #ffe6e6 !important;
        text-shadow: 0 0 10px #ffffff, 0 0 20px #ff00de;
        transform: translateY(-2px);
    }

    /* Cake Card Styling */
    .cake-container {
        text-align: center;
        padding: 50px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🧭 NAVBAR ---
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

# --- 🎂 CAKE CUTTING LOGIC ---

st.title("🎂 Let's Cut the Cake!")
st.write("Kya laga main waha nahi hoon toh cake nahi katega? Galat fehmi hai. 😉")

# Session State to track if candles are blown
if 'candles_blown' not in st.session_state:
    st.session_state.candles_blown = False

# Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if not st.session_state.candles_blown:
        # STATE 1: CANDLES LIT (Before Click)
        st.markdown("### Make a wish and blow the candles! 🕯️")
        
        # Lit Cake Image (Placeholder GIF)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm95Ym15dGg5Z3J3NmJ5Z3J3NmJ5Z3J3NmJ5Z3J3NmJ5Z3J3NmJ5/L0x6W9Xyj7Q4/giphy.gif", caption="Waiting for you...", use_container_width=True)
        
        st.write("")
        if st.button("🌬️ Blow Candles"):
            st.session_state.candles_blown = True
            st.rerun() # Refresh page to show next state
            
    else:
        # STATE 2: CELEBRATION (After Click)
        st.balloons() # Confetti/Balloons
        
        st.markdown("### 🎉 YAYYYY! HAPPY BIRTHDAY! 🥳")
        st.write("May all your wishes come true!")
        
        # Audio Play (Happy Birthday Instrumental)
        # Using a reliable raw link from GitHub or similar source
        st.audio("https://dn720303.ca.archive.org/0/items/happy-birthday-to-you-piano-version/Happy%20Birthday%20To%20You%20%28Piano%20Version%29.mp3", format="audio/mp3", autoplay=True)
        
        # Celebration Image
        st.image("https://media.giphy.com/media/l4KibWpBGWchSqCRy/giphy.gif", caption="Party Time! 💃", use_container_width=True)
        
        if st.button("🔄 Light Candles Again?"):
            st.session_state.candles_blown = False
            st.rerun()

st.write("---")