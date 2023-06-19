import pygame
import sys

grid = []

v_width = 600
v_height = 600

col = 8
filas = 8

box_width = v_width // col
box_height = v_height// filas

Corona = pygame.transform.scale(pygame.image.load('crown.png'),(44,25))

class Pieza:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.x=0
        self.y=0
        self.fichaBlanca = False
        self.turn=0
        self.fichaNegra = False
        self.king = False
        self.pos()
    
        
  
    def drawFicha(self,window,side):
         
         
         if(side == 'Blanca'):
          pygame.draw.circle(window,(55,48,34), (self.j *box_width+37.5, self.i * box_height+37.5),22)
          pygame.draw.circle(window,(249,227,183), (self.j *box_width+37.5, self.i * box_height+37.5),20)
          
         if(side =='Negra'):
          pygame.draw.circle(window,(249,227,183), (self.j *box_width+37.5, self. i* box_height+37.5),22)
          pygame.draw.circle(window, (55,48,34), (self.j *box_width+37.5, self.i * box_height+37.5),20) 

         if self.king:
             window.blit(Corona,(self.x- Corona.get_width()//2,self.y - Corona.get_height()//2))

    def pos(self):
       self.x= (box_height*self.j+box_height//2 )
       self.y= (box_height*self.i+box_height//2 )
             
         
    def setFicha(self,side):
         if(side == 'Blanca'):
          self.fichaBlanca=True
          self.turn =1
         elif(side =='Negra'):
          self.fichaNegra=True
          self.turn=0

    def hacerRey(self):
       self.king = True
    
    def moverPieza(self,i,j):
       self.i=i
       self.j=j
       self.pos()
    
    
  

    
                  
