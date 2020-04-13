# 1

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

print(num1+num2)

# 2


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact


num = 5
print("Factorial of", num, "is",
      factorial(num))

# 3
P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
print((P * N * R)/100)

# 4


def compound_interest(principle, rate, time):

    CI = principle * (pow((1 + rate / 100), time))
    print("Compound interest is", CI)


compound_interest(10000, 10.25, 5)

# 5


def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp/10

    return (sum1 == x)


print(isArmstrong(x))

# 6

r = int(input())
print((22/7)*r*r)


# 7

start = 11
end = 25

for val in range(start, end + 1):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)

# 8

num = 11

if num > 1:

    for i in range(2, num//2):

        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")

# 9

FibArray = [0, 1]


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib


print(fibonacci(9))

# 10


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

# 11


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib


# 12
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

# 13


c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# 14

n = int(input())

print((n*(n+1)*(2*n + 1))/6)

# 15

n = int(input())
print(((n(n+1))/2)**2)
