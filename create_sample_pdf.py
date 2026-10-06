from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


output_path = "sample_data/sample_resume.pdf"

c = canvas.Canvas(output_path, pagesize=letter)

c.setFont("Helvetica-Bold", 18)
c.drawString(72, 750, "John Doe")

c.setFont("Helvetica", 11)
c.drawString(72, 725, "john.doe@email.com | +91-9876543210")

c.setFont("Helvetica-Bold", 14)
c.drawString(72, 680, "Skills")

c.setFont("Helvetica", 11)
c.drawString(72, 660, "Python, C++, Machine Learning, SQL, Flask, Scikit-learn")

c.setFont("Helvetica-Bold", 14)
c.drawString(72, 620, "Education")

c.setFont("Helvetica", 11)
c.drawString(72, 600, "M.Tech in Computer Science and Engineering")

c.setFont("Helvetica-Bold", 14)
c.drawString(72, 560, "Projects")

c.setFont("Helvetica", 11)
c.drawString(72, 540, "ATS Resume Parser and Job Description Matching System")
c.drawString(72, 520, "Developed an NLP-based system to compare resumes with job descriptions.")

c.save()

print(f"Sample resume created: {output_path}")