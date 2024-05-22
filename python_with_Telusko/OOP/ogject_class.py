
class Computer:

    def __init__(self,cpu,ram) :
        self.cup=cpu
        self.ram = ram


    def config(self):
        print("Config is: ",self.cup,self.ram)


com1 = Computer('i5,',16)
com2 = Computer('Ryan 3',8)

#Computer.config(com1)
#Computer.config(com2)

com1.config()
com2.config()



