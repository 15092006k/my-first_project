
import random
import streamlit as st

st.set_page_config(
    page_title="Karishma Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

st.markdown("<h1 style='text-align: center; color: #89b4fa;'>🎮 Karishma Rock Paper Scissors</h1>", unsafe_allow_html=True)

RULES = {
    'Classic': {
        'Rock': ['Scissors'],
        'Paper': ['Rock'],
        'Scissors': ['Paper']
    },
    'RPSLS (Extended)': {
        'Rock': ['Scissors', 'Lizard'],
        'Paper': ['Rock', 'Spock'],
        'Scissors': ['Paper', 'Lizard'],
        'Lizard': ['Spock', 'Paper'],
        'Spock': ['Scissors', 'Rock']
    }
}

CHOICE_EMOJIS = {'Rock': '🪨', 'Paper': '📄', 'Scissors': '✂️', 'Lizard': '🦎', 'Spock': '🖖'}

if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'ties' not in st.session_state:
    st.session_state.ties = 0

st.sidebar.header("⚙️ Settings")
mode = st.sidebar.radio("Select Game Mode", ["Classic", "RPSLS (Extended)"])

if st.sidebar.button("🔄 Reset Scores"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.rerun()

col1, col2, col3 = st.columns(3)
col1.metric("Player Score", st.session_state.player_score)
col2.metric("Ties", st.session_state.ties)
col3.metric("Computer Score", st.session_state.computer_score)

st.markdown("### Choose Your Move")
moves = list(RULES[mode].keys())
cols = st.columns(len(moves))

for idx, move in enumerate(moves):
    with cols[idx]:
        if st.button(f"{CHOICE_EMOJIS[move]}\n\n{move}", key=move, use_container_width=True):
            computer_move = random.choice(moves)
            if move == computer_move:
                st.session_state.ties += 1
                st.info(f"It's a Tie! Both chose {CHOICE_EMOJIS[move]} {move}.")
            elif computer_move in RULES[mode][move]:
                st.session_state.player_score += 1
                st.success(f"You Win! {CHOICE_EMOJIS[move]} {move} beats {CHOICE_EMOJIS[computer_move]} {computer_move}.")
            else:
                st.session_state.computer_score += 1
                st.error(f"You Lose! {CHOICE_EMOJIS[computer_move]} {computer_move} beats {CHOICE_EMOJIS[move]} {move}.")
