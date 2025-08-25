import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("⚽ Virtual Football Match Simulator")

# Input odds
home_odds = st.number_input("Home Odds", value=2.50, step=0.01)
draw_odds = st.number_input("Draw Odds", value=2.53, step=0.01)
away_odds = st.number_input("Away Odds", value=2.73, step=0.01)

# Convert odds to probabilities
implied_probs = [1/home_odds, 1/draw_odds, 1/away_odds]
total = sum(implied_probs)
probs = [p/total for p in implied_probs]

st.write("📊 Implied Probabilities:")
st.write(f"Home: {probs[0]*100:.2f}%, Draw: {probs[1]*100:.2f}%, Away: {probs[2]*100:.2f}%")

# Number of simulations
n = st.slider("Number of Matches to Simulate", 1, 1000, 100)

# Run simulations
outcomes = np.random.choice(["Home", "Draw", "Away"], size=n, p=probs)
df = pd.DataFrame(outcomes, columns=["Result"])

# Show counts
counts = df["Result"].value_counts()
st.write("📈 Results after simulation:")
st.write(counts)

# Plot
fig, ax = plt.subplots()
counts.plot(kind="bar", ax=ax)
st.pyplot(fig)
