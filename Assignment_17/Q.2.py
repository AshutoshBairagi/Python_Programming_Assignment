'''
Question2. Create a function that returns True if a given inequality expression is correct and
False otherwise.
Examples
correct_signs(&quot;3 &lt; 7 &lt; 11&quot;) ➞ True
correct_signs(&quot;13 &gt; 44 &gt; 33 &gt; 1&quot;) ➞ False
correct_signs(&quot;1 &lt; 2 &lt; 6 &lt; 9 &gt; 3&quot;) ➞ True
'''

def correct_signs(exp):
    try:
        return eval(exp)
    except Exception as e:
        return e
print(correct_signs("3<7<11"))
print(correct_signs("13>44>33>1"))
print(correct_signs("1<2<6<9>3"))