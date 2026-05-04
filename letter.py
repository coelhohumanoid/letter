import random
import time

import streamlit as st

# Page configuration
st.set_page_config(page_title="A letter for you 💌", page_icon="💌", layout="centered")

# Custom CSS for the letter's clean and elegant interface
st.markdown(
    """
    <style>
    .carta-container {
        background-color: #fdfdfd;
        padding: 40px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        font-family: 'Georgia', serif;
        color: #2b2b2b;
        line-height: 1.7;
        margin-top: 20px;
    }
    .data-local {
        text-align: right;
        color: #777;
        font-size: 0.9em;
        margin-bottom: 25px;
    }
    .assinatura {
        margin-top: 40px;
        font-style: italic;
        text-align: right;
    }
    .titulo-envelope {
        text-align: center;
        margin-top: 50px;
        color: #444;
    }
    /* Animation for the hearts, chicks, and sparkles */
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0.8; }
    }
    .emoji-rain {
        position: fixed;
        top: -10vh;
        z-index: 9999;
        pointer-events: none;
        animation: fall linear forwards;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Function to generate the animation (now with chicks and sparkles)
def throw_special_effects():
    # Added 🐣 (chick) and ✨ (sparkles) to the list
    emojis = ["❤️", "🎉", "💖", "✨", "💕", "🎊", "🐥", "✨"]
    rain_html = ""
    for _ in range(80):  # Increased amount slightly for more effect
        emoji = random.choice(emojis)
        left = random.randint(0, 100)
        duration = random.uniform(3, 6)
        delay = random.uniform(0, 1)
        size = random.uniform(1.2, 2.8)  # Slightly varied sizes
        rain_html += f'<div class="emoji-rain" style="left: {left}%; font-size: {size}rem; animation-duration: {duration}s; animation-delay: {delay}s;">{emoji}</div>'
    st.markdown(rain_html, unsafe_allow_html=True)


# Initialize session state
if "carta_aberta" not in st.session_state:
    st.session_state.carta_aberta = False


def abrir_carta():
    st.session_state.carta_aberta = True


# UI Logic
if not st.session_state.carta_aberta:
    st.markdown(
        "<h2 class='titulo-envelope'>You have a new letter... ✉️</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    # Centering the button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("Open Letter", on_click=abrir_carta, use_container_width=True)
else:
    # Standard Streamlit balloons
    st.balloons()

    # Custom effects (hearts, chicks, sparkles)
    throw_special_effects()

    # Small dramatic pause
    with st.spinner("Opening the envelope..."):
        time.sleep(1.5)

    # Letter content in English
    st.markdown(
        """
    <div class="carta-container">
        <div class="data-local">May 4th, 2026 - Curitiba</div>
        <p>Dear Nuha,</p>
        <p>Today marks one month since we met. Today, as a way of celebrating, I would like to thank you. Thank you for not giving up. I know you had every justifiable reason to become a bad person. But instead, you chose to be fair, true to your values, with the certainty that your reward would come.</p>
        <p>I, on the other hand, never expected things to actually work out. But I also chose to do good without expecting anything in return. And as a consequence, here we are. Completely in love with each other's essence.</p>
        <p>I hope time will confirm what you already know. That we have a beautiful and constructive love ahead of us. That we will build our families, with the blessing of Allah, that we will be prosperous, just, and very, very happy.</p>
        <p>In this first month, I would like to reaffirm my vows and my commitment to be loyal, honest, and kind to you. And I hope time will prove my words to you. I will always do my best to make you happy and to satisfy you. I want to give myself to you, body and soul.</p>
        <p>I thank Allah for bringing you into my life. I am ready to embrace this new stage of my journey. You are part of my life now; you are part of my personal legend.</p>
        <p>Thank you, my love! Thank you for being who you are. For believing in yourself when no one else did. I promise you, you are not alone anymore. And you will never have to go through certain things again. And if you do, I will be right by your side!</p>
        <div class="assinatura">With love, Lucas.</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
