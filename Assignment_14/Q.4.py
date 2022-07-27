
'''Question 4:
Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].
'''

sub = ['I','You']
verb = ['Play', 'Love']
object = ['Hockey', 'Football']
for i in range(len(sub)):
    for j in range(len(verb)):
        for k in range(len(object)):
            print(sub[i],verb[j],object[k])
