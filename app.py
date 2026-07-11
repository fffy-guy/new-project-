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
        index, chunks = create_vector_store(text)

context = "\n".join(search(index, chunks, "Generate Question Paper"))

paper = generate_question_paper(context)

        return f"""
<h2>Question Paper Generated</h2>

<pre>{paper}</pre>
"""

    return "No file selected"

if __name__ == "__main__":
    app.run(debug=True)from generator import generate_question_paper
from rag import create_vector_store, search
