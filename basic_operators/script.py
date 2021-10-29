number = 1 + 2 * 3 / 4
print("Should be 2.5. Value: %f" % number)

remainder = 7 % 2
print("Should be 1. Value: %f" %remainder)

two_squared = 2 ** 2
print("Should be 4. Value: %f" % two_squared)

list1 = [1, 2, 3]
list2 = ["hello", 4]
total_list = list1 + list2
print("Both lists", total_list)

seed_list = [1, 2, 3]
print("List with duplicates", seed_list * 2)

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))

if x_list.count(x) == 10 and y_list.count(y) == 10 and big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Done ✔")