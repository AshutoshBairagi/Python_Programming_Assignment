'''
Question 5. Create a function that returns a base-2 (binary) representation of a base-10
(decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to the left
will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
Examples
binary(1) ➞ &quot;1&quot;
# 1*1 = 1
binary(5) ➞ &quot;101&quot;
# 1*1 + 1*4 = 5
binary(10) ➞ &quot;1010&quot;
# 1*2 + 1*8 = 10
'''

def binary(num):
    try:
        return format(num,'b')
    except Exception as e:
        return e

print(binary(1))
print(binary(5))
print(binary(10))
