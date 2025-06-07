# TalentScoutBot 🤖

An AI-powered Hiring Assistant built with Hugging Face Transformers and Streamlit to screen candidates based on their tech stack.

## 📦 Features
- Collects candidate details
- Generates 3–5 technical questions based on tech stack
- Clean UI with Streamlit
- Modular Python structure
- Uses `google/flan-t5-large` model

## 🏗️ Folder Structure
```
TalentScoutBot/
├── main.py                     # Streamlit entry point
├── app/
│   ├── __init__.py             # Init file
│   ├── ui.py                   # Streamlit UI
│   ├── prompts.py              # Prompts for info & questions
│   └── model.py                # HF model loading
├── requirements.txt
└── README.md
```

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/TalentScoutBot.git
cd TalentScoutBot
pip install -r requirements.txt
streamlit run main.py
```

## 🤗 Model Used
- `google/flan-t5-large` (Hugging Face)

## 📋 Sample Prompt
```
Tech Stack: Python, Django

Questions:
1. Explain Django's request/response lifecycle.
2. How do you use middleware in Django?
3. What are Python decorators and their use in Django?
```

## ✅ Future Enhancements
- Sentiment analysis
- Multilingual support
- Cloud deployment (Streamlit Cloud / Hugging Face Spaces)

## 📃 License
MIT License
