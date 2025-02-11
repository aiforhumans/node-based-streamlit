import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nodes.base_node import BaseNode

class SentimentIntensityNode(BaseNode):
    def __init__(self, title="Sentiment Intensity Node"):
        super().__init__(title)
        self.analyzer = SentimentIntensityAnalyzer()

    def set_inputs(self):
        st.header(self.title)
        self.inputs['text'] = st.text_area("Enter text for sentiment analysis")
    
    def process(self, shared_data):
        text = self.inputs.get('text', '')
        if text:
            scores = self.analyzer.polarity_scores(text)
            shared_data['sentiment_scores'] = scores
    
    def display_result(self, shared_data):
        if 'sentiment_scores' in shared_data:
            scores = shared_data['sentiment_scores']
            st.markdown(f"**Sentiment Scores:**")
            st.json(scores)
        else:
            st.warning("No sentiment analysis performed.")
