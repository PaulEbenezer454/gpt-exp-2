
from utils import ask_ai, save_blog


def generate_blog(topic, style, tone, words):
    prompt = f"""
Write a complete blog about: {topic}

Writing style: {style}
Tone: {tone}
Target length: approximately {words} words.

Requirements:
- Create an attractive title.
- Include an introduction.
- Use meaningful headings and subheadings.
- Explain the topic clearly with useful details.
- Include a conclusion.
- Follow the requested writing style and tone.
- Aim for approximately the requested word count.
"""

    print("\nGenerating Blog...\n")
    blog = ask_ai(prompt)
    print("\n" + blog)
    save_blog(blog)
    return blog
