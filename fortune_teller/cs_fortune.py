import random

def cs_fortune(category: str = "random") -> str:
    fortunes = {
        "tech": [
            "You will fix a bug... but create two new ones.",
            "Your commit messages will inspire thousands of developers.",
            "Your code will compile on the first try... eventually.",
            "Rubber duck debugging will save your day—just don't question the duck.",
            "A segfault in your future? Fear not, for logs will guide you.",
            "You will spend more time reading logs than writing code."
        ],
        "startup": [
            "Your pitch deck will raise millions, as soon as you remove that one extra slide.",
            "A hidden co-founder is about to appear in your life.",
            "Your MVP will be hailed as the next big thing."
        ],
        "open source": [
            "You will become a beloved maintainer of a widely used project.",
            "A community member's pull request will solve your trickiest issue.",
            "Your next contribution will inspire new developers to join open source."
        ],
        "ai": [
            "Your ML model will become self-aware… proceed with caution!",
            "AI is just a fancy name for code that doesn't work yet.",
            "Your next project: bridging the gap between humans and robots."
        ],
        "career": [
            "You're on the path to landing your dream developer job!",
            "One day you'll write the code that changes the world.",
            "Your LinkedIn profile will attract a special opportunity."
        ]
    }

    if category in fortunes:
        return random.choice(fortunes[category])
    else:
        return (f"Oops: '{category}' is not from our list ( • ᴖ • ｡)"
            f"Please pick from this list of moods next time you decide to choose this function: tech, startup, open source, ai, career.")