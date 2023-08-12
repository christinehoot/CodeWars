# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in vowels:
        counter += sentence.count(letter)
    return counter
