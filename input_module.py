
def collect_input():
    topic = input("Enter Blog Topic: ").strip()
    style = input("Enter Writing Style (Professional, Casual, Technical): ").strip()
    tone = input("Enter Tone (Formal, Friendly, Persuasive): ").strip()

    while True:
        try:
            words = int(input("Enter Approximate Word Count: "))
            if words <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Enter a valid whole number.")

    print("\n---------- Blog Details ----------")
    print("Blog Topic :", topic)
    print("Style      :", style)
    print("Tone       :", tone)
    print("Words      :", words)
    print("----------------------------------")

    return topic, style, tone, words
