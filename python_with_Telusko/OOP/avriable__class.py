class Car:
    wheels = 4
    def __init__(self) -> None:
        self.mil = 10
        self.com = 'BMW'
        

c1 = Car()
c2 = Car()

Car.wheels = 5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)