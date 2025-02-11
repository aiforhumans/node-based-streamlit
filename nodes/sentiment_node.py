# nodes/sentiment_node.py

import streamlit as st

class SentimentNode:
    def __init__(self, title="Sentiment Analysis"):
        self.title = title
        self.inputs = {}

    def set_inputs(self):
        st.header(self.title)
        self.inputs['text'] = st.text_area("Enter text for sentiment analysis")
        return self.inputs

    def process(self, shared_data):
        text = self.inputs.get('text', '')
        # Simple sentiment logic
        sentiment = "Positive" if "good" in text else "Negative"
        shared_data['sentiment_result'] = sentiment

    def display_result(self, shared_data):
        if 'sentiment_result' in shared_data:
            st.markdown(f"**Sentiment:** {shared_data['sentiment_result']}")
        else:
            st.warning("No sentiment result found.")
