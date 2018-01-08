from nltk.corpus import wordnet
syns = wordnet.sysnsets("program")

print(syns)

#synset
print(syns[0].name())

#just the word
print(syns[0].lemmas()[0].name())

#defintion
print(syns[0].definition())

#examples
print(syns[0].examples)

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in sym.lemmas():
        print("l:", l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))


w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))
