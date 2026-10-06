# ATS Chatbot

An ATS (Applicant Tracking System) based resume analysis web application that compares a candidate's resume with a job description and provides an ATS score, skill matching analysis, resume-JD similarity, and improvement suggestions.

## Features

- Upload a resume in PDF format
- Extract resume text using Python and PyPDF
- Enter a job description directly in the web interface
- Extract technical skills from the resume and job description
- Identify matching and missing skills
- Calculate resume-JD similarity using TF-IDF and cosine similarity
- Generate an overall ATS score
- Provide resume improvement suggestions
- Interactive ATS Assistant for analysis feedback
- Responsive web interface

## Tech Stack

- Python
- Flask
- JavaScript
- HTML5
- CSS3
- PyPDF
- Natural Language Processing
- TF-IDF
- Cosine Similarity

## Project Structure

```text
ATS-Chatbot/
├── app.py
├── create_sample_pdf.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── text_preprocessor.py
│   ├── keyword_extractor.py
│   ├── similarity.py
│   ├── ats_scorer.py
│   └── suggestions.py
│
├── static/
│   ├── script.js
│   ├── skills.json
│   └── style.css
│
├── templates/
│   └── index.html
│
└── sample_data/
    ├── sample_resume.pdf
    └── sample_jd.txt