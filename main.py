import random
import string

def generate_wordlist(entry_count=100, save_to_file=False):
    wordlist = []
    
    for _ in range(entry_count):
        numbers = ''.join(random.choices(string.digits, k=6))
        letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)
        word = numbers + letters
        wordlist.append(word)

    if save_to_file:
        with open("wordlist.txt", "w") as f:
            for word in wordlist:
                f.write(word + "\n")

    return wordlist

# Generate a list of 100 entries and print
wordlist = generate_wordlist(entry_count=100, save_to_file=True)
print(wordlist)
