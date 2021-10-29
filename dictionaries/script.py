phonebook = {}
phonebook["John"] = "+44000001"
phonebook["Mary"] = "+44000002"

print(phonebook)

phonebook = {
    "John": "+44000001",
    "Theresa": "+44000003",
    "Mistaken": "+44000003",
}

print(phonebook)

del phonebook["Mistaken"]

for name, number in phonebook.items():
    print("%s: %s" % (name, number))

if not ("Arnold" in phonebook):
    print("Confirmed Arnold is not in the phonebook.")

if "Theresa" in phonebook:
    print("Confirmed Theresa is in the phonebook.")