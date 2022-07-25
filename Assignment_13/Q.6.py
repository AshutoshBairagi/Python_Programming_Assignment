'''Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''

x= input("Enter multiple passwords : ")
l = x.split(",")
small_case = "qwertyuiopasdfghjklzxcvbnm"
cap_case = small_case.upper()
special_char = "$#@"
min_length = 6
max_length = 12
l1 = []
for j in l:
    small_case_bool = False
    cap_case_bool = False
    special_char_bool = False
    count = 0
    for i in j:
        if i in small_case:
            small_case_bool = True
        if i in cap_case:
            cap_case_bool = True
        if i in special_char:
            special_char_bool = True
        count+=1
    if (small_case_bool == True) and (cap_case_bool == True) and (special_char_bool == True) and (
            count in range(min_length, max_length + 1)):
        l1.append(j)
        result = ",".join(l1)
print(result)




