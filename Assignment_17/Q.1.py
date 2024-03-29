'''
Question1. Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''
def evenly_divisible(a,b,c):
    try:
        l=[0]
        for i in range(a,b+1):
            if i % c==0:
                l.append(i)
        return sum(l)
    except Exception as e:
        return e

print(evenly_divisible(1,10,20))
print(evenly_divisible(1,10,2))
print(evenly_divisible(1,10,3))