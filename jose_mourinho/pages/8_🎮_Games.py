import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="The Bestie Quiz 🎮",
    page_icon="🧩",
    layout="centered", # Quiz ke liye centered layout best hai
    initial_sidebar_state="collapsed"
)

# --- 🎨 CSS STYLING (Floating Hearts + Quiz Style) ---
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

    /* Quiz Container */
    .quiz-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    /* Radio Button Text */
    .stRadio > label {
        color: white !important;
        font-size: 1.1rem !important;
    }
    p {
        font-size: 1.2rem;
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
    
    /* Result Box */
    .result-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #fff;
        color: #333;
        text-align: center;
        margin-top: 20px;
        border: 4px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🫧 FLOATING HEARTS BACKGROUND ---
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

# --- 🎮 QUIZ LOGIC ---

st.title("🎮 The 'Do You Know Me?' Quiz")
st.write("Let's see if you really know your boyfriend or not. 😉 (Be careful, options are tricky!)")

# QUESTIONS DATA
questions = [
    {
        "q": "1. Mera Favorite Food kya hai? (Soch ke batana!)",
        "options": ["Kadhi Chawal (Classic)", "Samosa (Love it)", "Jackfruit (Kathal)"],
        "correct": "Jackfruit (Kathal)",
        "hint": "Most people hate it, but I love it."
    },
    {
        "q": "2. Football mein Mera GOAT kaun hai? (Club: Real Madrid)",
        "options": ["Cristiano Ronaldo", "Luka Modrić", "Lionel Messi"],
        "correct": "Luka Modrić",
        "hint": "Magician of midfield."
    },
    {
        "q": "3. Humne Theater mein pehli movie kaunsi dekhi thi?",
        "options": ["12th Fail", "Sitaare Zameen Par", "Animal"],
        "correct": "Sitaare Zameen Par",
        "hint": "Birthday wale din!"
    },
    {
        "q": "4. Jab mujhe gussa aata hai, toh main kya karta hoon?",
        "options": ["Chillata hoon (Shout)", "Chup ho jata hoon (Silent)", "Cheezein phekta hoon"],
        "correct": "Chup ho jata hoon (Silent)",
        "hint": "Main bas gayab ho jata hoon."
    },
    {
        "q": "5. Meri sabse gandi aadat (Worst Habit) kya hai?",
        "options": ["Overthinking", "Gussa karna", "Aalas (Laziness)"],
        "correct": "Aalas (Laziness)",
        "hint": "Main kabhi kabhi bas pada rehta hoon."
    },
    {
        "q": "6. Agar mujhe kahin ghumne jana ho, toh Dream Place kaunsi hai?",
        "options": ["Ladakh (Mountains)", "Spain (Europe)", "Paris (Romance)"],
        "correct": "Spain (Europe)",
        "hint": "Not Ladakh this time."
    },
    {
        "q": "7. Humne pehli baar baat kab ki thi? (Date yaad hai?)",
        "options": ["3 Dec (Picnic wala din)", "1 Dec (Classroom)", "12 Jan (Proposal)"],
        "correct": "1 Dec (Classroom)",
        "hint": "Picnic se pehle."
    },
    {
        "q": "8. Main sabse zyada kya peeta hoon?",
        "options": ["Adrak wali Chai", "Cold Coffee", "Water (Paani)"],
        "correct": "Water (Paani)",
        "hint": "Hydration is key."
    },
    {
        "q": "9. Mera wo Nickname kya hai jo sirf TU bulati hai?",
        "options": ["Chinu", "Pog", "Baby pog"],
        "correct": "Baby pog",
        "hint": "Sabse cute wala."
    },
    {
        "q": "10. Mujhe sabse zyada dar kis cheez se lagta hai?",
        "options": ["Tujhe khone se", "Bhoot se", "Failure se"],
        "correct": "Failure se",
        "hint": "I want to be successful for us."
    },
    {
        "q": "11. Main free time mein sabse zyada kya karta hoon?",
        "options": ["Coding", "Sleeping", "YouTube"],
        "correct": "YouTube",
        "hint": "Scroll scroll scroll."
    },
    {
        "q": "12. Last Question: Kitna pyaar karta hoon main tujhse?",
        "options": ["Bahut sara", "Infinity", "100%"],
        "correct": "Infinity",
        "hint": "Koi limit nahi hai."
    }
]

# FORM START
with st.form("quiz_form"):
    score = 0
    user_answers = []
    
    for i, q in enumerate(questions):
        st.markdown(f"### {q['q']}")
        choice = st.radio(f"Select option for Q{i+1}:", q['options'], index=None, key=f"q{i}")
        user_answers.append(choice)
        st.write("---")

    submitted = st.form_submit_button("🔒 Lock My Answers")

# RESULT LOGIC
if submitted:
    # Calculate Score
    for i, q in enumerate(questions):
        if user_answers[i] == q['correct']:
            score += 1
            
    # DISPLAY RESULT
    if score == 12:
        st.balloons()
        st.markdown("""
        <div class="result-box">
            <h1>🏆 PERFECT SCORE! (12/12)</h1>
            <p>
                <b>OMG! You know me better than I know myself.</b> <br>
                Honestly, I am so lucky to have someone who pays attention to even the smallest details about me.
                Whether it's my love for Jackfruit (weird, I know) or my silent anger, you get me.
                <br><br>
                You are my "Baby pog", my safe place, and my forever. 
                Knowing that you know me this well just makes me love you even more (Infinity wala love).
                <br>
                <b>You won the game, but I won at life by having you. ❤️</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    elif score >= 9:
        st.markdown(f"""
        <div class="result-box">
            <h2>✨ Nice Try! Score: {score}/12</h2>
            <p>Close enough! You know the big things, but missed a few small details. 
            Koi baat nahi, I still love you. 😉</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown(f"""
        <div class="result-box" style="border-color: red;">
            <h2>💀 Score: {score}/12 - Hain??</h2>
            <p>Do you even know me? 😤 <br>
            Lagta hai mujhe aur attention chahiye! Jao wapas padho mere baare mein! (Just kidding, I love you 😘)</p>
        </div>
        """, unsafe_allow_html=True)

    # Show Correct Answers (if not perfect)
    if score < 12:
        with st.expander("👀 See Correct Answers"):
            for q in questions:
                st.write(f"**{q['q']}** -> ✅ {q['correct']}")

st.write("")
st.markdown("<center>🎮 <b>Thanks for playing, Love!</b></center>", unsafe_allow_html=True)