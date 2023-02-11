# imports spacy library
import spacy
nlp = spacy.load('en_core_web_md')

# creates doc objects for each of the words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#prints the similarity between the words on a scale of 0-1 where 1 is perfect
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# prints the similarities between numtiple tokens
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
# convents the sentence to an object
model_sentence = nlp(sentence_to_compare)
# prints the similarities between the sentences
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# The output of the similarity scores between "cat", "monkey", and "banana" is fascinating
# as it reflects the semantic similarity between the words.
# The higher score between "cat" and "monkey" compared to "cat" and "banana" suggests that
# the model perceives "cat" and "monkey" as more semantically related, which aligns with the fact
# that both are animals, whereas "banana" is a fruit.
# A similar relationship can also be observed by comparing the words "book" and "library".
# One can expect a high similarity score between these two words as a library is a place where books
# are stored and made available for reading, signifying a strong connection between them.
