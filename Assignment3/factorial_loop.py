# Calculate Factorial using for Loop

n1 = int(input('Enter a number: '))

fact = 1

if (n1 < 0):
    fact = "Invalid Argument"
elif (n1 == 0 or n1 == 1):
    fact = 1
else:
    for i in range(1, n1 + 1, 1):
        fact = fact * i


print('Factorial of', n1, 'is:', fact)
