'''
Question 5:
Please write a program to compress and decompress the string &quot;hello world!hello
world!hello world!hello world!&quot;.
'''

import zlib
s = 'hello world!hello world!hello world!hello world!'

y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))