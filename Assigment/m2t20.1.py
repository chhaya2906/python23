#Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word(words):
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

# Test the function
word_list = ["apple", "bananas", "kiwi", "orange"]
print("Length of the longest word:", longest_word(word_list))