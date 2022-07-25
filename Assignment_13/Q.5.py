"""Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10

DIGITS 3"""

x = input("Enter the statement: ")
x1 = x.split(" ")
l = "qwertyuiopasdfghjkllzxcvbnm"
d = "123456789"
letters=[]
digits = []
for i in x1:
    for j in i:
        if j in l:
            letters.append(j)
        if j in d:
            digits.append(j)


letters_count = 0
digits_count = 0
for i in letters:
    letters_count+=1
for j in digits:
    digits_count+=1
print("LETTERS ",letters_count)
print("DIGITS ",digits_count)
