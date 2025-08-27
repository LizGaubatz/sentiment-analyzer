import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

# Page title
st.title("🧠 Sentiment Analyzer")
st.subheader("Type a sentence below and see its emotional tone.")

# Text input
user_input = st.text_area("Enter text here:", height=150)

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input.strip():
        # Analyze with TextBlob
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Results
        st.markdown(f"**Polarity:** `{polarity:.2f}`")
        if polarity > 0.3:
            st.caption("💖 (aka. this feels pretty positive)")
        elif polarity < -0.3:
            st.caption("💔 (aka. that’s kinda negative, you okay?)")
        else:
            st.caption("😐 (aka. neutral vibes)")

        st.markdown(f"**Subjectivity:** `{subjectivity:.2f}`")
        if subjectivity > 0.5:
            st.caption("🤔 (aka. very opinion-based)")
        else:
            st.caption("📚 (aka. feels more fact-based)")


        # Show chart
        labels = ['Polarity', 'Subjectivity']
        scores = [polarity, subjectivity]
        colors = ['#8e6dc4', '#b18be8']

        fig, ax = plt.subplots()
        ax.bar(labels, scores, color=colors)
        ax.set_ylim([-1, 1])
        st.pyplot(fig)
    else:
        st.warning("Please enter some text to analyze.")
