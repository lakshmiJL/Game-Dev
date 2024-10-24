import pgzrun
import random
#screen dimensions
WIDTH = 1200
HEIGHT = 600

#definiting colours
WHITE = (255,255,255)
BLUE = (0,0,255)

#create a ship
ship = Actor('galaga')
bug = Actor('bug')

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 5

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

#we want 8 enemies
for x in range(8):
    enemies.append(Actor('bug'))
    #now the enemies will be ina straight line
    enemies[-1].x = 100+ 90*x
    #starting off the screen thats why putting it at -100,
    #slowly the enemy will come down
    enemies[-1].y = 80
    
score = 0
direction = 1

#for updating the score
def displayScore():
    screen.draw.text(str(score), (50,30))

def on_key_down(key):
    if key == keys.SPACE:        
        bullets.append(Actor('bullet'))
        #the last bullet added , set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

   
def update():
    global score
    global direction
    moveDown = False
    #move the ship left or right with arrow keys
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0
            
    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH
    #to fire bullets
    #it should not be while you on hold spapce key event
    #rather it should be on s[ace key down event
    '''
    if keyboard.space:
        print("Pressing space")
        bullets.append(Actor('bullet'))
        #the last bullet added , set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y
    '''
    for bullet in bullets:
        #if the bullet reaches the top of the screen it should get removed
        #else the list will become huge
        if bullet.y <=0 :
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    
    #check the position of the last enemy
    
    if len(enemies)>0  and (enemies[-1].x > WIDTH-80 or enemies[0].x < 80):
        moveDown = True
        direction = direction*-1
    for enemy in enemies:
        enemy.x += 5*direction
        if moveDown == True:
            enemy.y += 50
        #checking if the enemy hits a bullet while moving down
        #iterate over all the bullets and check for a collision
        for bullet in bullets :
            if enemy.colliderect(bullet):
                sounds.eep.play()
                score +=100
                #we also want to destory the bullet
                bullets.remove(bullet)
                enemies.remove(enemy)
        
                     
def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    ship.draw()
    displayScore()
    
pgzrun.go()