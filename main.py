
from input_module import collect_input
from blog_module import generate_blog
from title_module import generate_titles
from summary_module import generate_summary
from keyword_module import generate_keywords
from meta_module import generate_meta
from intent_module import detect_intent
from utils import save_blog


def main():
    current_blog = ""
    current_topic = ""
    current_style = ""
    current_tone = ""
    current_words = 500

    while True:
        print("\n========== AI BLOG GENERATOR ==========")
        print("1. Generate Blog")
        print("2. Generate Blog Titles")
        print("3. Generate Summary")
        print("4. Generate SEO Keywords")
        print("5. Generate Meta Description")
        print("6. Detect Intent from a Request")
        print("7. Exit")
        print("=======================================")

        choice = input("Enter your choice: ").strip()

        if choice == "7":
            print("Thank you for using AI Blog Generator!")
            break

        if choice == "1":
            topic, style, tone, words = collect_input()
            if not topic:
                print("Topic cannot be empty.")
                continue

            current_topic = topic
            current_style = style
            current_tone = tone
            current_words = words

            current_blog = generate_blog(
                topic, style, tone, words
            )

        elif choice == "2":
            topic = current_topic or input("Enter topic: ").strip()
            if topic:
                generate_titles(topic)
            else:
                print("Please enter a topic first.")

        elif choice in ("3", "4", "5"):
            if not current_blog:
                print("Generate a blog first using option 1.")
                continue

            if choice == "3":
                generate_summary(current_blog)
            elif choice == "4":
                generate_keywords(current_blog)
            else:
                generate_meta(current_blog)

        elif choice == "6":
            request = input("Enter your request: ").strip()
            intent = detect_intent(request)
            print("\nDetected Intent:", intent)

            if intent == "EXIT":
                break

            elif intent == "BLOG_GENERATION":
                topic, style, tone, words = collect_input()
                if topic:
                    current_topic = topic
                    current_style = style
                    current_tone = tone
                    current_words = words
                    current_blog = generate_blog(
                        topic, style, tone, words
                    )
                else:
                    print("Topic cannot be empty.")

            elif intent in (
                "SUMMARY",
                "KEYWORD_GENERATION",
                "META_DESCRIPTION"
            ):
                if not current_blog:
                    print("Generate a blog first using option 1.")
                elif intent == "SUMMARY":
                    generate_summary(current_blog)
                elif intent == "KEYWORD_GENERATION":
                    generate_keywords(current_blog)
                else:
                    generate_meta(current_blog)

            elif intent == "TITLE_GENERATION":
                topic = current_topic or input("Enter topic: ").strip()
                if topic:
                    generate_titles(topic)
                else:
                    print("Please enter a topic first.")

            else:
                print("Intent not recognized. Please try again.")

        else:
            print("Invalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
