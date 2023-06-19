import pygame
import sys
from pieza import Pieza






v_width = 600
v_height = 600

col = 8
filas = 8

box_width = v_width // col
box_height = v_height// filas





class Tablero:

    def __init__(self):
        self.grid =[]
        self.piezaaSelect =None
        self.piezasNegras = 12
        self.piezasBlancas=12
        self.kingNegras=0
        self.kingBlancas=0
        self.iniciarFichas()

    def setFicha(self,side,pieza):
        pieza.setFicha(side)
          
    def drawTablero(self,window):

        window.fill((55,48,34))
        for i in range(filas):
            for j in range(i %2,col ,2):
                pygame.draw.rect(window, (249,227,183), (i *box_width, j * box_height, box_width-1, box_height-1))
        
        for i in range(filas):
            for j in range(col):
                box=self.grid[i][j]
                if box!=0:
                    if(box.fichaBlanca):
                        box.drawFicha(window,'Blanca')
                    if(box.fichaNegra):
                        box.drawFicha(window,'Negra')
    
 

          
    def iniciarFichas(self):

        for i in range(filas):
            self.grid.append([])
            for j in range(col):
                if j %2 ==((i+1)%2):
                    if i <3:
                      self.grid[i].append(Pieza(i,j))
                      self.setFicha('Blanca',self.grid[i][j])
                    elif i>4:
                      self.grid[i].append(Pieza(i,j)) 
                      self.setFicha('Negra',self.grid[i][j]) 
                    else :
                      self.grid[i].append(0)  
                else:
                  self.grid[i].append(0)

    def moverPieza(self,i,j,pieza):
         self.grid[pieza.i][pieza.j], self.grid[i][j] = self.grid[i][j] , self.grid[pieza.i][pieza.j]
         pieza.moverPieza(i,j)

         if i == filas-1 or i ==0:
             pieza.hacerRey()
             if pieza.fichaBlanca :
                 self.kingBlancas +=1
             elif pieza.fichaNegra :
                 self.kingNegras +=1
                 
    def getPieza(self,i,j):
        return self.grid[i][j]
    
    def getMovimientosV(self,pieza):
        movimientos={}
        izq = pieza.j -1
        der = pieza.j +1
        fila = pieza.i
        
        if pieza.fichaNegra or pieza.king:
        
            movimientos.update(self._movimientoIzq(fila-1, max(fila-3,-1),-1,pieza,izq))
            movimientos.update(self._movimientoDer(fila-1, max(fila-3,-1),-1,pieza,der))

        if pieza.fichaBlanca or pieza.king:
          
            movimientos.update(self._movimientoIzq(fila+1, min(fila+3,filas),1,pieza,izq))
            movimientos.update(self._movimientoDer(fila+1, min(fila+3,filas),1,pieza,der))
        
        return movimientos
    
    def _movimientoIzq(self,inicio,stop,step,pieza,izq,skipped=[]):
        movimientos={}
        last =[]
        for i in range(inicio,stop,step):
            if izq <0:
                break
            current = self.getPieza(i,izq)
            if current ==0:
                if skipped and not last:
                    break
                elif skipped:
                    movimientos[(i,izq)]=last + skipped
                else: 
                   movimientos[(i,izq)]=last 
                
                if last:
                    if step ==-1:
                        fila = max(i-3,0)
                    else:
                        fila = min(i+3, filas)
                    
                    movimientos.update(self._movimientoIzq(i+step, fila,step,pieza,izq-1,skipped=last))
                    movimientos.update(self._movimientoDer(i+step, fila,step,pieza,izq+1,skipped=last))
                break
                   
            elif current.fichaBlanca == pieza.fichaBlanca or current.fichaNegra==pieza.fichaNegra:
                break
            else: 
                last = [current]
            izq -=1  
              
        return movimientos
    
    def delete ( self, piezas):
        for pieza in piezas:
            self.grid[pieza.i][pieza.j]=0
            if pieza.fichaBlanca and pieza !=0:
                self.piezasBlancas -=1
            elif pieza.fichaNegra and pieza !=0:
                self.piezasNegras -=1

    def ganar(self):
        if self.piezasNegras <=0:
            return 'Blancas'
        elif self.piezasBlancas <=0:
            return 'Negras'
        return None
    
    def _movimientoDer(self,inicio,stop,step,pieza,der,skipped=[]):
        movimientos={}
        last =[]
        for i in range(inicio,stop,step):
            if der >= col:
                break
            current = self.getPieza(i,der)
            if current ==0:
                if skipped and not last:
                    break
                elif skipped:
                    movimientos[(i,der)]=last + skipped
                else: 
                   movimientos[(i,der)]=last 
                
                if last:
                    if step ==-1:
                        fila = max(i-3,0)
                    else:
                        fila = min(i+3, filas)
                    
                    movimientos.update(self._movimientoIzq(i+step, fila,step,pieza,der-1,skipped=last))
                    movimientos.update(self._movimientoDer(i+step, fila,step,pieza,der+1,skipped=last))
                break
                   
            elif current.fichaBlanca == pieza.fichaBlanca or current.fichaNegra==pieza.fichaNegra:
                break
            else: 
                last = [current]
            der +=1 

        return movimientos
    
    def evaluate(self):
        return self.piezasBlancas - self.piezasNegras + (self.kingBlancas * 0.5 - self.kingNegras * 0.5)

    def getPiezasBlancas(self):
        piezas = []
        for fila in self.grid:
            for pieza in fila:
                if pieza != 0 and pieza.fichaBlanca:
                    piezas.append(pieza)
        
        return piezas
    
    def getPiezasNegras(self):
        piezas = []
        for fila in self.grid:
            for pieza in fila:
                if pieza != 0 and pieza.fichaNegra:
                    piezas.append(pieza)

        return piezas



                  
        

    
                          
      


