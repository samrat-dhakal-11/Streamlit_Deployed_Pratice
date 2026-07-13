import streamlit as st
import random
import time

# Page config
st.set_page_config(
    page_title="🌸 Shweta's Flower Garden 🌸",
    page_icon="🌺",
    layout="centered"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600&display=swap');

    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }

    .title-text {
        font-family: 'Pacifico', cursive !important;
        font-size: 3rem !important;
        color: #fff !important;
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        animation: float 3s ease-in-out infinite;
    }

    .subtitle-text {
        font-family: 'Poppins', sans-serif !important;
        font-size: 1.3rem !important;
        color: #ffe4e1 !important;
        text-align: center;
        margin-bottom: 2rem;
    }

    .flower-btn {
        background: linear-gradient(45deg, #ff6b6b, #feca57) !important;
        color: white !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        padding: 15px 40px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 8px 25px rgba(255,107,107,0.4) !important;
        transition: all 0.3s ease !important;
        cursor: pointer;
    }

    .flower-btn:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 12px 35px rgba(255,107,107,0.6) !important;
    }

    .flower-card {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: bloom 0.8s ease-out;
        margin: 10px;
    }

    .flower-emoji {
        font-size: 5rem;
        animation: sway 2s ease-in-out infinite;
        display: inline-block;
    }

    .flower-name {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: #764ba2;
        margin-top: 10px;
    }

    .flower-meaning {
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem;
        color: #666;
        font-style: italic;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    @keyframes bloom {
        0% { transform: scale(0) rotate(-10deg); opacity: 0; }
        100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }

    @keyframes sway {
        0%, 100% { transform: rotate(-5deg); }
        50% { transform: rotate(5deg); }
    }

    .sparkle {
        animation: sparkle 1.5s ease-in-out infinite;
    }

    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }

    .footer {
        text-align: center;
        color: rgba(255,255,255,0.7);
        font-family: 'Poppins', sans-serif;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Flower database with emojis and meanings
FLOWERS = [
    {"emoji": "🌹", "name": "Red Rose", "meaning": "Love & Passion"},
    {"emoji": "🌸", "name": "Cherry Blossom", "meaning": "Beauty & Renewal"},
    {"emoji": "🌻", "name": "Sunflower", "meaning": "Happiness & Warmth"},
    {"emoji": "🌷", "name": "Tulip", "meaning": "Perfect Love"},
    {"emoji": "🌺", "name": "Hibiscus", "meaning": "Delicate Beauty"},
    {"emoji": "🌼", "name": "Daisy", "meaning": "Innocence & Purity"},
    {"emoji": "🪷", "name": "Lotus", "meaning": "Spiritual Growth"},
    {"emoji": "🌺", "name": "Orchid", "meaning": "Luxury & Strength"},
    {"emoji": "🌻", "name": "Marigold", "meaning": "Creativity & Joy"},
    {"emoji": "🌹", "name": "Pink Rose", "meaning": "Grace & Admiration"},
    {"emoji": "🌸", "name": "Peony", "meaning": "Prosperity & Honor"},
    {"emoji": "🌷", "name": "Lavender", "meaning": "Calm & Serenity"},
    {"emoji": "🌼", "name": "Jasmine", "meaning": "Sweet Love"},
    {"emoji": "🌺", "name": "Plumeria", "meaning": "New Beginnings"},
    {"emoji": "🌻", "name": "Dahlia", "meaning": "Elegance & Dignity"},
    {"emoji": "🌸", "name": "Magnolia", "meaning": "Dignity & Nobility"},
    {"emoji": "🌹", "name": "White Rose", "meaning": "Purity & Innocence"},
    {"emoji": "🌷", "name": "Bluebell", "meaning": "Humility & Gratitude"},
    {"emoji": "🌼", "name": "Buttercup", "meaning": "Cheerfulness"},
    {"emoji": "🌺", "name": "Gardenia", "meaning": "Secret Love"},
]

# Initialize session state
if "flowers_generated" not in st.session_state:
    st.session_state.flowers_generated = []
if "total_flowers" not in st.session_state:
    st.session_state.total_flowers = 0
if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True

# Welcome message
st.markdown('<h1 class="title-text">🌸 Hello Shweta Dhakal 🌸</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">✨ Welcome to your magical flower garden! ✨<br>💐 🌺 🌷 🌻 🌹 🌼 💐</p>', unsafe_allow_html=True)

# Center the button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🌺 Click to Grow a Flower! 🌺", key="flower_btn", use_container_width=True):
        st.session_state.show_welcome = False

        # Pick random flowers (1 to 3 at a time for surprise!)
        num_flowers = random.randint(1, 3)
        new_flowers = []

        for _ in range(num_flowers):
            flower = random.choice(FLOWERS)
            new_flowers.append(flower)
            st.session_state.flowers_generated.append(flower)

        st.session_state.total_flowers += num_flowers

        # Show celebration
        st.balloons()

# Display flower count
if st.session_state.total_flowers > 0:
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <span style="font-size: 1.5rem; color: white; font-family: 'Poppins', sans-serif;">
            🌿 You have grown <b>{st.session_state.total_flowers}</b> beautiful flowers! 🌿
        </span>
    </div>
    """, unsafe_allow_html=True)

# Display all generated flowers
if st.session_state.flowers_generated:
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.3); margin: 30px 0;'>", unsafe_allow_html=True)

    # Display in a grid
    cols = st.columns(3)
    for i, flower in enumerate(st.session_state.flowers_generated):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="flower-card">
                <div class="flower-emoji">{flower['emoji']}</div>
                <div class="flower-name">{flower['name']}</div>
                <div class="flower-meaning">{flower['meaning']}</div>
            </div>
            """, unsafe_allow_html=True)

# Reset button
if st.session_state.total_flowers > 0:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Start Fresh Garden", key="reset"):
            st.session_state.flowers_generated = []
            st.session_state.total_flowers = 0
            st.session_state.show_welcome = True
            st.rerun()

# Footer
st.markdown("""
<div class="footer">
    💝 Made with love for Shweta Dhakal 💝<br>
    🌸 Every flower carries a wish for your happiness 🌸
</div>
""", unsafe_allow_html=True)
