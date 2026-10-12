
import ollama
from pathlib import Path

MODEL = "llama3.2"

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

BLOG_FILE = OUTPUT_DIR / "generated_blog.txt"


def ask_ai(prompt, system_prompt="You are a helpful AI writing assistant."):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.message.content.strip()


def save_blog(blog):
    BLOG_FILE.write_text(blog, encoding="utf-8")
    print(f"\nBlog saved to: {BLOG_FILE}")
