# Node-Based Streamlit App

## 📌 Project Overview

### **Goal**
The main goal of this project is to create a **modular and flexible** framework in Streamlit where each **node** encapsulates a specific functionality (e.g., user input, system prompt generation, AI processing, data transformation, etc.).

By organizing these nodes as **separate Python classes**, they can be easily reused, modified, and arranged dynamically, similar to how **node editors** work in visual programming tools.

### **How It Works**

#### **🔹 Node Definition**
Each node is a Python class that follows a structured pattern with three primary methods:

- `set_inputs()`: Defines the Streamlit UI elements for the node.
- `process(shared_data)`: Executes the main logic based on user input.
- `display_result(shared_data)`: Displays results in Streamlit.

#### **🔹 Dynamic Node Selection & Linking**
- The system **automatically detects new nodes** in the `nodes/` directory.
- Nodes can **share data dynamically** through a global `shared_data` dictionary.
- Developers can **add, remove, or modify nodes** without touching the core `main.py` file.

---

## 📂 Project Structure

```
node-based-streamlit/
├── nodes/
│   ├── base_node.py            # Abstract class for all nodes
│   ├── translation_node.py     # Node for translating text
│   ├── summarization_node.py   # Node for text summarization
│   ├── sentiment_node.py       # Node for sentiment analysis
│   ├── ner_node.py             # Named Entity Recognition node
│   ├── tts_node.py             # Text-to-Speech node
│   ├── image_caption_node.py   # AI-based image captioning node
│
├── main.py                     # Main entry point, dynamically loads nodes
├── generate_nodes.py            # Script to auto-generate nodes
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
```

---

## 🔧 Installation & Setup

1️⃣ **Clone the Repository:**
```bash
git clone https://github.com/yourusername/node-based-streamlit.git
cd node-based-streamlit
```

2️⃣ **Set Up a Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

3️⃣ **Run the Streamlit App:**
```bash
streamlit run main.py
```

4️⃣ **Open in Browser:**
- The app should be running at **http://localhost:8501**.

---

## 🚀 Advantages of This Node-Based Setup Over Standard Streamlit Development

### **1️⃣ Dynamic Node Loading → Plug & Play Functionality**
✅ **Advantage:**
- No need to modify `main.py` when adding new nodes.
- Simply drop a new `.py` file in the `nodes/` folder, and it **automatically appears in the UI**.

### **2️⃣ Modular & Reusable Components**
✅ **Advantage:**
- Each feature (e.g., translation, summarization) is **self-contained**.
- Nodes can be reused across different projects easily.

### **3️⃣ Scalable Architecture**
✅ **Advantage:**
- Easily add or remove nodes without breaking the system.
- Ideal for AI tools that grow over time.

### **4️⃣ Shared Data Handling Between Nodes**
✅ **Advantage:**
- A **global `shared_data` dictionary** allows nodes to share outputs.
- Example: The **Sentiment Node** can analyze **translated text** from the **Translation Node**.

### **5️⃣ More Organized Code (Easier to Maintain)**
✅ **Advantage:**
- Each feature is in its **own class**, making debugging & maintenance easier.
- No need to modify a massive `main.py` file.

### **6️⃣ Flexibility: Easily Switch or Remove Features**
✅ **Advantage:**
- Removing a feature = **Delete one file**.
- No need to modify core files.

### **7️⃣ Future-Proof: Ready for AI Pipelines & Drag-and-Drop Systems**
✅ **Advantage:**
- The system mimics **workflow automation tools** like ComfyUI and Node-RED.
- Future potential for a **visual drag-and-drop interface**.

### **🚀 When to Use This Over Normal Streamlit?**
✅ **Use this approach if:**
- You need **multiple independent AI tools** inside one app.
- You plan to **scale the app** over time.
- You want a **structured & clean** Streamlit project.

🔴 **Stick to normal Streamlit if:**
- You are making a **simple one-page app with 1-2 functions**.

---

## 📜 How to Add a New Node

1️⃣ **Create a new Python file** in `nodes/` (e.g., `nodes/new_feature_node.py`).

2️⃣ **Follow this structure:**
```python
import streamlit as st
from nodes.base_node import BaseNode

class NewFeatureNode(BaseNode):
    def __init__(self, title="New Feature Node"):
        super().__init__(title)
    
    def set_inputs(self):
        st.header(self.title)
        self.inputs['user_text'] = st.text_area("Enter text")
    
    def process(self, shared_data):
        shared_data['processed_text'] = self.inputs.get('user_text', '').upper()
    
    def display_result(self, shared_data):
        if 'processed_text' in shared_data:
            st.write(f"Processed Text: {shared_data['processed_text']}")
```

3️⃣ **Run the app:**
```bash
streamlit run main.py
```
- Your new node **automatically appears** in the UI! 🎉

---

## 🛠 Future Enhancements
- ✅ **Drag-and-Drop Node Editor**: Build a UI to visually arrange nodes.
- ✅ **Pre-Built AI Nodes**: Add sentiment analysis, translation, summarization, etc.
- ✅ **Conditional Workflows**: Auto-trigger nodes based on previous outputs.

---

## 📬 Contributions
- Feel free to **fork the repo**, add new nodes, and submit a **pull request**!
- For feature suggestions or bug reports, open an **issue** on GitHub.

Happy coding! 🚀

