# import functions from respective modules
from fortune_teller.date_time import rand_date_time 
from fortune_teller.emoji_fortune import emoji_fortune
from fortune_teller.fortune_stories import fortune_story
from fortune_teller.get_fortune import get_fortune

def main():
    # 1. Call rand_date_time with a sample fortune message.
    fortune_msg = "You will write perfect code today! 🚀" 
    print("=== Random Date Time Fortune ===")
    print(rand_date_time(fortune_msg))
    print("-" * 40)

    # 2. Call emoji_fortune:
    # - Without any argument (default)
    # - With a specific mood ("funny")
    print("=== Emoji Fortune (default) ===")
    print(emoji_fortune())
    print("=== Emoji Fortune (with mood 'funny') ===")
    print(emoji_fortune("funny"))
    print("-" * 40)

    # 3. Call fortune_story with a sample name.
    name = "Alice"
    print("=== Fortune Story ===")
    print(fortune_story(name))
    print("-" * 40)

    # 4. Call get_fortune with a valid category (e.g., "tech")
    category = "tech"
    print("=== Get Fortune (category: tech) ===")
    print(get_fortune(category))
    print("-" * 40)

if __name__ == '__main__':
    main()
