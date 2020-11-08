from math import floor

def count_elements(list):
    mid = floor(len(list) / 2)
    left = list[:mid]
    right = list[mid:]
    return len(left) + len(right)


print(count_elements(['d','t','er','e','q','ew','fd','4','5']))