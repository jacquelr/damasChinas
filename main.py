import pygame
import sys
from tkinter import messagebox
from juego import Juego
from ia import minimax
import sys
grid = []

pygame.init()
v_width = 600
v_height = 600

col = 8
filas = 8

box_width = v_width // col
box_height = v_height // filas
window = pygame.display.set_mode((v_width, v_height))


dificultad_actual = int(sys.argv[1])
dificultad=0

if dificultad_actual == 0:
    dificultad = 1
elif dificultad_actual == 1:
    dificultad = 2
elif dificultad_actual == 2:
    dificultad = 3
else:
    dificultad = 2

def main():

    juego = Juego(window)
    play = True

    while play:

        if juego.turn == 1:
            value, tablero = minimax(juego.getTablero(), dificultad, True, juego)
            juego.ai_move(tablero)
            print(dificultad)

        ganador = juego.ganar()
        if ganador is not None:
            messagebox.showinfo("Ganador", "El ganador es " + ganador)
            break

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                i = y // box_width
                j = x // box_height

                if dificultad != 0:
                    juego.select(i, j)

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

        window.fill((0, 0, 0))

        juego.flip()


main()
