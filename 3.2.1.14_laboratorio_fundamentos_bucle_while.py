blocks = int(input("Ingresa el número de bloques: "))

altura = 0
capa = 1
while capa <= blocks:
    altura += 1
    blocks -= capa
    capa += 1

print("La altura de la pirámide:", altura)

