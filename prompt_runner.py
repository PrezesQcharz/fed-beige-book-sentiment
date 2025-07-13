from sentiment_models.openai_gpt import analyze_sentiment_gpt

def run_custom_prompt(text, custom_prompt):
    scores = analyze_sentiment_gpt(text, custom_prompt)
    if scores:
        avg = sum(scores) / len(scores)
        avg = round(avg, 2)
    else:
        avg = "N/A"
    return {
        "prompt": custom_prompt,
        "scores": scores,
        "average": avg
    }
