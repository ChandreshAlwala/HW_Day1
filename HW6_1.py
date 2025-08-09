# Write a program to take two lists from the user and print the common elements using
# sets.
list1 = (map(int, input("Enter elements of first list separated by spaces: ").split()))
list2 = (map(int, input("Enter elements of second list separated by spaces: ").split()))
set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)
