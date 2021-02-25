from constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import pygame
import os

from pygame.locals import *
x=6
y=0
z=4
x1=5
y1=7
z1=3
y2=8
table_verticies_vector3 =(
#gambe a terra
(x,y,z),
(x,y,z1),
(x1,y,z1),
(x1,y,z),

(x,y,-z1),
(x,y,-z),
(x1,y,-z),
(x1,y,-z1),

(-x1,y,-z1),
(-x1,y,-z),
(-x,y,-z),
(-x,y,-z1),

(-x1,y,z),
(-x1,y,z1),
(-x,y,z1),
(-x,y,z),
#gambe in alto
(x,y1,z),
(x,y1,z1),
(x1,y1,z1),
(x1,y1,z),

(x,y1,-z1),
(x,y1,-z),
(x1,y1,-z),
(x1,y1,-z1),

(-x1,y1,-z1),
(-x1,y1,-z),
(-x,y1,-z),
(-x,y1,-z1),

(-x1,y1,z),
(-x1,y1,z1),
(-x,y1,z1),
(-x,y1,z),

#rect
(x,y2,z),#primo
(x,y2,-z),#secondo
(-x,y2,-z),#terzo
(-x,y2,z),#quarto
)
table_edges_vector2 = (
(0,1),
(1,2),
(2,3),
(3,0),
#uno
(4,5),
(5,6),
(6,7),
(7,4),
#due
(8,9),
(9,10),
(10,11),
(11,8),
#tre
(12,13),
(13,14),
(14,15),
(15,12),
#quattro
(16,17),
(17,18),
(18,19),
(19,16),
#cinque
(20,21),
(21,22),
(22,23),
(23,20),
#sei
(24,25),
(25,26),
(26,27),
(27,24),
#sette
(28,29),
(29,30),
(30,31),
(31,28),
#otto
(32,33),
(33,34),
(34,35),
(35,32),
#rettangolone
(0,16),
(1,17),
(2,18),
(3,19),
#gamba uno
(4,20),
(5,21),
(6,22),
(7,23),
#gamba due
(8,24),
(9,25),
(10,26),
(11,27),
#gamba tre
(12,28),
(13,29),
(14,30),
(15,31),
#gamba quattro
(16,21),
(21,26),
(26,31),
(31,16),
#tavolone faccia in basso
(16,32),
(21,33),
(26,34),
(31,35),
#righette

)

table_faces_vector4 = (
(0,1,2,3),
(4,5,6,7),
(8,9,10,11),
(12,13,14,15),
#quadrati in basso
(16,17,18,19),
(20,21,22,23),
(24,25,26,27),
(28,29,30,31),
#quadrati in alto
(0,1,17,16),
(1,2,18,17),
(2,3,19,18),
(3,0,16,19),
(4,5,21,20),
(5,6,22,21),
(6,7,23,22),
(7,4,20,23),
(8,9,25,24),
(9,10,26,25),
(10,11,27,26),
(11,8,24,27),
(12,13,29,28),
(13,14,30,29),
(14,15,31,30),
(15,12,28,31),
(16,21,26,31),#rettangolone1
(32,33,34,35),#rettaangolone2
(16,32,33,21),#lato alto
(21,33,34,26),#lato alto
(34,26,31,35),#lato alto
(31,16,32,35),#lato alto
)
def Table():
    glBegin(GL_QUADS)
    for surface in table_faces_vector4:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            #glColor3f(1,0,0);
            glVertex3fv(table_verticies_vector3[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in table_edges_vector2:
        for vertex in edge:
            glVertex3fv(table_verticies_vector3[vertex])
    glEnd()
