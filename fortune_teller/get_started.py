import sys
from fortune_teller.mood_fortune import mood_fortune
from fortune_teller.fortune_stories import fortune_story
from fortune_teller.cs_fortune import cs_fortune
from fortune_teller.date_time import rand_date_time

def main():
    """
    Welcome to the Fortune Teller!
    
    This interactive program will guide you through choosing one of the three fortune functions
    (mood_fortune, fortune_story, or cs_fortune) and optionally combining one of their fortunes
    with a random future date using rand_date_time function. Try your luck ;)!
    
    Usage:
        1. Run in your terminal:
            python -m fortune_teller.get_started
        
        2. Follow the prompts to:
           - Pick a fortune function (mood, story, or CS).
           - Provide any required details (e.g., mood, name, or category).
           - Optionally add a random future date to your fortune by supplying a current date in
             'YYYY-MM-DD' format (with the year <= 2025).
    """
    print("Welcome to the Fortune Teller!")
    print("Try your luck today with one of the following fortune functions:")
    print("  1) mood_fortune (receive fortunes based on your mood)")
    print("  2) fortune_story (receive personalized story fortunes)")
    print("  3) cs_fortune (receive fortunes based on a computer science topic)")
    print("  4) Quit")
    
    while True:
        choice = input("\nWhich fortune function would you like to use? type 1/2/3/4) ").strip()
        
        if choice == "1":
            handle_mood_fortune()
        elif choice == "2":
            handle_fortune_story()
        elif choice == "3":
            handle_cs_fortune()
        elif choice == "4":
            print("Goodbye for now but remember: luck waits for no one!")
            sys.exit(0)
        else:
            print("Oops, invalid choice. Please enter 1, 2, 3, or 4.")

def handle_mood_fortune():
    """
    Guides the user to pick a mood, gets a fortune, and optionally combines it with a random date.
    """
    print("\nYou chose 'mood_fortune'. Now, choose your mood: positive, funny, cursed, motivational.")
    mood = input("Enter your mood: ").strip()
    
    # Get the fortune from mood_fortune
    fortune = mood_fortune(mood)
    
    # Check if the function returned an error (invalid mood)
    if fortune.startswith("Error:"):
        print(fortune)
        return
    
    print(f"\nYour mood-based fortune is:\n  {fortune}")
    
    # Ask if the user wants to combine this fortune with a random future date
    add_date = input("\nWould you like to know when this fortune is going to happen?! (y/n) ").strip().lower()
    if add_date == "y":
        current_date_str = input("Please enter the current date (YYYY-MM-DD, year <= 2025): ").strip()
        combined = rand_date_time(current_date_str, fortune)
        print(f"\nHere's your fortune:\n  {combined}")

def handle_fortune_story():
    """
    Guides the user to provide a name, gets a story fortune, and optionally combines it with a random date.
    """
    print("\nYou chose 'fortune_story'.")
    name = input("For whom is this fortune? (enter your/their name): ").strip()
    
    # Get the fortune story
    story = fortune_story(name)
    
    # Check if the function returned an error (e.g., empty name)
    if story.startswith("Error:"):
        print(story)
        return
    
    print(f"\nYour story fortune is:\n  {story}")
    
    # Ask if the user wants to combine this fortune with a random future date
    add_date = input("\nWould you like to know when this fortune is going to happen?! (y/n) ").strip().lower()
    if add_date == "y":
        current_date_str = input("Please enter the current date (YYYY-MM-DD, year <= 2025): ").strip()
        combined = rand_date_time(current_date_str, story)
        print(f"\nHere's your fortune:\n  {combined}")

def handle_cs_fortune():
    """
    Guides the user to pick a category, gets a CS fortune, and optionally combines it with a random date.
    """
    print("\nYou chose 'cs_fortune'. Now, please pick a category: tech, startup, open source, ai, career.")
    category = input("Enter your category: ").strip()
    
    # Get the CS fortune
    cs_message = cs_fortune(category)
    
    # Check if the function returned an error (invalid category)
    if cs_message.startswith("Error:"):
        print(cs_message)
        return
    
    print(f"\nYour CS fortune is:\n  {cs_message}")
    
    # Ask if the user wants to combine this fortune with a random future date
    add_date = input("\nWould you like to know when this fortune is going to happen?! (y/n) ").strip().lower()
    if add_date == "y":
        current_date_str = input("Please enter the current date (YYYY-MM-DD, year <= 2025): ").strip()
        combined = rand_date_time(current_date_str, cs_message)
        print(f"\nHere's your fortune:\n  {combined}")

if __name__ == "__main__":
    main()
