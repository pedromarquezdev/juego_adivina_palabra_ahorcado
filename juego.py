import random

def obtener_palabra_secreta():
    palabras = ['Canuto','Cornamenta','Lunatico','Colagusano','Siempre']
    return random.choice(palabras)



def mostrar_letras_en_palabras(palabraSecreta, letrasAdivinadas):
    palabra_adivinada = ''
    
    for letra in palabraSecreta:
        if letra in letrasAdivinadas:
            palabra_adivinada += letra
        else:
            palabra_adivinada += '_ '
    return palabra_adivinada 



def juego_adivina_la_palabra():
    juego_terminado = False
    palabra_secreta = obtener_palabra_secreta().lower()
    letras_adivinadas = []
    intentos = 7
    
    print("Bienvenido al 'Adivina la palabra'.")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta.")
    print(mostrar_letras_en_palabras(palabra_secreta, letras_adivinadas))
        
    
    while not juego_terminado and intentos > 0:
        letra_ingresada = input(f"Ingresa la letra de la palabra:").lower()
        
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("Por favor introduzca una letra válida(escribir sólo una letra).")
        elif letra_ingresada in letras_adivinadas:
            print("Ya has ingresado esa letra, prueba con otra.")
        else:
            letras_adivinadas.append(letra_ingresada)
            
            if letra_ingresada in palabra_secreta:
                print(f"¡Correcto, la letra ingresada {letra_ingresada} está en la palabra secreta!")
            else:
                intentos-= 1
                print(f"La letra ingresada no está en la palabra secreta.")
                print(f"Te quedan {intentos} intentos.")
        progreso_actual = mostrar_letras_en_palabras(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        
        if '_ ' not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print("¡Felicitaciones has ganado!")
            print(f"La palabra completa es: {palabra_secreta}.")
        
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print("Has perdido, se te han acabado los intentos")
        print(f"La palabra secreta era: {palabra_secreta}.")
    

juego_adivina_la_palabra()


















