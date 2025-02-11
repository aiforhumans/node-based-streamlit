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
