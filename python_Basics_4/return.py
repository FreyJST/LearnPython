def sum(num1, num2):
    def another_sum(num1, num2):
        return num1 + num2
    return another_sum(num1, num2)
    return 5
    print("This is Never going to be printed")

total = 50

print(sum(4,5))
print(sum(223,2))
print(sum(44, total))

print(type(sum))

total = sum(10,20)
print(total)

