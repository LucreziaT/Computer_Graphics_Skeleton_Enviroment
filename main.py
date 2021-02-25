import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import math
import numpy as np
import pygame
from pygame.locals import *
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sqrt
from numpy import pi
from numpy import arccos
import json
import random
from chair import Chair
from table import Table
from glass import Glass
from dish import Dish
from ground import Ground

def cylinder_between(a,b):
    p =[a[1] - b[1],a[2]-b[2],a[0]-b[0]]
    h = math.sqrt(p[0]*p[0] + p[1]*p[1] + p[2]*p[2])
    axis = (1, 0, 0) if math.hypot(p[0], p[1]) < 0.001 else np.cross(p, (0, 0, 1))
    angle = -math.atan2(math.hypot(p[0], p[1]), p[2])*180/pi
    return(h,angle,*axis)

def drawSphere(sphere, x=0, y=0, z=0, radius=0.4,l=0.5,m=0,n=0.1):
    ''' This function draws a sphere in coordinates (x,y,z) '''
    glPushMatrix()
    glTranslatef(x, y, z)  # Move to the place
    glColor4f(l,m,n, 1.0)  # Select color
    gluSphere(sphere, radius, 32, 16)  # Draw sphere

    glPopMatrix()


def drawCylinder(cylinder, x=0,y=0,z=0,h=1,angolo=0,x2=0,y2=0,z2=0,radius=0.1):
    ''' This function draws a cylinder in coordinates (x,y,z) '''
    glPushMatrix()
    glTranslatef(x, y, z)  # Move to the place
    glRotatef(angolo,x2,y2,z2 )
    glColor4f(0.3,0,0.9, 0.0) # Select color
    gluCylinder(cylinder,radius,radius,h,32, 16 )  # Draw sphere
    glPopMatrix()

def drawDisk(disk,x,y,z):
    glPushMatrix()
    glTranslatef(x, y+2, z)  # Move to the place
    glRotatef(90,1,0,0)
    glRotatef(10,0,0,1)
    glColor4f(0.2,0.1,0.9, 1.0) # Select color
    gluDisk(disk,0,2,32,16)  # Draw disk
    glPopMatrix()

def sortlu(frame): #I reorder the jsons in ascending order
    lunghezza=len(frame)
    newstr=frame[0]
    for i in range(lunghezza-1,0,-1) :
        if lunghezza-i < lunghezza-5 :
            newstr=newstr+frame[lunghezza-i]
    valore=abs(int(newstr))
    return(valore)

def nextframe(u):
    newstr=str(u)+'.json'
    return(newstr)

def Skeleton(u):
    m=80
    sphere = gluNewQuadric()  # Create new sphere
    cylinder= gluNewQuadric() # Create new cylinder
    disk=gluNewQuadric() # Create new disk
    frames = os.listdir('animation')
    frames.sort(key=sortlu)

    number_frames = len(frames)
    for frame in frames:
        with open(os.path.join('animation', nextframe(u))) as f:
            skeleton = json.load(f)

            cx=skeleton[0][1]
            cy=skeleton[0][2]
            cz=skeleton[0][0]

            center_vector=[]
            incl3=[]
            for i in range (0,17):

                x=skeleton[i][0]
                y=skeleton[i][1]
                z=skeleton[i][2]
                temp_list=[x/m,y/m,z/m]
                center_vector.append(temp_list)

            incl3.append(cylinder_between(center_vector[7],center_vector[0]))
            incl3.append(cylinder_between(center_vector[0],center_vector[1]))
            incl3.append(cylinder_between(center_vector[1],center_vector[2]))
            incl3.append(cylinder_between(center_vector[2],center_vector[3]))
            incl3.append(cylinder_between(center_vector[0],center_vector[4]))
            incl3.append(cylinder_between(center_vector[4],center_vector[5]))
            incl3.append(cylinder_between(center_vector[5],center_vector[6]))
            incl3.append(cylinder_between(center_vector[8],center_vector[7]))
            incl3.append(cylinder_between(center_vector[9],center_vector[8]))
            incl3.append(cylinder_between(center_vector[10],center_vector[9]))
            incl3.append([0,0,0,0,0])
            incl3.append(cylinder_between(center_vector[8],center_vector[11]))
            incl3.append(cylinder_between(center_vector[11],center_vector[12]))
            incl3.append(cylinder_between(center_vector[12],center_vector[13]))
            incl3.append(cylinder_between(center_vector[8],center_vector[14]))
            incl3.append(cylinder_between(center_vector[14],center_vector[15]))
            incl3.append(cylinder_between(center_vector[15],center_vector[16]))

        l=0
        for joint in skeleton:
            #print('dentro')
            a=(joint[1]-skeleton[0][1])/m
            b=(joint[2]-skeleton[0][2])/m
            c=(joint[0]-skeleton[0][0])/m
            drawCylinder(cylinder,a,b,c,incl3[l][0],incl3[l][1],incl3[l][2],incl3[l][3],incl3[l][4])
            drawSphere(sphere,a,b,c)

            l=l+1
            if l==10:
                drawDisk(disk,a,b,c)
                drawSphere(sphere, a,b+2.2,c,0.3,0.2,0.1,0.9)
            if l==17:
                l=0
        time.sleep(0.1)
        break

