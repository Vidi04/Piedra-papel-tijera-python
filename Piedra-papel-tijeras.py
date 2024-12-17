#se puede colocar el nombre en la segunda solicitud
#lo ingresado por el usuario sea lowercase
# Mas de un turno con while



Nombre1= input("¿como te llamas jugador 1?: ")
Nombre2= input("¿como te llamas jugador 2?: ")




intentos=0
maximo=3

while intentos<maximo:
    Jugador1 = input(f"¡hola {Nombre1}! ¿que eliges? ¿piedra,papel o tijeras?:")
    Jugador2 = input(f"¡hola {Nombre2}! ¿que eliges? ¿piedra,papel o tijeras?: ")
    jugador1 = Jugador1.lower()
    jugador2 = Jugador2.lower()
    
    condicion1= jugador1=="piedra" and jugador2 =="tijeras"
    condicion2= jugador1=="papel" and jugador2 == "piedra"
    condicion3= jugador1=="tijeras" and jugador2=="papel"

    if jugador1 == jugador2:
        print("¡ha sido un empate!")
    elif (condicion1) or (condicion2) or (condicion3):
        print("ha ganado: ",Nombre1)
    else:
        print("ha ganado: ",Nombre2)
    intentos+=1