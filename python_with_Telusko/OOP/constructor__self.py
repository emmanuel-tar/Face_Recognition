class Computer():
    
    def __init__(self) -> None:
        self.name = "Emmanuel"
        self.age = 32
        

        
        
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age=12
c2 = Computer()

if c1.compare(c2):
    print("They are same")
    
else:
    print("They are Different")




print(c1.name)
print(c2.age)