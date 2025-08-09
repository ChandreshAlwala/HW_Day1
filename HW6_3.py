# Write a program to find all unique vowels present in a given string using set.
def unique_vowels(s):
    vowels = set("aeiouAEIOU")      
    letters = set(s)                
    found_vowels = vowels.intersection(letters)  
    return found_vowels

input_str = input("Enter a string: ")
result = unique_vowels(input_str)

print("Unique vowels found:", result)