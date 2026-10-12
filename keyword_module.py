
from utils import ask_ai


def generate_keywords(blog):
    prompt = f"""
Generate 7 relevant SEO-friendly keywords or short key phrases
for the following blog.

Return one keyword per line.

BLOG:
{blog}
"""
    result = ask_ai(prompt)
    print("\nSEO Keywords\n")
    print(result)
    return result
