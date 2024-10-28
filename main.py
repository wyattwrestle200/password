import itertools
import string
import time

def generate_full_wordlist(filename="wordlist.txt"):
    start_time = time.time()
    total_combinations = 10**6 * 26 * 26
    counter = 0

    with open(filename, "w") as f:
        for numbers in range(1000000):  # From "000000" to "999999"
            num_str = f"{numbers:06}"  # Zero-padded to 6 digits
            for upper in string.ascii_uppercase:  # A-Z
                for lower in string.ascii_lowercase:  # a-z
                    word = f"{num_str}{upper}{lower}"
                    f.write(word + "\n")
                    
                    # Update counter and display progress every 1 million combinations
                    counter += 1
                    if counter % 1000000 == 0:
                        elapsed_time = time.time() - start_time
                        progress = counter / total_combinations
                        eta = elapsed_time / progress - elapsed_time
                        print(f"Progress: {progress:.2%
