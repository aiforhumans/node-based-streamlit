import streamlit as st
from deep_translator import GoogleTranslator
from nodes.base_node import BaseNode

class TranslationNode(BaseNode):
    def __init__(self, title="Translation Node"):
        super().__init__(title)

    def set_inputs(self):
        st.header(self.title)
        self.inputs['text'] = st.text_area("Enter text to translate")
        self.inputs['language'] = st.selectbox("Select target language", ["fr", "es", "de", "nl", "it", "ru"])
    
    def process(self, shared_data):
        text = self.inputs.get('text', '')
        language = self.inputs.get('language', 'en')
        if text:
            translated_text = GoogleTranslator(source="auto", target=language).translate(text)
            shared_data['translated_text'] = translated_text
    
    def display_result(self, shared_data):
        if 'translated_text' in shared_data:
            st.markdown(f"**Translated Text:** {shared_data['translated_text']}")
        else:
            st.warning("No text has been translated.")
