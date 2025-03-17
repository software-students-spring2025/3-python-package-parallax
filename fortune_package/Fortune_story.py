import random 
def fortune_story(name):
    stories= [
        f"{name} woke up on day to find out that his body was taken over by AI. When he thought of something his body would code it in an instance, but no matter what he did there always bugs",
        f"The universe opens and {name} sees the infinte possiblites of error in his code. After looking through millions of possiblites {name} found the one universe where they fixed their code",
        f"While in the ancient Libary, {name} found the ancient text of auto debugger,they opened the book and it read one line: in order to not have bugs one must not code",
        f"{name} searched far and wide in order to find the Grand AI that would save the world. After finding it the world turned into 1s and 0s and {name} was now the Grand AI"
    ]
    return random.choices(stories)