def generate_info_prompt():
    return """Please provide the following details in the format below:
- Full Name:
- Email Address:
- Phone Number:
- Years of Experience:
- Desired Position(s):
- Current Location:
- Tech Stack:
"""

def generate_tech_question_prompt(tech_stack):
    return f"""You are a technical interviewer. Based on the following tech stack, generate 3 to 5 technical interview questions:

Tech Stack: {tech_stack}

Make the questions relevant and moderately challenging.
Return as a numbered list.
"""

def extract_tech_stack(info_text):
    lines = info_text.split('\n')
    for line in lines:
        if 'Tech Stack' in line:
            return line.split(":")[-1].strip()
    return ""
