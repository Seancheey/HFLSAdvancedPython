# List Comprehension

# [0 - 1024]
list_a = []
for i in range(10):
	list_a.append(2 ** i)

print(list_a)

list_b = [2 ** i for i in range(10)]

print(list_b)

# [0 - 1024]

list_c = [2 ** i for i in range(10) if i % 2 == 1]

print(list_c)

str_a = "ABC"
str_b = "XYZ"

print([y + x for y in str_a for x in str_b])

