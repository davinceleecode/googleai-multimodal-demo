import os
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Load API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set. Please set it in your environment variables.")

genai.configure(api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        prompt = request.form["prompt"]

        # Call Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        result = model.generate_content(prompt)

        response = result.text

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
