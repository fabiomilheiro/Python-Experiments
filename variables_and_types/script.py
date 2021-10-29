x = 1000
y = 3.14
print(x)
print(y)
print(float(7))

name = 'John Smith'
print(name)
name = "John Smith's jacket"
print(name)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
hello_word = hello + " " + world
print(hello_word)

a, b = 3, 4
print(a, b, "something else")

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)