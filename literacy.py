# index = .0588 * L - .296 X S -15.8

# L is the average number of letters per 100 words
# S is the average number of sentences per 100 words


import re

string = 'Hey dude. How are you? Wow thats good for you!'

def splitSentences(string):
    sentences = re.split('[.?!]', string)
    sentences = list(filter(None, sentences))
    for index, sentence in enumerate(sentences):
        words = sentence.split(' ')
        print(words)
        length = len(words)
        print(f"sentence {index}. Wordcount: {length}. Letter count: ")

splitSentences(string)