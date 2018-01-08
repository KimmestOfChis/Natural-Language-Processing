from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing - form of grouping things
# word tokenizer - sort by words
# sentence tokenizer - sort by sentences
# corpora - body of text, ex: medical journals, presidential speeches, English language
# lexicon - words and their meanings

# investor-speak vs. regular english-speak


example_text = "Hello Mr. Smith, how are you. The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard"

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
