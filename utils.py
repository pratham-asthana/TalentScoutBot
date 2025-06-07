from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from dotenv import load_dotenv
import os

load_dotenv()
MODEL_ID = os.getenv("HF_MODEL_ID")
HF_TOKEN = os.getenv("HF_TOKEN", None)

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, use_auth_token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto",
    use_auth_token=HF_TOKEN
)

def generate_response(prompt: str, history: list[str], max_new_tokens: int = 200) -> str:
    # build full prompt with history
    full = "".join([f"{h}\n" for h in history]) + prompt
    inputs = tokenizer(full, return_tensors="pt", truncation=True, max_length=2048)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        temperature=0.8
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # strip history prefix
    return text[len(full):].strip()