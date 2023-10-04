# -*- coding: utf-8 -*-
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'python',
    'angular',
    'javascript',
    'nodejs',
    'android',
    'ionic',
    'php',
    'css',
    'html',
    'git',
    'gitlab',
    'devops'
]

#Función para elegir una palabra aleatoria de la lista WORDS
def random_word():
    # idx guarda un indice aleatorio y se
    # retorna la palabra según el indice
    idx = random.randint(0, len(WORDS)-1)
    return WORDS[idx]

#Función que muestra las imagenes según los intentos fallidos
def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('------------------------')

def run():
    #word contiene la palabra aleatoria
    word = random_word()
    # Mostrar el tablero con la palabra escondida
    hidden_word = ['-'] * len(word)
    #tries almacena el número de intentos
    tries = 0

    #Todo el tiempo muestra el tablero
    while True:
        display_board(hidden_word, tries)
        #current_letter almacena la letra ingresada por el usuario
        current_letter = str(input('Escoge una letra: '))

        # se verifica que la letra ingresada este en la palabra
        # de ser así se guarda en la letter_indexes
        letter_indexes =  []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        #Si la lista esta vacia, se suman los intentos
        # de lo contrario se reemplaza y muestra la letra
        if len(letter_indexes) == 0:
            tries += 1

            #Saber si se perdió
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste! La palabra correcta era: {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            #Se reinicia la palabra
            letter_indexes = []

            #Saber si ganaste al no tener mas -
            try:
                hidden_word.index('-')
            except ValueError:
                print('')
                print('Felicidades! Ganaste. La palabra es: {}'.format(word))
                break



if __name__ == '__main__':
    print('B I E N V E N I D O S  A L  A H O R C A D O')
    #Ejecutamos la función run
    run()