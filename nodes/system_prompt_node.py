# nodes/system_prompt_node.py

import streamlit as st

class SystemPromptNode:
    def __init__(self, title="System Prompt Node"):
        self.title = title
        self.inputs = {}

    def set_inputs(self):
        st.header(self.title)
        self.inputs['prompt'] = st.text_area("Enter the system prompt")
        return self.inputs

    def process(self, shared_data):
        prompt_text = self.inputs.get('prompt', '')
        # Here we simply store the prompt in shared_data
        shared_data['system_prompt'] = prompt_text

    def display_result(self, shared_data):
        if 'system_prompt' in shared_data:
            st.markdown(f"**System Prompt:** {shared_data['system_prompt']}")
        else:
            st.warning("No system prompt has been provided.")
