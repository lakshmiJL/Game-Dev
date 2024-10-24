import pgzrun
import random
WIDTH=600
HEIGHT=400
Spaceship=Actor("spaceship")
Spaceship.x=300
Spaceship.y=350
bullets = []
bugs=[]
for i in range(5):
    bug = Actor("alien")
    bug.x = 100 + i* 50
    bug. y = 100
    bugs.append(bug)

def draw():
    screen.blit("background",(0,0))
    Spaceship.draw()
    for bullet in bullets:
        bullet.draw()
    for bug in bugs:
        bug.draw()

def update():
    global score
    if keyboard.left:
        Spaceship.x-=5
    if keyboard.right:
        Spaceship.x+=5
    if keyboard.space:
        bullet = Actor("bullet")
        bullet.x =  Spaceship.x
        bullet.y =  Spaceship.y - 30
        bullets.append(bullet)
    for bullet in bullets:
        bullet.y -= 5
        for bug in bugs:
            if bug.colliderect(bullet):
                bugs.remove(bug)
                bullets.remove(bullet)
    for bug in bugs:
        bug.y += 1
        
        
pgzrun.go()