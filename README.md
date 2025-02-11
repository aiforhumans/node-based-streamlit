1. Project Overview
Goal
The main goal is to create a modular framework in Streamlit where each “node” (or component) encapsulates a specific functionality (e.g., user input, system prompt generation, API calls, data processing, etc.). By organizing these nodes as separate Python classes, you can easily rearrange or re-use them without rewriting large portions of your code. The overarching idea is to replicate a node editor’s benefits (modularity, flexibility, clarity) within a code-based environment.

How It Works

Node Definition:
Each node is represented by a Python class with three primary methods:

set_inputs(): Displays the Streamlit widgets needed for user input.
process(): Performs the node’s main logic based on the inputs.
display_result(): Renders the results back in the Streamlit app.
Shared Data Storage:
A global shared_data dictionary is passed among nodes, allowing them to access each other’s outputs via unique keys (e.g., shared_data["system_prompt"]).

Dynamic Node Selection & Linking:
Developers can pick which nodes to use and in which sequence. One node’s output can feed into the next node’s logic.

2. Project Structure
Below is a suggested directory layout for clarity and scalability:

bash
Copy
node-based-streamlit/
├── nodes/
│   ├── base_node.py           # (Optional) Abstract/base class for all nodes
│   ├── system_prompt_node.py  # Node that generates a system prompt
│   └── user_info_node.py      # Node that collects user information
│
├── main.py                    # Main entry point, controls app flow in Streamlit
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
Note: You can add more folders like utils/ or data/ if needed.

3. Installation
Clone the Repository:

bash
Copy
git clone https://github.com/yourusername/node-based-streamlit.git
cd node-based-streamlit
Set Up a Python Virtual Environment:

bash
Copy
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
Run the Streamlit App:

bash
Copy
streamlit run main.py
Open Your Browser:
By default, Streamlit typically opens on http://localhost:8501. You can start interacting with the nodes from there.

4. Boilerplate Code
Below is a minimal example to illustrate the entire workflow.

4.1 Base Node (Optional)
You can optionally define a base class to enforce the three required methods (set_inputs, process, display_result) for all nodes:

python
Copy
# nodes/base_node.py

import streamlit as st
from abc import ABC, abstractmethod

class BaseNode(ABC):
    def __init__(self, title):
        self.title = title
        self.inputs = {}

    @abstractmethod
    def set_inputs(self):
        pass

    @abstractmethod
    def process(self, shared_data):
        pass

    @abstractmethod
    def display_result(self, shared_data):
        pass
4.2 System Prompt Node
A simple node that generates a system prompt.

python
Copy
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
4.3 User Info Node
A node that collects user information (e.g., name, email).

python
Copy
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
4.4 Main App
main.py serves as the central controller. You can decide how to instantiate and run each node, in which order, and how to handle any dependencies between them.

python
Copy
# main.py

import streamlit as st

# Import your node classes
from nodes.system_prompt_node import SystemPromptNode
from nodes.user_info_node import UserInfoNode

def main():
    st.title("Node-Based Modular Components in Streamlit")

    # Shared data dictionary
    shared_data = {}

    # Instantiate Nodes
    system_node = SystemPromptNode()
    user_node = UserInfoNode()

    # Step 1: Node for System Prompt
    with st.expander("System Prompt Node", expanded=True):
        system_node.set_inputs()
        if st.button("Store System Prompt"):
            system_node.process(shared_data)
            system_node.display_result(shared_data)

    st.write("---")

    # Step 2: Node for User Info
    with st.expander("User Info Node", expanded=True):
        user_node.set_inputs()
        if st.button("Store User Info"):
            user_node.process(shared_data)
            user_node.display_result(shared_data)

    # You can add more nodes and chain them similarly

if __name__ == "__main__":
    main()
5. Instructions for Adding New Nodes
Create a New Node Class
Suppose you want to build a Sentiment Analysis node. Create a new file, e.g., nodes/sentiment_node.py.

Define the Node Methods
Each node should have three methods: set_inputs, process, and display_result.

python
Copy
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
Integrate the Node in main.py

python
Copy
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
6. Contribution Guidelines
Additions

Each new node file should be self-contained and follow the same pattern (3 methods, uses shared_data, etc.).
Keep node logic minimal; avoid large, monolithic nodes.
Testing

Test new nodes independently (e.g., comment out other nodes in main.py and confirm the new node runs correctly).
Check for broken references to shared_data.
Documentation

Update the project’s README (or dedicated doc pages) whenever you add or modify node functionality.
Provide clear instructions on how your node works and what inputs/outputs it expects.
7. Future Goals
UI for Node Connections

Potentially create a drag-and-drop visual interface that automatically arranges nodes in a workflow.
Common Node Library

Pre-built nodes for tasks like data cleaning, summarization, translation, etc.
Conditional Logic

Add support for branching logic (e.g., “If sentiment is negative, run an alternate node”).
Performance & Scalability

For larger applications, consider using a database or caching mechanism for shared data to improve performance.
