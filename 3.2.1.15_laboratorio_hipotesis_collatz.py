c0 = int(input("Ingresa c0: "))

if c0 > 1:
	count = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		count += 1
	print("pasos =",count)
else:
	print("Valor de c0 incorrecto")
