'''
Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels(&quot;the aardvark&quot;, &quot;#&quot;) ➞ &quot;th# ##rdv#rk&quot;
replace_vowels(&quot;minnie mouse&quot;, &quot;?&quot;) ➞ &quot;m?nn?? m??s?&quot;
replace_vowels(&quot;shakespeare&quot;, &quot;*&quot;) ➞ &quot;sh*k*sp**r*&quot;
'''

def replace_vowels(s,c):
    try:
        vowels='aeiou'
        for i in s:
            if i in vowels:
                s = s.replace(i,c)
        return s
    except Exception as e:
        return e

print(replace_vowels("the aardvark",'#'))
print(replace_vowels("minnie mouse",'?'))
print(replace_vowels("shakespeare",'*'))