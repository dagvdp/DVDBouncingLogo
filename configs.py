import pygame

class Screen:
    width = 1920
    height = 1080
    title = "DVD"

class Skins:
    dvd = [pygame.image.load("imgs/dvdlogo1.png"),
           pygame.image.load("imgs/dvdlogo2.png"),
           pygame.image.load("imgs/dvdlogo3.png"),
           pygame.image.load("imgs/dvdlogo4.png"),
           pygame.image.load("imgs/dvdlogo5.png"),
           pygame.image.load("imgs/dvdlogo6.png")]
    
class Move:
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3