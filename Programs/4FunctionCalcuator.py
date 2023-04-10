#Simple 4 Function Calculator
 
ops = "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division"
print(ops)
operation = input("Enter the operation you want to perform: ")

try:
    operation != int(operation)
except:
    print("Please enter a number.")
    quit()

if (int(operation) >= 5):
    print("Please enter a number between 1 and 4.")
    quit()

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 != int(num1)
    num2 != int(num2)
except:
    print("You are an idiot. Goodbye")
    quit()

if (int(operation) == 1):
    anwser = str(num1) + str(num2)
elif (int(operation) == 2):
    anwser = int(num1) - int(num2)
elif (int(operation) == 3):
    anwser = int(num1) * int(num2)
elif (int(operation) == 3):
    anwser = (num1) / (num2)

print("Do mental math. Your brain is a size of a pea\nHere's your anwser anyways:")
print(anwser)



