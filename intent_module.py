
from utils import ask_ai


def detect_intent(user_request):
    prompt = f"""
Classify the user request into exactly ONE label:

BLOG_GENERATION
SUMMARY
KEYWORD_GENERATION
META_DESCRIPTION
TITLE_GENERATION
EXIT
UNKNOWN

Rules:
- A request to write or create a blog is BLOG_GENERATION.
- A request to summarize a blog is SUMMARY.
- A request for SEO keywords is KEYWORD_GENERATION.
- A request for an SEO meta description is META_DESCRIPTION.
- A request for blog titles is TITLE_GENERATION.
- A request to quit is EXIT.
- If unclear, return UNKNOWN.

Return only the label.

User request: {user_request}
"""
    result = ask_ai(
        prompt,
        system_prompt="You are an intent classifier. Return only one allowed label."
    )

    allowed = {
        "BLOG_GENERATION",
        "SUMMARY",
        "KEYWORD_GENERATION",
        "META_DESCRIPTION",
        "TITLE_GENERATION",
        "EXIT",
        "UNKNOWN"
    }

    label = result.strip().upper().replace(" ", "_")
    return label if label in allowed else "UNKNOWN"
