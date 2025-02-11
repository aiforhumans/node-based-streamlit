import streamlit as st
import pyttsx3
from nodes.base_node import BaseNode

class TTSNode(BaseNode):
    def __init__(self, title="Text-to-Speech Node"):
        super().__init__(title)
        self.tts_engine = pyttsx3.init()

    def set_inputs(self):
        st.header(self.title)
        self.inputs['text'] = st.text_area("Enter text for speech synthesis")

    def process(self, shared_data):
        text = self.inputs.get('text', '')
        if text:
            self.tts_engine.save_to_file(text, "speech.mp3")
            self.tts_engine.runAndWait()
            shared_data['tts_audio'] = "speech.mp3"

    def display_result(self, shared_data):
        if 'tts_audio' in shared_data:
            st.audio(shared_data['tts_audio'], format="audio/mp3")
        else:
            st.warning("No speech generated.")
