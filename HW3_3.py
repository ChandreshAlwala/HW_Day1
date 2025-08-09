def count_upper_lower(text):
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

sentence = "Hello World! Python Is FUN."
upper, lower = count_upper_lower(sentence)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)