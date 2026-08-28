import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are ResumeBloom, a friendly but honest AI resume coach.

Your job is to analyze a candidate's resume against a target job description.

Be specific and practical. Do not invent experience, skills, degrees,
companies, or achievements that are not present in the resume.

Focus on:
1. Resume strengths
2. Missing or weak keywords
3. Formatting/content problems
4. Actionable improvements
5. Rewriting weak resume bullets without inventing facts
6. Interview questions relevant to the candidate

Return ONLY valid JSON matching this structure:

{
  "score": 0,
  "summary": "short overall assessment",
  "strengths": [
    "strength 1",
    "strength 2",
    "strength 3"
  ],
  "missing_keywords": [
    "keyword 1",
    "keyword 2"
  ],
  "improvements": [
    {
      "problem": "specific problem",
      "suggestion": "specific solution"
    }
  ],
  "rewritten_bullets": [
    {
      "original": "original bullet",
      "improved": "improved bullet"
    }
  ],
  "interview_questions": [
    "question 1",
    "question 2",
    "question 3"
  ]
}

The score must be an integer from 0 to 100.
Keep the response concise and useful.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    resume = data.get("resume", "").strip()
    job_description = data.get("job_description", "").strip()

    if not resume or not job_description:
        return jsonify({
            "error": "Please provide both your resume and the job description."
        }), 400

    user_prompt = f"""
Analyze this resume against the target job description.

RESUME:
{resume}

TARGET JOB DESCRIPTION:
{job_description}
"""

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=SYSTEM_PROMPT,
            input=user_prompt
        )

        result_text = response.output_text

        # Remove accidental markdown code fences
        result_text = result_text.replace("```json", "").replace("```", "").strip()

        result = json.loads(result_text)

        return jsonify(result)

    except json.JSONDecodeError:
        return jsonify({
            "error": "The AI returned an invalid response. Please try again."
        }), 500

    except Exception as e:
        print("ERROR:", e)

        return jsonify({
            "error": "Something went wrong while analyzing your resume."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
