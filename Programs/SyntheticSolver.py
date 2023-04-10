#Synthetic Equation Solver
cube = input("Write your (Cube) value:")
square = input("Write your (Square) value:")
linear = input("Write your (Linear) value:")
constant = input("Write your (Constant) value:")

try:
    cube = int(cube)
    square = int(square)
    linear = int(linear)
    constant = int(constant)

except:
    print("Are you dumb? You can't even write a number!")
    quit()

print('Your Equation:')
print(str(cube) + "x^3", "+",str(square) + "x^2", "+",str(linear) + "x", "+", str(constant))
x = input("Enter your possible zero:")

print(x)

BringDownNum = (int(cube) * int(x)) + (int(square))

print("First Part:", BringDownNum)

BringDownNum = (int(BringDownNum) * int(x)) + (int(linear))

print("Second Part:", BringDownNum)

BringDownNum = (int(BringDownNum) * int(x)) + (int(constant))

print("Third Part:", BringDownNum)

if (BringDownNum == 0):
    print("Alright, nice! You found a possible zero!")
else:
    print("This is not a possible zero, sorry.")
    quit()




