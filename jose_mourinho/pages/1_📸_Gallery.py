import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Gallery 📸",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 🎨 CSS STYLING (Pink Theme + Neon Nav + Polaroid Effect) ---
st.markdown("""
    <style>
    /* 1. Hide default Sidebar */
    [data-testid="stSidebar"] { display: none; }
    
    /* 2. Main Background */
    .stApp {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* 3. Top Navigation Bar Styling */
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

    /* 4. PHOTO FRAME STYLING */
    img {
        border: 5px solid white;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }
    img:hover {
        transform: scale(1.02) rotate(1deg);
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }
    
    /* 5. Text Styling */
    .caption-box {
        background-color: rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #fff;
    }
    .song-lyric {
        font-style: italic;
        color: #ffe6e6;
        font-size: 1.1rem;
        margin-top: 10px;
    }
    .song-ref {
        font-size: 0.9rem;
        color: #ffccdd;
        font-weight: bold;
        text-align: right;
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


# --- 📸 GALLERY CONTENT ---

st.title("📸 Our Memory Lane")
st.write("Every picture tells a story. Here are some of my favorites.")
st.write("") 

# --- PHOTO 1 (Left Image) ---
c1, c2 = st.columns([1, 1.2], gap="large")
with c1:
    st.image("images/pic4.jpeg", use_container_width=True)
with c2:
    st.markdown("""
    <div class="caption-box">
        <h3>✨ The Beginning</h3>
        <p>Whether we are traveling or just sitting idle, time flies with you. Can't wait for more adventures.</p>
        <div class="song-lyric">
        "We keep this love in a photograph, we made these memories for ourselves..."
        </div>
        <div class="song-ref">~ Photograph, Ed Sheeran</div>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- PHOTO 2 (Right Image) ---
c1, c2 = st.columns([1.2, 1], gap="large")
with c1:
    st.markdown("""
    <div class="caption-box">
        <h3>🤪 The Chaos</h3>
        <p>This one perfectly captures our vibe. No filters, just pure chaos and laughter. Never change, okay?</p>
        <div class="song-lyric">
        "I don't know about you, but I'm feeling 22... (oops, 19!)"
        </div>
        <div class="song-ref">~ 22, Taylor Swift</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.image("images/pic2.jpeg", use_container_width=True)

st.write("---")

# --- PHOTO 3 (Left Image) ---
c1, c2 = st.columns([1, 1.2], gap="large")
with c1:
    st.image("images/pic3.jpeg", use_container_width=True)
with c2:
    st.markdown("""
    <div class="caption-box">
        <h3>💎 Pure Gold</h3>
        <p>In a world full of noise, you are my peace. Thank you for always listening to my nonsense.</p>
        <div class="song-lyric">
        "Look at the stars, look how they shine for you and everything you do..."
        </div>
        <div class="song-ref">~ Yellow, Coldplay</div>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- PHOTO 4 (Right Image) ---
c1, c2 = st.columns([1.2, 1], gap="large")
with c1:
    st.markdown("""
    <div class="caption-box">
        <h3>🌍 My Favorite View</h3>
        <p>Remember this? Just a random moment that turned into a core memory. Looking at this makes me realize how lucky I am to have you.</p>
        <div class="song-lyric">
        "Cause girl you're amazing, just the way you are."
        </div>
        <div class="song-ref">~ Just the Way You Are, Bruno Mars</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.image("images/pic5.jpeg", use_container_width=True)

st.write("---")

# --- PHOTO 5 (Left Image) ---
c1, c2 = st.columns([1, 1.2], gap="large")
with c1:
    st.image("images/pic1.jpeg", use_container_width=True)
with c2:
    st.markdown("""
    <div class="caption-box">
        <h3>👸 The Birthday Queen</h3>
        <p>Look at you! 19 and glowing. Keep shining bright. The world is yours for the taking.</p>
        <div class="song-lyric">
        "Baby you're a firework, come on show 'em what your worth!"
        </div>
        <div class="song-ref">~ Firework, Katy Perry</div>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- PHOTO 6 (Right Image - CATS) ---
c1, c2 = st.columns([1.2, 1], gap="large")
with c1:
    st.markdown("""
    <div class="caption-box">
        <h3>🦇 Basically Us</h3>
        <p>If we were cats, this would be it. I'm the Batman (trying to be cool), and you're the cutie with the bow (stealing the show).</p>
        <div class="song-lyric">
        "You are the best thing that's ever been mine."
        </div>
        <div class="song-ref">~ Mine, Taylor Swift</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    # Make sure file name is pic6.jpeg (ya jpg)
    st.image("images/pic6.jpeg", use_container_width=True)

st.write("---")
st.markdown("<center>💖 <b>More memories to be created...</b></center>", unsafe_allow_html=True)