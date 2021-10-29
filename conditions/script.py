x = 20
print(x == 2)
print(x == 20)
print(x > 5)

if x > 5:
    print("%d is greater than 5 ✅" % x)

x = 100
options = [1, 10, 40, 100]

if x in options:
    print("%d is on of the options is %s" % (x, options))

if 555 in options:
    print("Not happening.")
elif 22222 in options:
    print("Also not happening")
else:
    print("Reached else statement.")


x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("Lists are equivalent %s" % (x == y))
print("Lists are the same %s" % (x is y))
print("X list is same as Z %s" % (x is z))

value = True
print("value = %s" % value)
print("!value = %s" % (not value))

