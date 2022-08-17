myfile = open("fruits.txt")
print(myfile.read())
content = myfile.read()
myfile.close()
# if read the file now there will be error
# print(myfile.read())

with open("fruits.txt") as myfile:
    content = myfile.read()#close the file after the block

with open("vegetables.txt", "w") as myfile2: #if vegetables.txt already exists, this func will overwrite the file
    myfile2.write("beans")
    myfile2.write("tomato\npotato\ncabbage")

print("--------------------")
file = open("vegetables.txt")
content = file.read()
file.close()
print(content[:15])

print("--------------------")
def foo(character, filepath = "fruits.txt"):
    file = open(filepath)
    return file.read().count(character)

print("--------------------")
with open("fruits.txt") as file1:
    content = file1.read()

with open("first.txt", "w") as file2:
    file2.write(content[:20])

print("--------------------")
with open("fruits.txt", "a") as file3:
    file3.write("\nmango")

print("--------------------")
with open("fruits.txt", "a+") as file4:
    file4.write("\norange")
    file4.seek(0)
    content = file4.read()

print(content)

print("--------------------")
with open("first.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write("\n" + content)
    file.write("\n" + content)