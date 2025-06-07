def get_greeting_prompt():
    return (
        "You are TalentScout, an AI Hiring Assistant. "
        "Greet the candidate warmly, explain that you'll collect some details and assess their skills with a few technical questions. "
        "Type 'exit' anytime to end this chat.\n"
    )


def get_info_prompt():
    return (
        "Please provide the following information, each on a new line:\n"
        "1. Full Name\n"
        "2. Email Address\n"
        "3. Phone Number\n"
        "4. Years of Experience\n"
        "5. Desired Position(s)\n"
        "6. Current Location\n"
        "7. Your Tech Stack (e.g., Python, Django, PostgreSQL, Docker)\n"
    )


def get_question_prompt(tech_stack: str):
    return (
        f"Based on the tech stack: {tech_stack}, generate 3-5 technical interview questions "
        "that assess the candidate’s proficiency in these technologies. Keep the tone professional and concise."
    )


def get_fallback_prompt():
    return "Sorry, I didn’t understand that. Could you please rephrase or try again?"


def get_exit_prompt():
    return (
        "Thank you for sharing your information. Our team will review your responses and get in touch with you soon. Have a great day!"
    )