import random

def play():
    num_sec = random.randint(1, 100)
    intentos = 0

    print("¡bienvenido al juego de adivinanzas de números!\n"
    'Estoy pensando en un número entre 1 y 100.\n'
    'Tienes 5 posibilidades de adivinar el número correcto.elige tu dificultad: \n 1.facil \n 2.medio \n dificil ")


    print("adivina el numero secreto entre el 1 y 100: ")

    while True:
        guess = int(input("Numero: "))
        intentos += 1

        if guess < num_sec:
            print("Demasiado Bajo. ")

        elif guess > num_sec:
            print("Demasiado Alto.")

        else
            print("felicidades, has hecho ", intentos, " intentos")
            break

play()
