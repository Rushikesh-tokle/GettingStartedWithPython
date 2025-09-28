#print backwards
def printBackwards(num):
    if(num==1):
        print(num)
        return
    print(num)
    printBackwards(num-1)
printBackwards(5) 


#iterate backwards and print forwards
def printForwards(num):
    if(num==1):
        print(num)
        return
    printForwards(num-1)
    print(num)
printForwards(5)        



#print factorial
def printFactorials(num):
    if(num==1):
        return num
    return num*printFactorials(num-1)
print(printFactorials(4))    


#sum of n natural numbers
def sumOfNatural(num):
    sum=0
    if(num==1):
        sum+= num
        return sum
    
    sum=num+sumOfNatural(num-1)
    return sum
print(sumOfNatural(2))


list=[1,2,3,4,5,6]
def printList(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    printList(list,idx+1)
printList(list,0)    
