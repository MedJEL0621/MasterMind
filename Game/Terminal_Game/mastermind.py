#!/usr/bin/python3
from array import array
import os
import sys
import random
import tkinter

from matplotlib import use
from colors import bcol
from user import User
from banner import banner


#print("tu color es :  {}".format(random.choice(colors)))

# Define color array
colors = ['Red','Green', 'Blue', 'Orange','Purple', 'Pink', 'Gold', 'Violet', 'Coffe', 'black', 'white']

dificults = ['', 'Easy', 'Medium', 'Hard', ]

top_10_user = []


def create_user():
    """ Esta funcion servira para crear un nombre de usuario"""
    print('\n[*] Primero Crearemos un usuario\n')
    
    new_user = User()
    new_user.nickname = input('Ingresa el nombre de usuario: ')
    return new_user

def mode():
    """ Esta funcion servira para determinar el modo de juego 
        Modes
            1 - Solo
            2 - Multiplayer
    """
    print("Selecciona el modo de juego")

def question_code(user):
    """esta es la funcion que se encarga de testear si el usuario
    Ingresa el codigo correcto
    """
    pass

def bucle_dificult(size):
    """ Esta funcion se encarga de crear el arreglo de los colores 
    y los metodos dentro"""
    codigo_colores = []

    def generate_array_dificult(size):
        '''genera el arreglo de colores segun el nivel de dificultad'''
        array_for_dificult = []
        if size == 4:
            size_array_dificult = size + 3
        elif size == 6:
            size_array_dificult = size + 3
        elif size == 8:
            size_array_dificult = size + 3
        j = 0    
        while j < size_array_dificult:
            array_for_dificult.append(random.choice(colors))
            j+=1
        print(array_for_dificult)
        print('\n\n')

    def generate_code(size):
        """ Esta funcion se encarga de generar el codigo
            que adivinara el usuario
        """
        i = 0
        index = random.randint(1, len(colors) + 1)
        codigo_colores = []
        while i < size:
            codigo_colores.append(random.choice(colors)) 
            i+=1
        print(codigo_colores)
    
    if __name__ == "__main__":
        print("\n***************** SELECCIONE SU COMBINACIÓN ENTRE ESTOS COLORES *************************\n")
        generate_array_dificult(size)
        
        print('\n')
        print("***************** ESTE ES EL CODIGO DEL JUEGO *************************\n")
        generate_code(size)
        print("\n\n***************** FIN *************************")

    
def init_game(dificult):
    """ Esta es la funcion principal que inicia el juego"""
    print(dificult)
    
    if dificult == 1:
        print('Tu dificultad es : {}'.format(dificults[dificult]))
        size = 4
        bucle_dificult(size)
        return 0
    elif dificult == 2:
        print('Tu dificultad es : {}'.format(dificults[dificult]))
        size = 6
        bucle_dificult(size)
        return 0
    elif dificult == 3:
        print('Tu dificultad es : {}'.format(dificults[dificult]))
        size = 8
        bucle_dificult(size)
        return 0        
 
if __name__ == "__main__":
    """ Llevamos el flujo principal del programa"""
    banner()
    print('\n')
    print('\n')
#    while True:
    user = create_user()
    dif = int(input('Ingresa la dificultad: '))
    init_game(dif)
    print('\n')
    print('\nSu nombre de usuario es -------> {}\n', user.nickname)
    print('\n\n\t\t [ ! ]  GAME OVER ')