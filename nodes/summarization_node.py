import streamlit as st
from transformers import pipeline
from nodes.base_node import BaseNode

class SummarizationNode(BaseNode):
    def __init__(self, title="Summarization Node"):
        super().__init__(title)
        self.summarizer = pipeline("summarization")

    def set_inputs(self):
        st.header(self.title)
        self.inputs['text'] = st.text_area("Enter text to summarize")
        self.inputs['max_length'] = st.slider("Summary Length", 10, 200, 50)
    
    def process(self, shared_data):
        text = self.inputs.get('text', '')
        max_length = self.inputs.get('max_length', 50)
        if text:
            summary = self.summarizer(text, max_length=max_length, min_length=10, do_sample=False)
            shared_data['summary'] = summary[0]['summary_text']
    
    def display_result(self, shared_data):
        if 'summary' in shared_data:
            st.markdown(f"**Summary:** {shared_data['summary']}")
        else:
            st.warning("No summary generated.")
