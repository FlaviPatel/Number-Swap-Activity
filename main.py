# Take input from user
# We have to Typecast the input as input will return value as string
x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
print("Value of x before swapping:", x)
print("Value of y before swapping:", y)

# Swappinh
temp = x
x = y
y = temp

print("Value of x after swapping:", x)
print("Value of y after swapping:", y)
