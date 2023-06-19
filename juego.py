import pygame
from tablero import Tablero


v_width = 600
v_height = 600

col = 8
filas = 8

box_width = v_width // col
box_height = v_height// filas


class Juego:
    def __init__(self,window):
        self.tablero = Tablero()
        self.selected = None
        self.turn =0
        self.movimientos ={}
        self.window = window
    
    def reset(self):
        self.selected=None
        self.tablero = Tablero()
        self.turn=0
        self.movimientos ={}

    def select(self,i,j):
        if self.selected:
            result = self._mover(i,j)
            if not result:
                self.selected=None
                self.select(i,j)
        
        pieza = self.tablero.getPieza(i,j)
        if pieza !=0 and pieza.turn == self.turn:
            self.selected = pieza
            self.movimientos = self.tablero.getMovimientosV(pieza)
            return True
        
        return False
    
    def _mover(self,i,j):
        pieza = self.tablero.getPieza(i,j)
        if self.selected and pieza ==0 and (i,j) in self.movimientos:
            self.tablero.moverPieza(i,j,self.selected)
            salto = self.movimientos[(i,j)]
            if salto:
                self.tablero.delete(salto)
            self.cambiarTurno()
        else :
            return False
        return True
    
    def cambiarTurno(self):
        self.movimientos={}

        if self.turn ==0:
            self.turn = 1
        else :
            self.turn = 0
    
    def drawMovimientos(self,movimientos):
        for mov in movimientos:
            i,j = mov
            pygame.draw.circle(self.window,(88, 214, 141),(j * box_height + box_height//2,i * box_height+box_height//2),15)
    
    def ganar(self):
        return self.tablero.ganar()
    
    def getTablero(self):
        return self.tablero

    def ai_move(self, tablero):
        self.tablero = tablero
        self.cambiarTurno()

    def flip(self):
        self.tablero.drawTablero(self.window)
        self.drawMovimientos(self.movimientos)
        pygame.display.flip()