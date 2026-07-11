from flask import Flask, render_template, request
import os
from pdf_utils import extract_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        text = extract_text(filepath)

        return f"""
        <h2>PDF Uploaded Successfully</h2>
        <p>File: {file.filename}</p>
        <p>Total Characters: {len(text)}</p>
        """

    return "No file selected"

if __name__ == "__main__":
    app.run(debug=True)
