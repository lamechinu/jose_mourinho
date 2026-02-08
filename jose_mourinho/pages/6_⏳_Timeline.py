import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Our Journey ⏳",
    page_icon="🛤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 🎨 CSS STYLING (Vertical Line + Cards) ---
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

    /* TIMELINE STYLING */
    .timeline-container {
        position: relative;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px 0;
    }
    
    /* The Vertical Line */
    .timeline-container::after {
        content: '';
        position: absolute;
        width: 6px;
        background-color: white;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -3px;
        border-radius: 3px;
    }
    
    /* Event Card */
    .event-card {
        padding: 20px 30px;
        background-color: rgba(255, 255, 255, 0.9);
        position: relative;
        border-radius: 15px;
        width: 45%; /* Half width */
        margin-bottom: 30px;
        color: #333;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    /* Left Side Cards */
    .left {
        left: 0;
    }
    
    /* Right Side Cards */
    .right {
        left: 50%;
    }
    
    /* Dots on the line */
    .event-card::after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        right: -16px; /* Adjust for left cards */
        background-color: #ff00de;
        border: 4px solid #fff;
        top: 25px;
        border-radius: 50%;
        z-index: 1;
    }
    
    /* Fix dot for Right cards */
    .right::after {
        left: -16px;
    }

    /* Text Styling */
    .date-badge {
        background-color: #ff416c;
        color: white;
        padding: 5px 10px;
        border-radius: 10px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    h3 {
        margin: 0;
        color: #2c3e50;
    }
    p {
        margin-top: 10px;
        line-height: 1.5;
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


# --- ⏳ TIMELINE CONTENT ---

# --- ⏳ TIMELINE CONTENT ---

st.title("⏳ How It All Started...")
st.write("From Winners Science Academy to 'The Conjuring' scares... what a ride!")

# Timeline HTML Structure (Fixed Indentation)
st.markdown("""
<div class="timeline-container">
<div class="event-card left">
<div class="date-badge">2023</div>
<h3>🏫 The Classmates</h3>
<p>Winners Science Academy. Ek hi class mein the, par shuruaat mein anjaan the. Who knew this classroom would give me my favorite person?</p>
</div>
<div class="event-card right">
<div class="date-badge">Dec 1, 2023</div>
<h3>💬 First Conversation</h3>
<p>The day we finally broke the ice. Pehli baar baat hui thi. Choti si baat, par story wahin se shuru hui.</p>
</div>
<div class="event-card left">
<div class="date-badge">Dec 3, 2023</div>
<h3>🚌 The Picnic</h3>
<p>I saw you that day, and damn... <b>You looked beautiful.</b><br>
Uss din samajh gaya tha ki ye ladki sirf 'friend' nahi rahegi.</p>
</div>
<div class="event-card right">
<div class="date-badge">Jan 12, 2024 (1:41 AM)</div>
<h3>❤️ The Confession</h3>
<p>Late night himmat karke bol hi diya.<br>
<b>"I Love You."</b><br>
Best decision of my life.</p>
</div>
<div class="event-card left">
<div class="date-badge">Special Memory</div>
<h3>🥟 Homemade Momos</h3>
<p>Jab tune apne haathon se Momos bana ke khilaye the. <br>
Ladai kabhi 'crazy' nahi hui humari, bas aise sweet moments ne sab sambhal liya.</p>
</div>
<div class="event-card right">
<div class="date-badge">June 20, 2025</div>
<h3>🎬 Birthday & Sitaare Zameen Par</h3>
<p>My Birthday. We went to watch 'Sitaare Zameen Par'.<br>
Sitting next to you in the theatre > Any movie.</p>
</div>
<div class="event-card left">
<div class="date-badge">Core Memory 🔒</div>
<h3>👻 The Conjuring & Versova Beach</h3>
<p>Was great day, horror movie... aur wo darne ka bahana 😉 (IYKYK 😋). yumyumm.<br>
Aur next month Versova Beach ki shanti and vo coloring Perfect day.</p>
</div>
<div class="event-card right" style="background: #FFD700; border: 2px solid white;">
<div class="date-badge" style="background: white; color: black;">Feb 9, 2026</div>
<h3>👸 Happy 19th Birthday!</h3>
<p>Aur aaj hum yahan hain. <br>
Abhi toh bohot saare 'Firsts' baaki hain. <br>
<b>Happy Birthday Love!</b></p>
</div>
</div>
""", unsafe_allow_html=True)

st.write("---")
st.markdown("<center>💖 <b>To be continued...</b></center>", unsafe_allow_html=True)