def longest_word(sentence):
    words = sentence.split()
    
    longest = max(words, key=len)
    
    return longest

text = "Python programming is interesting and powerful"
print(longest_word(text))
