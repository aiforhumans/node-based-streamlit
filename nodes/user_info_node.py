# nodes/user_info_node.py

import streamlit as st

class UserInfoNode:
    def __init__(self, title="User Info Node"):
        self.title = title
        self.inputs = {}

    def set_inputs(self):
        st.header(self.title)
        self.inputs['name'] = st.text_input("Enter your name")
        self.inputs['email'] = st.text_input("Enter your email")
        return self.inputs

    def process(self, shared_data):
        name = self.inputs.get('name', '')
        email = self.inputs.get('email', '')
        # Store user info in shared_data
        shared_data['user_info'] = {
            "name": name,
            "email": email
        }

    def display_result(self, shared_data):
        user_info = shared_data.get('user_info', {})
        if user_info:
            st.markdown(f"**Name:** {user_info.get('name', 'N/A')}  \n"
                        f"**Email:** {user_info.get('email', 'N/A')}")
        else:
            st.warning("No user info has been provided.")
