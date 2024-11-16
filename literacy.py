# index = .0588 * L - .296 X S -15.8

# L is the average number of letters per 100 words
# S is the average number of sentences per 100 words

#  i really really need to learn regular expressions in python and js to delete everything thats not a letter.
import re

string = 'Hey dude. How are you? Wow thats good for you! Do you like commas? I am going to try to break my app with commas and colons: ok, i tried; ; : ,.'

def splitSentences(string):
    translation_table = str.maketrans({",": "", ";": "", ":": ""})
    new_string = string.translate(translation_table)
    print(new_string)

    sentences = re.split('[.?!]', new_string)
    sentences = list(filter(None, sentences))
    for index, sentence in enumerate(sentences):
        words = sentence.split(' ')

        # iterates through the list of words backwards and empty strings
        for i, word in enumerate(words):
            if word == '':
                del words[i]

        length = len(words)
        print(f"sentence {index}. Wordcount: {length}. Words: {words} Letter count: ")

splitSentences(string)
