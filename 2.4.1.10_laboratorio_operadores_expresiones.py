"""
Escenario
Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión:

3x3 - 2x2 + 3x - 1

El resultado debe ser asignado a y.

Entrada de Muestra

x = 0
x = 1
x = -1

Salida Esperada

y = -1.0
y = 3.0
y = -9.0

"""
x = -1 # codifica aquí tus datos de prueba
x = float(x)
# escribe tu código aquí
y=3*(x**3)-2*(x**2)+(3*x)-1
print("y =", y)
