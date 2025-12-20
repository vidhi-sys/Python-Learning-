# Mad Libs is a word game where players fill in blanks in a story template with different parts of speech (nouns, verbs, adjectives, etc.) without knowing the story context
import random
import string
def generate_random_string(length):
    characters = string.ascii_letters + string.digits # Includes A-Z, a-z, 0-9
    random_string = ''.join(random.choices(characters, k=length)) # Use random.choices for repetition
    return random_string
madLib=f"computer programming is so { generate_random_string(15)}: it makes me so excited becaus i love to { generate_random_string(5)} .stay hydrtaed and{  generate_random_string(7)} like you are { generate_random_string(2)}" 
print(madLib)
