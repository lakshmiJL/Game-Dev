import pygame
import random,os
pygame.init()
WIDTH=350
HEIGHT=400
screen = pygame.display.set_mode( (WIDTH, HEIGHT ) )
pygame.display.set_caption('clicked on image')
redSquare = pygame.image.load("alien.png").convert()
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT)) 
x1 = 20; # x coordnate of image
y1 = 30; # y coordinate of image
def drawo():
    screen.blit(SPACE ,  (0,0))
    screen.blit(redSquare ,  ( x1,y1))
    redSquare.get_rect() 
    place()
    pygame.display.update() 
def place():
    x1 = random.randint(50, 350-50)
    y1 = random.randint(50, 400-50)
 
running = True
while (running):
    drawo()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if redSquare.get_rect().collidepoint(x, y):
                x1 = random.randint(50, 350-50)
                
                y1 = random.randint(50, 400-50)
                pygame.display.update()
                print('clicked on image')
#loop over, quite pygame
pygame.quit()