my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list = []

for numero in my_list:
	if numero not in list:
		list.append(numero)
my_list = list[:]

print("La lista con elementos únicos:")
print(my_list)