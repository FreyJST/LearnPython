def highest_even(li):
    
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)

print(highest_even([1,3,7,33,75,88,2,357,64]))
