"""Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""

s = set()
x = input("Enter the statement : ")
l = x.split(" ")

for i in l:
    s.add(i)
s1 = list(s)
s1.sort()
result = " ".join(s1)
print(result)

