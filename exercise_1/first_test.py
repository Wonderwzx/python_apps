# name = input("Enter your name: ")
# print(name)


# print("abcifjojfafj"[1:10:2])

# print(type("a") == str)
# print(isinstance("abd", str))

# phone_numbers = {"zw":"607", "ly":"188"}
# for pair in phone_numbers.items():
#     print("{} has phone number {}".format(pair[0], pair[1]))

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for key, value in phone_numbers.items():
#     print("%s: %s"%(key, value))

# for value in phone_numbers.values(): # .keys()
#     print("------" + value.replace("9", "00000"))

# def foo(name):
#     return "Hi %s" %name
# print(foo("wzx"))

# for letter in 'abc':
#     print(letter.upper())
#     print(letter.capitalize())
# print("abc".capitalize())

# print("****".join(["aa", "bb", "cc"]))

# ques = ("what","why","where")
# print("where are you".startswith(ques))


# def foo(lst):
#     return [i for i in lst if isinstance(i, int)]

# temp = [100, 120, 140, 150]

# new_temp = [t / 10 for t in temp]
# print(new_temp)


# temps = [1,2,3,4,5,6,7]
# new_temp = [temp / 10 if temp != 7 else 0 for temp in temps]
# print(new_temp)

# def foo(lst):
#     return [s if isinstance(s, int) else 0 for s in lst]

# def foo(lst):
#     return sum([float(i) for i in lst])

# def sub(a, b):
#     return a - b
# print(sub(b=4, a=3))

# def area(a, b=5):
#     return a/b
# print(area(6))
# print(area(b=6,a=7))

# def add(*args):
#     return sum(args)/len(args)
# print(add(1,2,3,4))

# def join(args):
#     return ""+args
# print(join("1"))

# def foo(*args):
#     args = [a.upper() for a in args]
#     return sorted(args)#sort the list

# Indefinite number of keyword arguments 
# def getDict(**kwargs):
#     return kwargs
# print(getDict(a=1,b=2))

# import collections
# words = ["dic", "pre", "end", "dic"]
# word_count = collections.Counter(words)
# print(word_count["dic"])

# s = "abc"
# a = 1
# print("ac" + 1)

ans = float("inf"), None, None


