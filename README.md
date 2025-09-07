# Google AI Studio Multimodal Challenge – Gemini AI Demo

This is a simple **Flask web app** built for the [Google AI Studio Multimodal Challenge](https://aistudio.google.com/).  
It showcases Gemini’s **text understanding & generation** using a minimal Python backend.

## 🚀 Features
- Simple web UI with textarea input  
- Connects to **Gemini 1.5 Flash** via Google AI SDK  
- Displays AI-generated responses in real-time  

## 🛠️ Tech Stack
- Python 3 + Flask  
- Google Generative AI SDK (`google-generativeai`)  
- HTML + CSS frontend  

## ⚡ How to Run Locally
1. Clone this repo:
   ```bash
   git clone https://github.com/davinceleecode/googleai-multimodal-demo.git
   cd googleai-multimodal-demo

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate   # Windows
   pip install -r requirements.txt

3. Set your Google AI Studio key:
   ```powershell
   setx GOOGLE_API_KEY "your_api_key_here"
   
4. Run the app:
   ```bash
   python main.py
   
5. Open your browser at http://127.0.0.1:8080

## 🎯 Challenge Goal

This project demonstrates Gemini’s multimodal capabilities in a simple, interactive way.
Built for educational purposes and submitted to the Google AI Studio Multimodal Challenge.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

