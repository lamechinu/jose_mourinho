import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Open When... 💌",
    page_icon="💌",
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
    
    /* Letter Box Styling */
    .letter-box {
        background-color: rgba(255, 255, 255, 0.9);
        color: #333;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-top: 20px;
        border-top: 10px solid #ff00de;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .signature {
        margin-top: 20px;
        font-weight: bold;
        text-align: right;
        font-family: 'Brush Script MT', cursive;
        font-size: 1.5rem;
        color: #ff416c;
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


# --- 💌 LETTERS CONTENT ---

st.title("💌 Open When...")
st.write("Pick a card based on how you are feeling right now. I might not be there physically, but my words are.")

# Dropdown to select mood
option = st.selectbox(
    "How is your heart feeling today?",
    ("Select an option...", "I'm feeling Sad / Low 😔", "I'm Missing You 🥺", "I'm Angry at You 😡", "I need a Laugh / Motivation 😂")
)

# --- LETTER 1: SAD/LOW ---
if option == "I'm feeling Sad / Low 😔":
    st.markdown("""
    <div class="letter-box">
        <h3>Hey Strong Girl,</h3>
        <p>
            I know things might feel heavy right now. Maybe it's exam stress, maybe someone said something, or maybe it's just one of "those" days.
            <br><br>
            But listen to me: <b>You are a fighter.</b>
            <br>
            Remember that time you handled when you were alone you didnt had me? You got through that, and you'll get through this.
            <br><br>
            Take a deep breath. Drink some water. Put on our playlist.
            <br>
            I believe in you, even when you don't believe in yourself.
        </p>
        <div class="signature">~ Your #1 Fan</div>
    </div>
    """, unsafe_allow_html=True)

# --- LETTER 2: MISSING YOU ---
elif option == "I'm Missing You 🥺":
    st.markdown("""
    <div class="letter-box">
        <h3>Aww, I miss you too!</h3>
        <p>
            Trust me, agar main waha aa sakta toh abhi aa jata. 
            <br><br>
            Distance sucks, but it also means our bond is stronger than just physical presence. 
            Close your eyes and remember our best hug. Feel that? That's me sending you energy.
            <br><br>
            Call me whenever you can. Main yahi hoon. Hamesha.
        </p>
        <div class="signature">~ Sahil (Yours)</div>
    </div>
    """, unsafe_allow_html=True)

# --- LETTER 3: ANGRY AT ME ---
elif option == "I'm Angry at You 😡":
    st.markdown("""
    <div class="letter-box">
        <h3>Okay, I'm Sorry! 🏳️</h3>
        <p>
            Pata hai maine kuch stupidity ki hogi. Engineering student hoon, dimag kabhi kabhi 'Error 404' ho jata hai. 🤦‍♂️
            <br><br>
            Gussa thuk do please? AAAAAAAAAA THUUUUUUUUUUU. You look prettier when you smile (cliché hai par sach hai).
            <br>
            Agli baar jab milenge, treat meri taraf se. Ice cream? Samosa? Deal?
        </p>
        <div class="signature">~ Your Idiot</div>
    </div>
    """, unsafe_allow_html=True)

# --- LETTER 4: NEED A LAUGH ---
elif option == "I need a Laugh / Motivation 😂":
    st.markdown("""
    <div class="letter-box">
        <h3>Daily Dose of Cringe ⚡</h3>
        <p>
            <b>Why do programmers prefer dark mode?</b><br>
            Because light attracts bugs. 🐛<br>
            (Okay, that was bad. Sorry.)
            <br><br>
            On a serious note: You are doing great. Life is tough but so are you. 
            Don't let the world dull your sparkle. 
            <br>
            Now go conquer the world (or at least your syllabus)!
        </p>
        <div class="signature">~ Tech Support for Life</div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()