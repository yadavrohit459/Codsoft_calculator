print("select an operation to perfom:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")


opeation =int(input())

if opeation == 1:
    num1= input("Enter the first number:")
    num2= input("Enter the second number:")
    print("The sum is " +str( eval(num1) +eval(num2)))
     
elif opeation == 2:
    num1= input("Enter the first number:")
    num2= input("Enter the second number:")
    print("The subtract is " + str(eval(num1) + eval(num2)))
    
    
elif opeation == 3:
    num1= input("Enter the first number:")
    num2= input("Enter the second number:")
    print("The multiplay is " + str(eval(num1) * eval(num2)))
    
    #code for division
elif opeation == 4:
    num1= input("Enter the first number:")
    num2= input("Enter the second number:")
    print("The divide is " + str(eval(num1) / eval(num2)))
    
    
    
    #code for muliply
else:
    print("Invalid Entry")
                   

