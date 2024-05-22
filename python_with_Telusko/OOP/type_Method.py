#Type of Method, Instance ,Class and  Static Method

class Student:

    school = 'Telusko'
    def __init__(self,m1,m2,m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3/3)
#get the value of m1
    def getM1(self):
        return self.m1
#set the value of m1
    def set_m1(self,value):
        self.m1 = value
        
    
        
    @classmethod
    def getSchool(cls):
            return cls.school
        
    @staticmethod 
    def info():
        print("This is Student Class... in abc Module")


s1 = Student(54,87,12)
s2 = Student(74,81,32)


print(s1.avg())
print(s2.avg())
print(Student.getSchool())

Student.info()
