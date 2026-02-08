import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Our Vibe 🎶",
    page_icon="🎧",
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

    /* Vinyl Animation */
    .vinyl-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
        padding-top: 20px;
    }
    .vinyl {
        width: 180px;
        height: 180px;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/b/b6/12in-Vinyl-LP-Record-Angle.jpg');
        background-size: cover;
        border-radius: 50%;
        animation: spin 5s linear infinite;
        box-shadow: 0 0 25px rgba(0,0,0,0.6);
        border: 4px solid rgba(255,255,255,0.1);
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Lyrics Card */
    .lyrics-card {
        background: rgba(0,0,0,0.2);
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #fff;
        font-style: italic;
        margin-top: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .lyrics-text {
        font-size: 1.2rem;
        color: #fce4ec;
        font-weight: 500;
    }
    .song-credit {
        margin-top: 10px;
        font-size: 0.9rem;
        color: #ff80ab;
        font-weight: bold;
        text-align: right;
    }
    
    /* Custom Button Style for Link */
    .stLinkButton > a {
        background-color: #1DB954 !important; /* Spotify Green */
        color: white !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        text-align: center !important;
        border: 2px solid white !important;
        padding: 10px 20px !important;
        display: block !important;
        margin: 0 auto !important;
        text-decoration: none !important;
    }
    .stLinkButton > a:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
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


# --- 🎶 MAIN CONTENT ---

c1, c2 = st.columns([1.3, 1], gap="large")

with c1:
    st.title("🎶 The Soundtrack of Us")
    st.write("""
    Music is the closest thing to magic. Whenever I can't find the words, I find a song.
    
    Ye playlist thodi *weird* hai, bilkul humari tarah. 
    Ek taraf **Lata ji & Kishore Kumar** ki pure classic melody hai, 
    aur dusri taraf **Seedhe Maut & Karma** ka raw emotion.
    
    From "O Rangrez" to "Nadaan"... har gaana ek memory hai.
    """)
    
    st.markdown("### 🎧 Top Picks for You:")
    st.markdown("- **Romantic:** *Nazm Nazm, Mon Bojhena, O Rangrez*")
    st.markdown("- **Classics:** *Lag Jaa Gale, Pal Pal Dil Ke Paas*")
    st.markdown("- **Vibe:** *Maina, Nadaan, Lena Mera Naam*")
    st.markdown("- **International:** *Perfect, Can't Help Falling in Love*")

    # Lyrics Card
    st.markdown("""
    <div class="lyrics-card">
        <div class="lyrics-text">
        "Haath thaam le piya, karte hain vaada...<br>
        Ab se tu aarzoo, tu hi hai iraada."
        </div>
        <div class="song-credit">~ Nazm Nazm (Bareilly Ki Barfi)</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    # Vinyl Animation
    st.markdown('<div class="vinyl-container"><div class="vinyl"></div></div>', unsafe_allow_html=True)
    st.markdown("<center><b>Now Playing (Forever Love Mix)...</b></center>", unsafe_allow_html=True)
    
    # 1. YOUTUBE PLAYER (Safe, no errors, vibe setter)
    # Includes Nazm Nazm & Arijit Hits
    st.markdown("""
        <iframe width="100%" height="300" 
        src="https://www.youtube.com/embed/3hM8GRjErUQ?autoplay=0&rel=0" 
        title="Forever Love Mix" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen style="border-radius: 15px;"></iframe>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # 2. THE SPECIAL SPOTIFY BUTTON (Opens your specific link)
    st.markdown("<center>👇 <b>Want to listen to YOUR specific playlist?</b></center>", unsafe_allow_html=True)
    
    # Ye link seedha teri playlist kholega app mein
    st.link_button("💚 Open 'Special Playlist' in App", "https://open.spotify.com/playlist/2yXhaiAFmCa01XQ5yN9KTg?si=h8tMwQpLS-SZij0j6uQP9w&pi=cDx5gRNET26Tn")

st.write("---")
st.markdown("<center>🎶 <b>Put on your headphones, close your eyes, and feel the magic.</b></center>", unsafe_allow_html=True)