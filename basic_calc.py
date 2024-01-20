'''Script tittle: Basic calculator v1
Developer name: Jorge Camilo
Date: 18-01-2024c'''

'''Description: 
This calculator let you get the result of basic math operations
from two numbers (Variables)
'''

#INPUTS (two static variables)
num1 = 20
num2 = 5

#PROCESS
add = num1 + num2 
sub = num1 - num2
mul = num1 * num2 
div = num1 / num2 

#OUTPUTS
print(":::Basic Calculator V1.0:::")
print("number 1:", num1, type(num1))
print("number 2:", num2, type(num2))
print("The addition is ",add )
print("The subtraction is ",sub)
print("The multiplication is ",mul)
print("The divison is ",div)
print("\n")
print(":::Basic Calculator V1.1:::")
print("number 1:", num1)
print("number 2:", num2)
print("The addition is ",num1 + num2)
print("The subtraction is ",num1 - num2)    
print("The multiplication is ",num1 * num2)
print("The divison is ",num1 / num2)