def main():
    pygame.init()
    display = (1900,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    u=0

    #pygame.mixer.music.load("Experience.mp3")
    #pygame.mixer.music.play()

    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    glTranslatef(0,0, -70)

    object_passed = False
    i=0
    controllore=0
    s=0
    w=0
    camera_y=0
    rotazione=0
    while not object_passed:
        if rotazione==72 or rotazione==-72:
            rotazione=0
        glClearColor(1,1,0.9,0)
        if i==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        glTranslatef(0.5,0,0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(-0.5,0,0)

                    if event.key == pygame.K_UP:
                            glTranslatef(0,-1,0)
                    if event.key == pygame.K_DOWN:
                        if camera_y < 1:
                            glTranslatef(0,1,0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0,0,1.0)

                    if event.button == 5:
                        glTranslatef(0,0,-1.0)
                keypress = pygame.key.get_pressed()
                if keypress[pygame.K_a]:
                    rotazione=rotazione-1
                    glRotate(5,0,0.5,0)#ang,x,y,z
                if keypress[pygame.K_w]:
                    if w<35:
                        w=w+1
                        glRotate(5,0.5,0,0)#ang,x,y,z
                if keypress[pygame.K_s]:
                    rotazione=rotazione+1
                    glRotate(5,0,-0.5,0)#ang,x,y,z
                if keypress[pygame.K_z]:
                    if w>0:
                        w=w-1
                        glRotate(5,-0.5,0,0)#ang,x,y,z

        x = glGetDoublev(GL_MODELVIEW_MATRIX)#, modelviewMatrix)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        #print('rotazione',rotazione)


        # slowly move forward :
        if camera_z >= 40 and i==0:
            glTranslatef(0,0,0.8)
        else:
            i=1
            controllore=1
            glTranslatef(0,0,0)



        if (rotazione <40 and rotazione >-1) or (rotazione <-49 and rotazione >-72):
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            if controllore==0:
                u=0
            Ground()
            if (rotazione>21 and rotazione<51 ) or (rotazione<-19 and rotazione>-52):
                Skeleton(u)
                glPushMatrix()
                glRotate(270,0,1,0)
                glTranslated(-1.5,-1,0)
                Chair()
                glPopMatrix()
                glPushMatrix()
                glRotate(120,0,1,0)
                glTranslated(-14,-9,9)
                Table()
                glPopMatrix()


                glPushMatrix()
                glTranslated(13,-1,7)
                Dish()
                glPopMatrix()
                glPushMatrix()
                glTranslated(18,-1,9)
                Glass()
                glPopMatrix()
                u=u+1
                if u < 371:
                    u=u
                else:
                    u=0
            else:
                glPushMatrix()
                glRotate(270,0,1,0)
                glTranslated(-1.5,-1,0)
                Chair()
                glPopMatrix()
                Skeleton(u)
                glPushMatrix()
                glRotate(120,0,1,0)
                glTranslated(-14,-9,9)
                Table()
                glPopMatrix()


                glPushMatrix()
                glTranslated(13,-1,7)
                Dish()
                glPopMatrix()
                glPushMatrix()
                glTranslated(18,-1,9)
                Glass()
                glPopMatrix();
                u=u+1
                if u < 371:
                    u=u
                else:
                    u=0
        else :
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            if controllore==0:
                u=0
            Ground()
            if (rotazione>21 and rotazione<51 ) or (rotazione<-19 and rotazione>-52):
                glPushMatrix()
                glRotate(120,0,1,0)
                glTranslated(-14,-9,9)
                Table()
                glPopMatrix()


                glPushMatrix()
                glTranslated(13,-1,7)
                Dish()
                glPopMatrix()
                glPushMatrix()
                glTranslated(18,-1,9)
                Glass()
                glPopMatrix()
                Skeleton(u)
                glPushMatrix()
                glRotate(270,0,1,0)
                glTranslated(-1.5,-1,0)
                Chair()
                glPopMatrix()
                u=u+1
                if u < 371:
                    u=u
                else:
                    u=0
            else:
                glPushMatrix()
                glRotate(270,0,1,0)
                glTranslated(-1.5,-1,0)
                Chair()
                glPopMatrix()
                glPushMatrix()
                glRotate(120,0,1,0)
                glTranslated(-14,-9,9)
                Table()
                glPopMatrix()


                glPushMatrix()
                glTranslated(13,-1,7)
                Dish()
                glPopMatrix()
                glPushMatrix()
                glTranslated(18,-1,9)
                Glass()
                glPopMatrix()
                Skeleton(u)
                u=u+1
                if u < 371:
                    u=u
                else:
                    u=0

        #print(u)
        pygame.display.flip()


        if camera_z <= 0:
            object_passed = True



main()
