import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code(code: str) -> str:
    prompt = f"""
You are a senior software engineer and strict code reviewer.
Format your response in clean markdown with headers and bullet points.

Analyze the following code and provide structured feedback:

1. Code Quality Review
2. Bug Detection
3. Performance Improvements
4. Clean Code Suggestions
5. Security Concerns (if any)
6. Provide an improved refactored version of the code.

Be clear, structured, and professional.

Also provide:
- Code Quality Score (1-10)
- Security Score (1-10)
- Performance Score (1-10)

CODE:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert software engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content

print("API KEY:", os.getenv("GROQ_API_KEY"))
