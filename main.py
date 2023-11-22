import pygame
import random
from pygame.locals import *
pygame.init()
from configs import *

pygame.init()
screen1 = Screen()
screen = pygame.display.set_mode([screen1.width, screen1.height], pygame.FULLSCREEN)
pygame.display.set_caption(screen1.title)
x = random.randint(0, screen.get_width() - Skins.dvd[0].get_width())
y = random.randint(0, screen.get_height() - Skins.dvd[0].get_height())
verticalMove = Move.DOWN
horizotalMove = Move.LEFT
vel = 3
colour = 0
run = True
clock = pygame.time.Clock()

while run:
    dt = clock.tick(60)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        run = False
    #movement
    if verticalMove == Move.UP:
        y -= vel
    elif verticalMove == Move.DOWN:
        y += vel
        
    if horizotalMove == Move.RIGHT:
        x += vel
    elif horizotalMove == Move.LEFT:
        x -= vel
    
    if  y <=0:
        verticalMove = Move.DOWN
        colour += 1
    elif y >= screen1.height - Skins.dvd[0].get_height():
        verticalMove = Move.UP
        colour += 1
    
    if x <=0 :
        horizotalMove = Move.RIGHT
        colour += 1
    elif x >= screen1.width - Skins.dvd[0].get_width():
        horizotalMove = Move.LEFT
        colour += 1
    
    if colour == len(Skins.dvd):
        colour = 0
        
    

    screen.fill("black")
    screen.blit(Skins.dvd[colour], [x, y])


    pygame.display.update()

pygame.quit()
