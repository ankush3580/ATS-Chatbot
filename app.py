from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from src.resume_parser import extract_text_from_pdf


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    resume_text = ""
    jd_text = ""
    error = None

    if request.method == "POST":

        resume_file = request.files.get("resume")
        jd_text = request.form.get("jd_text", "")

        if not resume_file:
            error = "Please upload a resume PDF."

        elif not jd_text.strip():
            error = "Please enter a job description."

        elif not resume_file.filename.lower().endswith(".pdf"):
            error = "Only PDF resumes are supported."

        else:

            filename = secure_filename(resume_file.filename)

            resume_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            resume_file.save(resume_path)

            try:

                # Python handles PDF text extraction.
                resume_text = extract_text_from_pdf(
                    resume_path
                )

                if not resume_text.strip():

                    raise ValueError(
                        "Could not extract text from the uploaded PDF."
                    )

            except Exception as e:

                error = f"Error processing resume: {str(e)}"

    return render_template(
        "index.html",
        resume_text=resume_text,
        jd_text=jd_text,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)