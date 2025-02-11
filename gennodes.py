import os

# Define the directory and the nodes
NODES_DIR = "nodes"
NODE_FILES = {
    "translation_node.py": """\
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
""",
    "summarization_node.py": """\
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
""",
    "sentiment_intensity_node.py": """\
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nodes.base_node import BaseNode

class SentimentIntensityNode(BaseNode):
    def __init__(self, title="Sentiment Intensity Node"):
        super().__init__(title)
        self.analyzer = SentimentIntensityAnalyzer()

    def set_inputs(self):
        st.header(self.title)
        self.inputs['text'] = st.text_area("Enter text for sentiment analysis")
    
    def process(self, shared_data):
        text = self.inputs.get('text', '')
        if text:
            scores = self.analyzer.polarity_scores(text)
            shared_data['sentiment_scores'] = scores
    
    def display_result(self, shared_data):
        if 'sentiment_scores' in shared_data:
            scores = shared_data['sentiment_scores']
            st.markdown(f"**Sentiment Scores:**")
            st.json(scores)
        else:
            st.warning("No sentiment analysis performed.")
""",
    "ner_node.py": """\
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
""",
    "tts_node.py": """\
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
""",
    "image_caption_node.py": """\
import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from nodes.base_node import BaseNode

class ImageCaptionNode(BaseNode):
    def __init__(self, title="Image Captioning Node"):
        super().__init__(title)
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def set_inputs(self):
        st.header(self.title)
        self.inputs['image'] = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    def process(self, shared_data):
        image_file = self.inputs.get('image', None)
        if image_file:
            image = Image.open(image_file).convert("RGB")
            inputs = self.processor(images=image, return_tensors="pt")
            output = self.model.generate(**inputs)
            caption = self.processor.decode(output[0], skip_special_tokens=True)
            shared_data['image_caption'] = caption

    def display_result(self, shared_data):
        if 'image_caption' in shared_data:
            st.image(self.inputs['image'], caption=shared_data['image_caption'], use_column_width=True)
        else:
            st.warning("No caption generated.")
"""
}

# Create the directory if it does not exist
if not os.path.exists(NODES_DIR):
    os.makedirs(NODES_DIR)

# Create the Python files with content
for file_name, content in NODE_FILES.items():
    file_path = os.path.join(NODES_DIR, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {file_path}")

print("All nodes have been successfully generated!")
