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
