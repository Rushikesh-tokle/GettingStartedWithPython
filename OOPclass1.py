# class Car:
#     color="blue"
#     model="mercedes"
# car1=Car()
# print(car1.color)    

# class Student:
    
#     def __init__(self,fullName):
#         self.name=fullName
#         # print(self)
#         print("hello this is constructor ", self.name)

#     def printName(self):
#         print("tthe name is bond ",self.name)


# st1=Student("rushikesh") 
# st2=Student("rushi") 
# st1.printName()


class Student:
    def __init__(self,name,math,phy,chem):
        self.math_marks=math
        self.phy_marks=phy
        self.chem_marks=chem
    def printAverage(self):
        print("the average of the marks is ",(self.math_marks+self.phy_marks+self.chem_marks)/3)  
    @staticmethod
    def hello():
        print("hello Everyone")    
st1=Student("Rushi",20,30,40)      
st1.printAverage()
st1.hello()    