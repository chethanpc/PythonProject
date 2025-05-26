# Calculate Factorial Using Recursive Function

n = int(input('Enter a number: '))
def factorial(n):
    if (n < 0):
        return 'Invalid Argument'
    elif (n == 0 or n == 1):
        return 1
    else:
        return n * (factorial(n - 1))

result = factorial(n)
print('Factorial of', n, 'is:', result)