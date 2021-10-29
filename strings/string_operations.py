string1 = "Hello world"
string2 = 'Hello world'
string3 = "Hello world, 'mate'"
print(string1)
print(string2)
print(string3)
print("string3 has %d characters." % len(string3))
print("string3 has %d 'l' characters." % string3.count("l"))
print(string3[1:5])
print("All characters after the first: %s" % string3[1:])
print(string3[-5:-1])
print(string3[::-1])
print(string3[::-2])
print(string3.upper())
print(string3.lower())
print("Starts with Hello: %s" % string3.startswith('Hello'))
print("Ends with 'mate': %s" % string3.endswith("'mate'"))
print("Split result: %s" % string3.split(' '))