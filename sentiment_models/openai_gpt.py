import os
import re
from openai import OpenAI  # New client-based API

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment_gpt(text, prompt, n_times=3, model="gpt-3.5-turbo"):
    scores = []
    for _ in range(n_times):
        user_prompt = f"{prompt}\n\nText:\n{text[:3500]}"
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a sentiment analysis assistant."},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3
        )
        reply = response.choices[0].message.content
        try:
            score = float(extract_score(reply))
            scores.append(score)
        except Exception as e:
            print(f"Failed to parse score: {e} | Got: {reply}")
    return scores

def extract_score(reply):
    match = re.search(r'([-+]?\d*\.\d+|\d+)', reply)
    if match:
        return match.group(0)
    raise ValueError("Score not found")
