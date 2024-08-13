import random
import string
import time

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def spam_random_words(count, word_length):
    for _ in range(count):
        print(generate_random_word(word_length))
        time.sleep(0.5)  # here y can customize the delay
    print("generated successfully")

# first one is how much words are gonna get generated, second one is the length in letters
spam_random_words(10, 5)
# default is 10,5 
