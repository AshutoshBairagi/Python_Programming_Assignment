'''
Question 5
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: &quot;abcbba&quot;
String2: &quot;abcbda&quot;
Hamming Distance: 1 - &quot;b&quot; vs. &quot;d&quot; is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance(&quot;abcde&quot;, &quot;bcdef&quot;) ➞ 5
hamming_distance(&quot;abcde&quot;, &quot;abcde&quot;) ➞ 0
hamming_distance(&quot;strong&quot;, &quot;strung&quot;) ➞ 1
'''
def hamming_distance(s1,s2):
    try:
        count = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                pass
            else:
                count+=1
        return count
    except Exception as e:
        return e

print(hamming_distance("abcde","bcdef"))
print(hamming_distance("abcde","abcde"))
print(hamming_distance("strong","strung"))