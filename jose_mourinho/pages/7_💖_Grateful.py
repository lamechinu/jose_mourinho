import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Grateful 💖",
    page_icon="🙏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 🎨 CSS STYLING (Floating Hearts + Glassmorphism) ---
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

    /* Content Box Styling */
    .grateful-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    h3 {
        color: #FFD700; /* Gold Color for Headings */
        margin-bottom: 15px;
    }
    p {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #fff;
    }

    /* FLOATING HEARTS ANIMATION */
    .heart {
        position: fixed;
        color: rgba(255, 255, 255, 0.3);
        font-size: 20px;
        animation: float 6s linear infinite;
        bottom: -100px;
        z-index: 0;
    }
    
    @keyframes float {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🫧 FLOATING HEARTS LOGIC ---
# Ye background mein hearts create karega
st.markdown("""
<div class="heart" style="left: 10%; animation-duration: 7s;">❤</div>
<div class="heart" style="left: 20%; animation-duration: 9s; font-size: 30px;">💖</div>
<div class="heart" style="left: 50%; animation-duration: 5s;">❤</div>
<div class="heart" style="left: 70%; animation-duration: 11s; font-size: 40px;">💖</div>
<div class="heart" style="left: 85%; animation-duration: 6s;">❤</div>
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


# --- 💖 MAIN CONTENT ---

st.title("💖 Why You Are So Special...")
st.write("There are a million reasons, but here are the ones close to my heart.")

# Section 1: The Care (Food)
st.markdown("""
<div class="grateful-box">
    <h3>🍲 The Way You Care</h3>
    <p>
        You know, people say "actions speak louder than words," and you prove it every single day. 
        Especially when you make food for me and bring it with so much love. 
        It's not just about the food (though it's amazing), it's about the effort. 
        It shows how much you truly care about my well-being. 
        That simple act of feeding me makes me feel like the luckiest guy alive.
    </p>
</div>
""", unsafe_allow_html=True)

# Section 2: The Temple & Future (Deep Paragraph)
st.markdown("""
<div class="grateful-box">
    <h3>⛩️ My Silent Prayers</h3>
    <p>
        I don't think I've ever told you this properly, but you are not just a part of my life anymore; you <i>are</i> my life. 
        Every time I visit a temple, I don't just ask for my own success or happiness. 
        <b>I ask for "Us".</b>
        <br><br>
        I pray for your happiness, for your protection, and for a future where we are together, facing everything side by side. 
        God knows how much I love you, and I promise you this today: 
        I will do everything humanly possible to keep that beautiful smile on your face. 
        Your happiness is my priority, today and forever.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# Final Touch
c1, c2, c3 = st.columns([1,2,1])
with c2:
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", caption="You & Me. Always.", use_container_width=True)

st.write("---")
st.markdown("<center>💖 <b>Thank you for being mine.</b></center>", unsafe_allow_html=True)