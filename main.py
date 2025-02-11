import streamlit as st
import os
import importlib
from nodes.base_node import BaseNode

def load_nodes():
    """Dynamically loads all node classes from the nodes directory."""
    nodes = []
    nodes_dir = "nodes"
    
    for file in os.listdir(nodes_dir):
        if file.endswith("_node.py") and file != "base_node.py":
            module_name = f"nodes.{file[:-3]}"  # Remove ".py" and create module path
            module = importlib.import_module(module_name)
            
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, BaseNode) and obj is not BaseNode:
                    nodes.append(obj())  # Instantiate node class
    return nodes

def main():
    st.title("Modular Node-Based Streamlit App")
    
    shared_data = {}  # Dictionary to share data across nodes

    nodes = load_nodes()  # Dynamically load all nodes

    for node in nodes:
        with st.expander(f"{node.title}"):
            node.set_inputs()
            if st.button(f"Run {node.title}"):
                node.process(shared_data)
                node.display_result(shared_data)

if __name__ == "__main__":
    main()
