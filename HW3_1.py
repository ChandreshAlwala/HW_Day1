import string

def IsPangram(sentence):
    sentence = sentence.lower()
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence)

    return alphabet_set <= sentence_set

sentence = "The quick brown fox jumps over the lazy dog"
print(IsPangram(sentence))  
