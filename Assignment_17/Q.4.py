'''
Question4. Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
'''
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return factorial(num-1)*num
print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))