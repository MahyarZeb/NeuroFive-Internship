🌸 ResumeBloom
Turn your resume into a stronger version of you.

ResumeBloom is a small AI-powered resume feedback application that compares a user's resume with a target job description and provides practical, personalized feedback.

✨ Problem

Many students and early-career job seekers submit resumes without knowing whether their resume actually matches the job they are applying for.

ResumeBloom helps solve this problem by giving users an instant AI-powered review.

🌷 Core Flow
User pastes their resume.
User pastes a target job description.
ResumeBloom sends both to an AI model.
The AI analyzes the resume against the job.
The application displays:
Resume score
Strengths
Missing keywords
Improvement suggestions
Rewritten resume bullets
Interview questions
🧠 AI Approach

The application uses a structured prompt that instructs the model to act as a resume coach.

The prompt also prevents the AI from inventing experience or qualifications.

The model is instructed to return structured JSON containing:

score
summary
strengths
missing_keywords
improvements
rewritten_bullets
interview_questions

This makes the AI response easier for the frontend to process reliably.

🛠 Tech Stack
Python
Flask
OpenAI API
HTML
CSS
JavaScript
python-dotenv
📁 Project Structure
resume-bloom/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js

🚀 How to Run

Create a virtual environment:

python -m venv venv


Activate it.

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Create a .env file:

OPENAI_API_KEY=your_api_key_here


Start the application:

python app.py


Then open:

http://127.0.0.1:5000

🧪 Testing

The application should be tested with several realistic cases:

Test 1 — Software Engineering Student

Use a student resume with Python, Flask, SQL, and Git and compare it with a junior software engineer job description.

Test 2 — Marketing Student

Use a marketing resume and compare it with a digital marketing internship.

Test 3 — Data Analyst

Use a resume containing Excel, SQL, and Python and compare it with a data analyst position.

Test 4 — Weak Resume

Use a resume containing vague statements such as "worked on projects" and check whether the AI recommends more specific descriptions.

Test 5 — Strong Resume

Use a highly targeted resume and check whether the application gives a high score while still providing useful suggestions.

🌱 What I Would Improve

With more time, I would add:

PDF resume upload
Resume history
Login/accounts
ATS keyword matching
Downloadable improved resume
Job-description URL support
RAG using resume-writing guidelines
Analytics showing score improvements over time
🎯 Capstone Concepts Demonstrated

ResumeBloom demonstrates:

Full-stack application development
API integration
Prompt engineering
Structured AI output
Frontend/backend communication
Environment-variable security
Error handling
User testing
Responsive UI design
💡 Why This Project

The project is intentionally small enough to finish and polish, while still demonstrating a complete AI application rather than simply calling an AI API.