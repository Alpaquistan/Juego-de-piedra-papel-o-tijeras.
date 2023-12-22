#Por recomendación de una compañera, coloco este comando hasta arriba.
import random

#Aunque me emociona mucho aprender a programar, la verdad es que esta complicado de lo que pensé y me ha hecho llorar varias veces.
#Pero como bien dicen por ahí "Confía en el proceso" y en internet, porque todo lo que no entendí, lo inventigué y bendito sea el que creó Internet y quienes comparten sus conocimientos en el mismo
a = "En un mundo donde la humanidad y las máquinas se pelean por el dominio del mundo, te tocará a tí jugador, salvarnos a todos"
b = "\nEste es un juego super extremo ya que tienes solo una oportunidad para ganar."
c = '\n¡Bienvenido a mi juego de piedra papel o tijeras!'
print (a + b + c)

#Aqui el jugador debe seleccionar una opción
ju = input('Escoge sabiamente tu arma, presionando "1" para Piedra, "2" para Papel o "3" para Tijera: ')

#Por recomendacion del prof. Ivan, utilice el random.choice pero para que funcionara correctamente, le agregue una lista
list=['1','2','3']
pc=random.choice (list)

#Estas son las opciones del jugador, nuestro heroe
if ju == "1":
     print("Has decidido entrar a esta batalla con tu arma, una 'Piedra;")
elif ju == '2':
     print("Has decidido entrar a esta batalla con tu arma, un 'Papel'")
elif ju == '3':
     print("Has decidido entrar a esta batalla con tu arma, un par de 'Tijeras'")
else:
     print("Así que has escogido el camino de la muerte")

#Estas son las opciones de la malvada computadora
if pc == '1':
     print("Computadora malvada escoge Piedra")
elif pc == '2':
     print("Computadora malvada escoge Papel")
else:
     pc == '3'
     print("Computadora malvada escoge Tijeras")

#Estos son los resultados de la interminable batalla entre la humanidad y las maquinas (Esta parte la simplifique porque me dijeron en el foro que estaba muy extenso)

if (ju == '1' and pc == '1') or (ju == '2' and pc == '2') or (ju == '3' and pc == '3'):
     print("Empate. Nadie ha ganado en esta batalla.\n¿Acaso podremos acabar algún día con esta tragedia?")
elif (ju == '1' and pc == '3') or (ju == '2' and pc == '1') or (ju == '3' and pc == '2'):
     print("Jugador gana contra la malvada computadora. La victoria, finalmente es nuestra.")
else:
     print("Oh no, ha ganado la malvada computadora. Ya no hay esperanza para la humanidad.")

#Honestamente, pensé que no lo lograría porque tengo la mala costumbre de complicar todo y luego no entender nada pero gracias a la guía de mis compañeros en el foro, a las guías del prof. Iván y del Internet (Bendito sea el internet), pude sacar adelante este proyecto
#Queria agregar más cosas pero entiendanme, todo lo que sé de programación lo acabo de aprender de esta clase; estoy en horarios extendidos en el trabajo por navidad y estuve 4 días sin internet en casas y 3 sin luz; estoy chiquita.
#Pero ya se la saben, hoy chillando por no entender, mañana hackeando bancos como una crack
#Queria dar la opcion de tres intentos, pero el while no me esta funcionando correctamente, asi que lo hago manual
ju = input('Tienes una segunda oportunidad.\nEscoge sabiamente tu arma, presionando "1" para Piedra, "2" para Papel o "3" para Tijera: ')

list=['1','2','3']
pc=random.choice (list)

if ju == "1":
     print("Has decidido entrar a esta batalla con tu arma, una 'Piedra;")
elif ju == '2':
     print("Has decidido entrar a esta batalla con tu arma, un 'Papel'")
elif ju == '3':
     print("Has decidido entrar a esta batalla con tu arma, un par de 'Tijeras'")
else:
     print("Así que has escogido el camino de la muerte")

if pc == '1':
     print("Computadora malvada escoge Piedra")
elif pc == '2':
     print("Computadora malvada escoge Papel")
else:
     pc == '3'
     print("Computadora malvada escoge Tijeras")


if (ju == '1' and pc == '1') or (ju == '2' and pc == '2') or (ju == '3' and pc == '3'):
     print("Empate. Nadie ha ganado en esta batalla.\n¿Acaso podremos acabar algún día con esta tragedia?")
elif (ju == '1' and pc == '3') or (ju == '2' and pc == '1') or (ju == '3' and pc == '2'):
     print("Jugador gana contra la malvada computadora. La victoria, finalmente es nuestra.")
else:
     print("Oh no, ha ganado la malvada computadora. Ya no hay esperanza para la humanidad.")
     
ju = input('Tercer y ultimo intento. \nEscoge sabiamente tu arma, presionando "1" para Piedra, "2" para Papel o "3" para Tijera: ')

list=['1','2','3']
pc=random.choice (list)

if ju == "1":
     print("Has decidido entrar a esta batalla con tu arma, una 'Piedra;")
elif ju == '2':
     print("Has decidido entrar a esta batalla con tu arma, un 'Papel'")
elif ju == '3':
     print("Has decidido entrar a esta batalla con tu arma, un par de 'Tijeras'")
else:
     print("Así que has escogido el camino de la muerte")

if pc == '1':
     print("Computadora malvada escoge Piedra")
elif pc == '2':
     print("Computadora malvada escoge Papel")
else:
     pc == '3'
     print("Computadora malvada escoge Tijeras")


if (ju == '1' and pc == '1') or (ju == '2' and pc == '2') or (ju == '3' and pc == '3'):
     print("Empate. Nadie ha ganado en esta batalla.\n¿Acaso podremos acabar algún día con esta tragedia?")
elif (ju == '1' and pc == '3') or (ju == '2' and pc == '1') or (ju == '3' and pc == '2'):
     print("Jugador gana contra la malvada computadora. La victoria, finalmente es nuestra.")
else:
     print("Oh no, ha ganado la malvada computadora. Ya no hay esperanza para la humanidad.")