import streamlit as st
import spacy
from nodes.base_node import BaseNode

class NERNode(BaseNode):
    def __init__(self, title="Named Entity Recognition Node"):
        super().__init__(title)
        self.nlp = spacy.load("en_core_web_sm")

    def set_inputs(self):
        st.header(self.title)
        self.inputs['text'] = st.text_area("Enter text for Named Entity Recognition")

    def process(self, shared_data):
        text = self.inputs.get('text', '')
        if text:
            doc = self.nlp(text)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            shared_data['entities'] = entities

    def display_result(self, shared_data):
        if 'entities' in shared_data:
            st.markdown("### Extracted Entities:")
            for entity, label in shared_data['entities']:
                st.markdown(f"- **{entity}** ({label})")
        else:
            st.warning("No entities found.")
