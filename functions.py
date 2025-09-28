num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))

def average(num1,num2,num3):
    return (num1+num2+num3)/3

print(average(num1,num2,num3))    

#print length of a list
list =[1,2,3,4,5,6,7,8,9,10]
def listLength(list):
    print(len(list))

listLength(list)    

def printList(list):
    for el in list:
        print(el,end=" ")
printList(list)    


#factorial of a nummber

def findFactorial(factNumb):
    answer=1
    for num in range(factNumb,0,-1):
        answer*=num
    return answer    

print(findFactorial(int(input("enter a number to find its factorial"))))


#convert USD to INR
def currrecnyConvertor(money):
    return money*80
print("The INR value for the current USD is ",currrecnyConvertor(20))  


#check whether the following number is odd or even
def oddOrEven(numb):
    if(numb%2!=0):
        return "ODD"
    else:
        return "EVEN"
print(oddOrEven(2))         
