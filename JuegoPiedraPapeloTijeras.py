#¡Bienvenidos sean todos los que van a probar mi primer juego!
#Hoy, aprendiendo a codificar en Pyhton.
#Mañana si Dios quiere, conquistando al mundo.
#O por lo menos intentandolo, disfruta
#Y perdona cualquier error, estoy aprendiendo c:

a = "¡Bienvenido a mi juego de piedra papel o tijeras! "
b = "En este juego gana el mejor de tres intentos."
c = '\nSi empatas dos veces ya pierdes automáticamente, ojito ahí.\nRecuerda escribir todo con la primera letra en mayusculas.'
d = '\nDe resto, puedes disfrutar con tranquilidad ;)'

print (a + b + c + d)

#Estas son las variables para comenzar con el juego
valor1 = 'Piedra'
valor2 = 'Papel'
valor3 = 'Tijera'

import random

#Con este comando, espero a que la computadora genere una respuesta aleatoria
respuesta_automatica = random.randint(valor1,valor2,valor3)

#Ahora, el jugador deberá escoger alguna opción para continuar
a = str(input('Ingresa "Piedra", "Papel" o "Tijera" para continuar: '))

if respuesta_automatica == jugador:
    print("empate")






