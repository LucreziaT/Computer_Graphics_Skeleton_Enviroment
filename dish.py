from constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import os
from pygame.locals import *

x=1.7
y=0
z=1.7
y2=0.5

vertices= (
    (x, y, -z),
    (x, y2, -z),
    (-x, y2, -z),
    (-x, y, -z),
    (x, y,z),
    (x, y2, z),
    (-x, y2, z),
    (-x, y, z)
    )
edges = (
    (4,0),
    (0,3),
    (3,7),
    (7,4),

    (5,1),
    (1,2),
    (2,6),
    (6,5),

    (5,4),
    (1,0),
    (2,3),
    (6,7),
)
colors = (
    (0.9,0.5,0.1),
    (0.9,0.5,0.6),
    (0.9,0.6,0),
    (0.9,0.6,0.5),
    (0.4,0,0.3 ),
    (0.9,0.7,0.4),
    (0.9,0.7,0.9),
    (0.9,0.8,0.3),
    (0.9,0.8,0.8),
    (0.9,0.9,0.2),
    (0.9,0.9,0.7),
    (0.9,0.5,0.5),
    )
surfaces = (
    (0,1,2,3),
    (3,2,6,7),
    (7,6,5,4),
    (4,5,1,0),
    (1,5,6,2),
    (4,0,3,7)
    )


def Dish():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
