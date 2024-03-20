import streamlit as st

def calculate_payoff(player_a, player_b, peace_peace, war_war, peace_war, war_peace):
    if player_a == "Peace" and player_b == "Peace":
        return peace_peace
    elif player_a == "War" and player_b == "War":
        return war_war
    elif player_a == "Peace" and player_b == "War":
        return peace_war
    elif player_a == "War" and player_b == "Peace":
        return war_peace

def main():
    st.title("Peace War Game")
    st.write("Welcome to the Peace War game! Choose your strategy and see the payoff.")

    player_a = st.selectbox("Player A's Strategy:", ["Peace", "War"])
    player_b = st.selectbox("Player B's Strategy:", ["Peace", "War"])

    peace_peace = st.number_input("Enter payoff for Peace-Peace:", min_value=0)
    war_war = st.number_input("Enter payoff for War-War:", min_value=0)
    peace_war = st.number_input("Enter payoff for Peace-War:", min_value=0)
    war_peace = st.number_input("Enter payoff for War-Peace:", min_value=0)

    if st.button("Calculate Payoff"):
        payoff_a = 0
        payoff_b = 0
        if player_a == "Peace" and player_b == "Peace":
            payoff_a = peace_peace
            payoff_b = peace_peace
        elif player_a == "War" and player_b == "War":
            payoff_a = war_war
            payoff_b = war_war
        elif player_a == "Peace" and player_b == "War":
            payoff_a = peace_war
            payoff_b = war_peace
        elif player_a == "War" and player_b == "Peace":
            payoff_a = war_peace
            payoff_b = peace_war
        
        st.write(f"Player A's Payoff: {payoff_a}")
        st.write(f"Player B's Payoff: {payoff_b}")

if __name__ == "__main__":
    main()
