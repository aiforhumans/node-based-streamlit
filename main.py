# main.py

import streamlit as st
from nodes.system_prompt_node import SystemPromptNode
from nodes.user_info_node import UserInfoNode
from nodes.sentiment_node import SentimentNode

def main():
    st.title("Node-Based Modular Components in Streamlit")
    shared_data = {}

    system_node = SystemPromptNode()
    user_node = UserInfoNode()
    sentiment_node = SentimentNode()

    # System Prompt Node
    with st.expander("System Prompt Node"):
        system_node.set_inputs()
        if st.button("Store System Prompt"):
            system_node.process(shared_data)
            system_node.display_result(shared_data)

    # User Info Node
    with st.expander("User Info Node"):
        user_node.set_inputs()
        if st.button("Store User Info"):
            user_node.process(shared_data)
            user_node.display_result(shared_data)

    # Sentiment Node
    with st.expander("Sentiment Node"):
        sentiment_node.set_inputs()
        if st.button("Run Sentiment Analysis"):
            sentiment_node.process(shared_data)
            sentiment_node.display_result(shared_data)

if __name__ == "__main__":
    main()
