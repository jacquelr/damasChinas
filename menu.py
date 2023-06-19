import pygame
import sys
import subprocess
from pygame.locals import *

pygame.init()
tamaño_pantalla = (700, 400)
ventana = pygame.display.set_mode(tamaño_pantalla)
fond = pygame.font.Font(None, 30)
menu = ["start", "opciones"]
dificultad = ["Facil", "Intermedio", "Dificil"]
dificultad_sel = 1

blanco = (255, 255, 255)
negro = (0, 0, 0)

def mostrar(texto, x, y):
    texto_ = fond.render(texto, True, negro)
    ventana.blit(texto_, (x, y))

def main():
    op = None
    escoger = True
    
    while escoger:
        ventana.fill(blanco)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == KEYDOWN:
                if evento.key == K_RETURN:
                    if op is not None:
                        if op == 1:
                            opcion()
                        elif op == 0: 
                            start()
                        escoger = False
                elif evento.key == K_UP:
                    if op is None:
                        op = len(menu) - 1
                    else:
                        op = (op - 1) % len(menu)
                elif evento.key == K_DOWN:
                    if op is None:
                        op = 0
                    else:
                        op = (op + 1) % len(menu)
            
        for i, option in enumerate(menu):
            texto_x = 70
            texto_y = 100 + i * 60
            if i == op:
                pygame.draw.rect(ventana, (100, 100, 100), (texto_x - 20, texto_y - 10, 250, 40))
            mostrar("Damas Chinas", 50, 40)
            mostrar(f"{option}", texto_x, texto_y)
        
        mostrar(f"Dificultad actual: {dificultad[dificultad_sel]}", 50, 300)  
        pygame.display.update()

def start():
    global dificultad_sel

    pygame.quit()
    subprocess.call(["python", "main.py", str(dificultad_sel)])
    sys.exit()
    

def opcion():
    global dificultad_sel
    escoger = True
    while escoger:
        ventana.fill(blanco)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == KEYDOWN:
                if evento.key == K_RETURN:
                    escoger = False
                elif evento.key == K_UP:
                    dificultad_sel = (dificultad_sel - 1) % len(dificultad)
                elif evento.key == K_DOWN:
                    dificultad_sel = (dificultad_sel + 1) % len(dificultad)
                elif evento.key == K_ESCAPE:  
                    escoger = False  

        for i, option in enumerate(dificultad):
            texto_x = 270
            texto_y = 100 + i * 50
            if i == dificultad_sel:
                pygame.draw.rect(ventana, (100, 100, 100), (texto_x - 20, texto_y - 10, 200, 40))
            mostrar("Seleccione una dificultad:", 230, 50) 
            mostrar(f"{option}", texto_x, texto_y)
        
        pygame.display.update()
    main()

main()
