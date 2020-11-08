from math import floor

def biggest_number(list:int):
    mid = floor(len(list) / 2)
    max_left = max(list[:mid])
    max_right = max(list[mid:])
    return max(max_left,max_right)

print(biggest_number([1,2,3,4,5,89,12,56,7,3,21,4,56,4,3]))