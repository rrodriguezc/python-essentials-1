"""
Escenario
La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.
"""

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

# sumamos la hora inicial con las horas adicionales
hour_final=hour+(mins+dura)//60
# obtenemos la hora final con el mod 24
hour_final=hour_final%24

#sumamos los minutos para obtener los minutos restantes finales
mins_final=(mins+dura)%60

print(hour_final,mins_final,sep=":")
