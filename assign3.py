# 1
numbers = [1, 2, 3, 4, 5, 1, 4, 5]
print(sum(numbers))

# 2


def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

# 3


list1 = [10, 20, 4, 45, 99]

print(max(list1))


# 4
list1 = [10, 20, 4, 45, 99]

print(min(list1))

# 5


def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

# 6


def last(n): return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)


# 7
lst = ['foo.py', 'bar.py', 'baz.py', 'qux.py', Ellipsis]
s = set(lst)
# sets contain unique items only

# 8

lst = []
if len(lst):
    print("empty")
else:
    print("nope")

# 9

old_list = [1, 2, 3]
new_list = old_list


print('New List:', new_list)
print('Old List:', old_list)

# 10


def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
