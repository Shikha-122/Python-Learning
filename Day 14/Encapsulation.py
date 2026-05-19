#Example 1:

class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0

    #getter method
    def get_marks(self):
        return self.__marks

    #setter method
    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks

        else:
            print('Invalid marks . Marks must be <=100')

stu=Student('John')
stu.set_marks(190)
print(stu.get_marks())