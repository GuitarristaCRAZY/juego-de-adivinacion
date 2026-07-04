import random

def intro():
    print("¡bienvenido al juego de adivinanzas de números!\nEstoy pensando en un número entre 1 y 100.\nTienes dependiendo de la dificultad ciertas oportunidades de adivinar el número correcto.\n")
    
    while True:
        dificultad = int(input("Elige tu dificultad:\n1.facil (10 oportunidades)\n2.medio (5 posibilidades)\n3.dificil (3 oportunidades) \n\n"))
        if dificultad == 1:
            return 10
        elif dificultad == 2:
            return 5
        elif dificultad == 3:
            return 3
        else:
            print("Esa dificultad no existe, elige una dificultad entre el 1 y 3.")
        
    


def play():
    while True:
        num_sec = random.randint(1, 100)
        max_intentos = intro()
        intentos = 0

        print("adivina el numero secreto entre el 1 y 100: ")
        print(f"\n Tienes {max_intentos} intentos para adivinar")

        while intentos < max_intentos:
            try:
                guess = int(input(f"Intento {intentos + 1}/{max_intentos} - Introduce tu número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
                
            intentos += 1

            if guess < num_sec:
                print("Demasiado bajo.")
            elif guess > num_sec:
                print("Demasiado alto.")
            else:
                print(f"¡Felicidades! Has adivinado en {intentos} intentos.")
                return # Termina la función al ganar

        print(f"\n¡Se te han acabado los intentos! El número era: {num_sec}")

        Reintento = input("Quieres volver a intentar? (S/N)\n").upper()
        if Reintento != "S":
            print("¡Gracias por jugar! Adiós.")
            break


# Iniciar el juego
if __name__ == "__main__":
    play()
