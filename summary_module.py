
from utils import ask_ai


def generate_summary(blog):
    prompt = f"""
Summarize the following blog in approximately 100 words.
Keep the main ideas and important information.

BLOG:
{blog}
"""
    result = ask_ai(prompt)
    print("\nBlog Summary\n")
    print(result)
    return result

