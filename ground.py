from constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os
from pygame.locals import *

ground_surfaces = (0,1,2,3)

ground_vertices = (
    (-1000,-0.1,500),
    (1000,-0.1,500),
    (-1000,-5,-1600),
    (1000,-5,-1600),

    )
def Ground():
    glBegin(GL_QUADS)
    x = 0
    for vertex in ground_vertices:
        x+=1
        glColor3fv((0.4,0.6,0.1))
        glVertex3fv(vertex)
    glEnd()
