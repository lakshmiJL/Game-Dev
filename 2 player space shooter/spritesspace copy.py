import pygame
pygame.init()


WIDTH = 1000
HEIGHT = 600
#set dimensions of the screen
screen= pygame.display.set_mode((WIDTH,HEIGHT))

bg = pygame.image.load("space.png")
border = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

ship_width = 55
ship_height = 50

class Spaceship(pygame.sprite.Sprite):
        def __init__(self,x,y,color):
            super().__init__()
            #yellow ship load image and rotate
            if color == "yellow":
               self.image = pygame.image.load("ship2.png")
               self.image = pygame.transform.rotate(self.image,90)
            #red ship load image and rotate
            elif color == "red":
                self.image = pygame.image.load("ship1.png")
                self.image = pygame.transform.rotate(self.image,270)

            self.image = pygame.transform.scale(self.image,(ship_width,ship_height))
            self.rect = self.image.get_rect()
            self.rect.topleft = x,y

red = Spaceship(700,HEIGHT/2,"red")
yellow = Spaceship(300,HEIGHT/2,"yellow")

#main loop
run = True
while run:
    #quit event to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("white")
    #bg
    screen.blit(bg,(0,0))
    #border
    pygame.draw.rect(screen,"white",border)
    #red ship
    screen.blit(red.image,red.rect.topleft)
    #yellow ship
    screen.blit(yellow.image,yellow.rect.topleft)

    #update the display
    pygame.display.update()