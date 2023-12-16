#¡Bienvenidos sean todos los que van a probar mi primer juego!
#Hoy, aprendiendo a codificar en Pyhton.
#Mañana si Dios quiere, conquistando al mundo.
#Ya revise, conquistar al mundo, va a demorar mas de lo previsto. Con el anterior codigo, todo se estaba complicando mucho
#Asi que hice uno nuevo e incluso mas simple porque ni yo estaba entendiendo que estaba haciendo.

a = "¡Bienvenido a mi juego de piedra papel o tijeras!3"
b = "\nEn este juego gana el mejor de tres intentos."
c = '\nSi empatas dos veces ya pierdes automáticamente, ojito ahí.'
d = '\nDe resto, puedes disfrutar con tranquilidad ;)'

print (a + b + c + d)

#Estas son las variables para comenzar con el juego
1 == 'Piedra'
2 == 'Papel'
3 == 'Tijera'

#Con este comando, espero a que la computadora genere una respuesta aleatoria
import random
random.choice(f"{1}'Piedra',{2}'Papel',{3}Tijeras")

a= random.choice

#Aqui intento crear la repeticion del programa, solo tres veces hasta lograr la victoria

while True:

#Ahora, el jugador deberá escoger alguna opción para continuar
    jugada_usuario = input(f'Ingresa "{1} para Piedra", "{2} para Papel" o "{3} para Tijera" para continuar: ')

#Aqui lo que intento hacer es que el sistema muestre que opcion esta escogiendo la pc
    if a == 1:
     print("Computadora selecciona Piedra")
    elif a == 2:
     print("Computadora selecciona Papel")
    else:
     a == 3
     print("Computadora escoge Tijeras")

    
#Ahora comparamos la jugada contra la computadora

    if (a == {1} == jugada_usuario == {1}):
     print("Empate")
     continue
    elif (a == {1} > jugada_usuario == {3}):
     print("Piedra le gana a tijeras. La máquina gana")
     continue
    elif (a == {1} < jugada_usuario == {2}):
     print("Papel le gana a piedra. Ganaste")
     continue
    elif (a == {2} == jugada_usuario == {2}):
     print("Empate")
     continue
    elif (a == {2} < jugada_usuario == {3}):
     print("Tijeras le gana al papel. La máquina gana.")
     continue
    elif (a == {2} > jugada_usuario == {1}):
     print("Papel le gana a la piedra. Ganaste")
     continue
    elif (a == {3} == jugada_usuario == {3}):
       print("Empate")
       continue
    elif (a == {3} > jugada_usuario == {2}):
      print("Tijera le gana a papel. La máquina gana.")
      continue
    else:
        (a == {3} < jugada_usuario == {1})
        print("Piedra le gana a tijeras. Ganaste")
        break

#Despues de cambiar el tipo de random me sigue saliendo la falla de que la computadora siempre escoge tijeras, independientemente de la seleccion del jugador, siempre lo coloca como empate.
#Ayuda diosito, ya no quiero ser tu mejor guerrera