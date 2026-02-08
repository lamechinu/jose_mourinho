import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Daily Dose ✨",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 🎨 CSS STYLING ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none; }
    
    .stApp {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Navbar */
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

    /* Message Card */
    .daily-card {
        background-color: rgba(255, 255, 255, 0.95);
        color: #333;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-top: 20px;
        border: 2px solid #fff;
    }
    .quote-text {
        font-size: 1.6rem;
        font-weight: bold;
        color: #e73c7e;
        font-family: 'Georgia', serif;
        margin-bottom: 20px;
    }
    .sub-text {
        font-size: 1.1rem;
        color: #555;
        font-style: italic;
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


# --- ✨ DAILY MESSAGE LOGIC ---

st.title("✨ Daily Dose of Love")
st.write("Come back here every day for a new reminder of how awesome you are.")

# --- 📅 DATE CHECKING LOGIC ---
today_date = datetime.date.today() # Aaj ki date uthayega
month = today_date.month
day = today_date.day

# --- 🎂 SPECIAL BIRTHDAY TRIGGER (9 FEB) ---
if month == 2 and day == 9:
    # Agar 9 Feb hai, toh ye dikhega
    st.markdown(f"""
    <div class="daily-card" style="border: 5px solid #FFD700;">
        <div class="quote-text" style="color: #FFD700; font-size: 2.5rem;">
            🎉 HAPPY BIRTHDAY QUEEN! 👸
        </div>
        <div class="quote-text">
            "The world is lucky to have you, but I am the luckiest."
        </div>
        <div class="sub-text">
            ~ Special Message for Today ({today_date.strftime('%B %d')})
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()
    st.toast("It's your day! Go shine! ✨")

else:
    # --- NORMAL DAYS (Rotational Messages) ---
    messages = [
        # 1-10
        "You are capable of amazing things. (Self-belief is key!)",
        "Tu hai toh mujhe phir aur kya chahiye? (Arijit Singh)",
        "I am so proud of the person you are becoming.",
        "Don't forget to drink water and take care of yourself.",
        "And darling I will be loving you 'til we're 70. (Ed Sheeran)",
        "Even on your worst days, you are still my favorite person.",
        "Tera humor broken hai, par tu perfect hai.",
        "Keep shining. The world needs your light.",
        "Lag ja gale ki phir ye haseen raat ho na ho... (Lata Mangeshkar)",
        "Sending you a virtual hug right now! 🤗",
        
        # 11-20
        "You are the best thing that's ever been mine. (Taylor Swift)",
        "Aaj ka din tera hai. Go crush it!",
        "Sau andheron mein bhi roshan ho, us haqeeqat ki tarah. (Tu Mile)",
        "Reminder: You are loved more than you know.",
        "Smile. It looks good on you.",
        "Maina ude, main bhi udun... (Seedhe Maut vibe)",
        "Whatever you are worrying about right now, it will pass.",
        "Wise men say only fools rush in, but I can't help falling in love with you.",
        "Tu bas khud pe bharosa rakh, main humesha tere peeche khada hoon.",
        "Life is tough, but so are you.",
        
        # 21-30
        "Ab se tu aarzoo, tu hi hai iraada. (Nazm Nazm)",
        "Take a break. You work too hard.",
        "You make my world colorful just by being in it.",
        "Agar tum saath ho... (Arijit Singh)",
        "Don't let anyone dull your sparkle.",
        "Mere liye tu kaafi hai. (Seedhe Maut - Nadaan)",
        "Just a reminder: I appreciate you.",
        "Happiness looks gorgeous on you.",
        "Cause you're a sky, 'cause you're a sky full of stars. (Coldplay)",
        "Believe in the magic of new beginnings.",

        # 31-40
        "Tu mera koi na hoke bhi kuch laage. (Arijit Singh)",
        "I hope today brings you as much joy as you bring me.",
        "You are my favorite distraction.",
        "Pal pal dil ke paas, tum rehti ho. (Kishore Kumar)",
        "Never apologize for being you.",
        "Dream big, little one.",
        "Baby you're a firework! (Katy Perry)",
        "Main tenu samjhawan ki... na tere bina lagda jee.",
        "Your energy is my favorite vibe.",
        "Stay wild, stay free.",

        # 41-50
        "Jeene ke liye socha hi nahi, dard sambhalne honge... (Arijit)",
        "You are stronger than you think.",
        "Thank you for existing.",
        "O Rangrez, tere rang dariya mein... (Bhaag Milkha Bhaag)",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Tere bina zindagi se koi shikwa toh nahi... (Classic)",
        "You are my sunshine on a cloudy day.",
        "Bas rukna mat. Chalte rehna. (Motivational)",
        "Everything is better when we do it together.",
        "Day 50! And I still haven't run out of reasons to love you."
    ]

    # Get Message Index based on Day of Year
    today_index = datetime.datetime.now().timetuple().tm_yday
    todays_message = messages[today_index % len(messages)]

    st.markdown(f"""
    <div class="daily-card">
        <div class="quote-text">
            " {todays_message} "
        </div>
        <div class="sub-text">
            ~ A reminder for today ({today_date.strftime('%B %d')})
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("✨ Tap for Good Vibes ✨", use_container_width=True):
            st.toast("Wishing you the best day ahead! 💖")
            st.balloons()