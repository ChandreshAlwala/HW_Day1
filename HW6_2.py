#  Write a program to check if two sets are disjoint or not.

set1 = set(map(int, input("Enter elements of first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by spaces: ").split()))
if set1.isdisjoint(set2):
    print("The sets are disjoint (no common elements).")
else:
    print("The sets are not disjoint (they have common elements).")