# Import the Pygame Zero Library
import pygame
from pygame.locals import *
from time import *
import random
#import pgzrun
#from random import randint
pygame.init()
screen=pygame.display.set_mode((600, 600))
# Pygame Standard for deciding the title of your game window
TITLE = "Good Shot"
# Pygame Standard for deciding the width and height for your game window in pixels
#WIDTH = 500
#HEIGHT = 500

# variable to store the message displayed on your screen
message = ""
font=pygame.font.SysFont("Times New Roman",72)
# Actor is built-in object in pgzero
# interacts with other actors, move around on screen
# Similar to Sprite in Scratch
#alien = Actor('alien')
#alien.pos = 50,50 Lesson6/goodshot.py
player = pygame.image.load("/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson6/goodshot.py").convert()
player_x = 50
player_y = 50
screen.fill((255,255,255))
screen.blit(player, (player_x, player_y))

pygame.display.update()

def place_alien():
  player_x = random.randint(50, 600-50)
  player_y = random.randint(50, 600-50)




def main():
    running = True
    while running:
        global player_x,player_y
        #screen.fill((255,255,255))
        #screen.blit(player, (player_x, player_y))
        #rect = player.get_rect()
        
        event = pygame.event.poll()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.get_rect().collidepoint(event.pos):
                    print("done")
                    message = "Good Shot"
                    player_x = random.randint(50, 600-50)
                    player_y = random.randint(50, 600-50)
                    #screen.blit(player, (player_x, player_y))
                    pygame.display.update()
                else:
                    message = "You missed"
                    pygame.display.update()



if __name__ == "__main__":
    main()


# This method needs to be called to start processing
#place_alien()
#pgzrun.go()