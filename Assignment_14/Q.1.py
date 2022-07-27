'''
Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.
'''

class gen_class(object):
    def __init__(self,n):
        self.n = n
    def gen(self):
        for i in range(0,self.n):
            if i%7==0:
                yield i
    
for x in gen_class(100).gen():
    print(x)


