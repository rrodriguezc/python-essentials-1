"""
Escenario
Millas y kilómetros son unidades de longitud o distancia.

Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

Millas a kilómetros.
Kilómetros a millas.
No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu programa con los datos que han sido provistos en el código fuente.
"""


miles = 7.38
kilometers = 12.25


miles_to_kilometers = (miles*1.61)/1 ### regla de 3
kilometers_to_miles = (kilometers*1)/1.61 ### regla de 3

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
