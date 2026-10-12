
from utils import ask_ai


def generate_titles(topic):
    prompt = f"""
Generate exactly five attractive blog titles about "{topic}".
Make them clear, engaging, and different from one another.
Return a numbered list from 1 to 5.
"""
    result = ask_ai(prompt)
    print("\nSuggested Titles\n")
    print(result)
    return result
