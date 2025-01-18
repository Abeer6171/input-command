print("1-Add")
print("2-Substraction")
print("3-Multiply")
print("4-Divide")
option=int(input("Choose an operation: "))
if(option in [1,2,3,4]): 
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1/num2
    print(f"The result of the operation is: {result}")
else:
    print("invalid option entered")
    print("Thanks a lot for seeing my project")