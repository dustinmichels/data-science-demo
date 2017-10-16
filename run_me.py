"""
run_me.py
16 Oct 2017
"""

def opposite(word):
    """Makes uppercase word lower and visa versa.
    NOTE: Anything not lowercase treated as uppercase.
    """

    try:
        if word.islower():
            word = word.upper()
        else:
            word = word.lower()
    except AttributeError:
        print('You passed a "word" that is not a string, silly!')

    return word

my_word = "carleton"
print(my_word)

my_word = opposite(my_word)
print(my_word)
