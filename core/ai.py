from transformers import pipeline


messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="Qwen/Qwen2.5-Coder-7B")
pipe(messages)