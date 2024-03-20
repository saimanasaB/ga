import streamlit as st
import random

# Function to determine the outcome of the peace/war decision
def peace_war_decision(player_decision):
    outcomes = ["Peace", "War"]
    computer_decision = random.choice(outcomes)
    if player_decision == "Peace":
        if computer_decision == "Peace":
            return "Both chose Peace. Both gain 2 points."
        else:
            return "You chose Peace, but your opponent chose War. You lose 1 point."
    else:
        if computer_decision == "Peace":
            return "You chose War, but your opponent chose Peace. You gain 3 points."
        else:
            return "Both chose War. No points are gained or lost."

# Main function to run the game
def main():
    st.title("Peace War Game")

    player_decision = st.radio("Choose your decision:", ("Peace", "War"))
    if st.button("Submit"):
        result = peace_war_decision(player_decision)
        st.write(result)

# Run the main function
if __name__ == "__main__":
    main()
