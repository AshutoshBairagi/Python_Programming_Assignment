'''
Question1. Write a function that stutters a word as if someone is struggling to read it. The
first two letters are repeated twice with an ellipsis ... and space after each, and then the
word is pronounced with a question mark ?.
Examples
stutter(&quot;incredible&quot;) ➞ &quot;in... in... incredible?&quot;
stutter(&quot;enthusiastic&quot;) ➞ &quot;en... en... enthusiastic?&quot;
stutter(&quot;outstanding&quot;) ➞ &quot;ou... ou... outstanding?&quot;

Hint :- Assume all input is in lower case and at least two characters long.
'''
def stutter(name):
    try:
        r = name[0:2]
        return r+"..."+r+"..."+name+"?"
    except Exception as e:
        return e

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))

