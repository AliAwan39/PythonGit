# n1 = input("enter first nunmber! ")
# n2 = input("\n enter second number! ")
# sum = int(n1) + int(n2)

# print("\n")
# print("the sum of number is: " , sum)

# for i in range(0,10 ,10) :
#     print("hello: ", i)

# i=1
# while(i<=10) :
#     print("hello: ",i)
#     i = i+1
#import datetime

#print(datetime.datetime.now())
#names = ["ali", "hassan", "ahmad", "ahsan"]

#for  i in names:
#print("Name: ", i)

fact = int(input("Enter a number to find Factorial: "))
if(fact > 1):
    for i in range(1,fact):
        fact *=i
    print("Factorial is : ", fact)
else:
    print("can't find a factorial of number: ", fact)
