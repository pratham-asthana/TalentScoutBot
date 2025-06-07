from prompts import (
    get_greeting_prompt,
    get_info_prompt,
    get_question_prompt,
    get_fallback_prompt,
    get_exit_prompt
)
from utils import generate_response

class Chatbot:
    def __init__(self):
        self.history: list[str] = []
        self.state = "greeting"
        self.candidate_info = {}

    def process(self, user_input: str) -> str:
        if user_input.lower() == "exit":
            response = get_exit_prompt()
            self.state = "ended"
            return response

        if self.state == "greeting":
            prompt = get_greeting_prompt() + get_info_prompt()
            self.history.append(f"assistant: {prompt}")
            self.state = "collecting_info"
            return prompt

        if self.state == "collecting_info":
            
            lines = [l.strip() for l in user_input.split("\n") if l.strip()]
            keys = ["name", "email", "phone", "experience", "position", "location", "tech_stack"]
            for k, v in zip(keys, lines):
                self.candidate_info[k] = v
            tech = self.candidate_info.get("tech_stack", "")
            prompt = get_question_prompt(tech)
            self.history.append(f"assistant: {prompt}")
            self.state = "asking_questions"
            return prompt

        if self.state == "asking_questions":
            
            q_prompt = get_question_prompt(self.candidate_info.get("tech_stack", ""))
            response = generate_response(q_prompt, self.history)
            self.history.append(f"assistant: {response}")
            
            self.state = "ended"
            return response

        
        return get_fallback_prompt()