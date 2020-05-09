
import math
# 1


def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(3, 6, -5))

# 2
print(sum(lis))

# 3
print(math.prod(lis))

# 4
txt = "Hello World"[::-1]
print(txt)

# 5
print(math.factorial(5))

# 6


def count(list1, l, r):
    return len(list(x for x in list1 if l <= x <= r))


list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
l = 40
r = 80
print count(list1, l, r)

# 7


def up_low(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print("No. of Upper case characters : %s,No. of Lower case characters : %s" % (u, l))


up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

# 8


def unique(list1):

    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        print x,


list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)

# 9

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

# 10

even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos)
