import pygame
import os
import time
pygame.mixer.init()
pygame.font.init()
WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")
border = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
red_health = 10
yellow_health = 10
font = pygame.font.SysFont("Verdana",30)
yellow_text = font.render(f"Health = {yellow_health}", True, (255,255,255))
red_text = font.render(f"Health = 10 {red_health}", True, (255,255,255))

bullet_vel = 7
max_bullets = 3
ss_w = 55
ss_h = 40
fps = 60
vel = 5
image = pygame.image.load(os.path.join("Lesson6/Assets","space.png"))
Red_ship = pygame.image.load(os.path.join("Lesson6/Assets","ship1.png"))
Red = pygame.transform.rotate(pygame.transform.scale(Red_ship,(ss_w,ss_h)),270)
Yellow_ship = pygame.image.load(os.path.join("Lesson6/Assets","ship2.png"))
Yellow = pygame.transform.rotate(pygame.transform.scale(Yellow_ship,(ss_w,ss_h)),90)
Hit = pygame.mixer.Sound("Lesson6/Assets/Grenade+1.mp3")

YELLOW_HIT = pygame.USEREVENT+1
RED_HIT = pygame.USEREVENT+2

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(image,(0,0))
    yellow_text = font.render(f"Health = {yellow_health}", True, (255,255,255))
    red_text = font.render(f"Health = {red_health}", True, (255,255,255))
    screen.blit(yellow_text,(25,25))
    screen.blit(red_text,(700,25))
    pygame.draw.rect(screen,(0,0,0),border)
    screen.blit(Red,(red.x,red.y))
    screen.blit(Yellow,(yellow.x,yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(screen,(255,0,0),bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,(255,255,0),bullet)
    pygame.display.update()

def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel > border.x + border.width:
        red.x -= 5
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < WIDTH:
        red.x += 5
    if keys_pressed[pygame.K_UP] and red.y - vel > 0:
        red.y -= 5
    if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < HEIGHT - 15:
        red.y += 5

def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0:
        yellow.x -= 5
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < border.x:
        yellow.x += 5
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0:
        yellow.y -= 5
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT - 15:
        yellow.y += 5

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)    
    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x < 0:
            red_bullets.remove(bullet)

    

def main():
    global yellow_health, red_health
    red = pygame.Rect(700,300,ss_w,ss_h)
    yellow = pygame.Rect(100,300,ss_w,ss_h)
    red_bullets = []
    yellow_bullets = []
    run = True
    clock = pygame.time.Clock()
    while run == True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2,10,5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_b and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2 - 2,10,5)
                    red_bullets.append(bullet)
            if event.type == RED_HIT:
                 red_health -= 1
                 Hit.play()
            if  event.type == YELLOW_HIT:
                yellow_health -= 1
                Hit.play()
        Winner = ""
        if red_health <= 0:
            Winner = "Yellow"
        elif yellow_health <= 0:
            Winner = "Yellow"
        if Winner != "":
            #draw_winner(Winner)
            break
        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed,red)
        yellow_movement(keys_pressed,yellow)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
        pygame.display.update()
    main()   
if __name__ == "__main__":
    main()