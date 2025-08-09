def word_count(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    return counts

text = "Python is fun and Python is powerful"
print(word_count(text))
