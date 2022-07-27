"""

Question 3:

Define a class Person and its two child classes: Male and Female. All classes have a
method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
class.
"""

class Person:
    def getGender(self):
        return "person"
class Male(Person):
    def getGender(self):
        return "Male"
class Female(Person):
    def  getGender(self):
        return  "Female"
obj_male = Male()
obj_female = Female()
print(obj_male.getGender())
print(obj_female.getGender())
