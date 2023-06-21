# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    if len(s) % 2 == 0:
        i = int(len(s) / 2)
        return s[i-1] + s[i]
    else:
        x = int(len(s) / 2 - .5)
        return s[x]


print(get_middle('test'))
print(get_middle('testing'))
