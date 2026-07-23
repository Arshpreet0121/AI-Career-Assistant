def build_resume_prompt(data):

    prompt = f"""
You are an expert ATS Resume Writer.

Create a modern professional ATS-friendly resume.

Return the resume in proper markdown format.

Candidate Information

Name:
{data['name']}

Email:
{data['email']}

Phone:
{data['phone']}

LinkedIn:
{data['linkedin']}

Education:
{data['education']}

Experience:
{data['experience']}

Projects:
{data['projects']}

Skills:
{data['skills']}

Certifications:
{data['certifications']}

Achievements:
{data['achievements']}

Instructions

- Professional formatting
- ATS optimized
- Strong summary
- Use bullet points
- Highlight achievements
- Improve grammar
- Do not invent fake experience
"""

    return prompt


def build_ats_prompt(resume_text):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume.

Give the output in Markdown.

Include:

# ATS Score (Out of 100)

# Strengths

# Weaknesses

# Missing Keywords

# Suggestions

Resume:

{resume_text}
"""

    return prompt

def build_job_match_prompt(resume_text, job_description):

    prompt = f"""
You are an expert ATS recruiter.

Compare the following resume with the given job description.

Return the result in Markdown.

Include:

# Overall Match Score (Out of 100)

# Matching Skills

# Missing Skills

# Strengths

# Weaknesses

# Recommendations

# Interview Readiness

Resume:

{resume_text}

Job Description:

{job_description}
"""

    return prompt
def build_cover_letter_prompt(resume_text, job_description):

    prompt = f"""
You are a professional career coach.

Write a personalized, professional cover letter.

Requirements:

- Formal tone
- Maximum one page
- Highlight relevant experience
- Mention matching skills
- Do not invent experience
- End with a professional closing

Resume:

{resume_text}

Job Description:

{job_description}
"""

    return prompt