def super_add(*arg, **keyarg):
    total = 0
    for items in keyarg.values():
        total += items
    print(f'and the numbers are:- ', (*arg))
    return sum(arg) + total

print(super_add(1,2,3,4,5,6,8,9, num1=5, num2=10))


# Rules :- params, *args, default parameters, **kwargs
