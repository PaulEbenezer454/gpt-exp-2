
from utils import ask_ai


def generate_meta(blog):
    prompt = f"""
Write one engaging SEO meta description for this blog.
Maximum length: 160 characters, including spaces.
Return only the description, with no quotation marks.

BLOG:
{blog}
"""
    result = ask_ai(prompt)

    # Enforce the maximum character limit.
    result = result.replace("\n", " ").strip()
    if len(result) > 160:
        result = result[:157].rsplit(" ", 1)[0] + "..."

    print("\nSEO Meta Description\n")
    print(result)
    print("Characters:", len(result))
    return result
