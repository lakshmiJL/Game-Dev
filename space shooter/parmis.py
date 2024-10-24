import pgzrun

WIDTH = 600
HEIGHT = 400

game_over = False
spaceship = Actor("spaceship")
spaceship.pos = (300,350)
"""
bugship = Actor("image 7")
bugship1 = Actor("image 7")
bugship2 = Actor("image 7")
bugship3 = Actor("image 7")
bugship4 = Actor("image 7")
bugship5 = Actor("image 7")
bugship6 = Actor("image 7")
bugship7 = Actor("image 7")
bugship8 = Actor("image 7")
bugship9 = Actor("image 7")
"""

"""
bugship.pos = (300,140)
bugship1.pos = (270,110)
bugship2.pos = (330,110)
bugship3.pos = (360,80)
bugship4.pos = (300,80)
bugship5.pos = (240,80)
bugship6.pos = (210,50)
bugship7.pos = (270,50)
bugship8.pos = (330,50)
bugship9.pos = (390,50)
bugs = [bugship, bugship1, bugship2 ,bugship3 ,bugship4 , bugship5, bugship6 , bugship7, bugship8, bugship9]
"""
bugs = []
for x in range(8):
    for y in range(4):
        bugs.append(Actor('alien'))
        #now the enemies will be ina straight line
        bugs[-1].x = 100+ 50*x
        #starting off the screen thats why putting it at -100,
        #slowly the enemy will come down
        bugs[-1].y = 80 + 50*y



bullets = []
score = 0
def gameOver():
    screen.draw.text("GAME OVER", (250,300))
direction = 1

def on_key_down(key):
    
        if key == keys.SPACE:        
            bullets.append(Actor('bullet'))
            #the last bullet added , set its position
            bullets[-1].x = spaceship.x
            bullets[-1].y = spaceship.y - 50
def update():
    global score
    global direction
    global bullets, bugs

    move = False

    if keyboard.left:
        spaceship.x -= 5

    if keyboard.right:
        spaceship.x += 5


    if len(bugs) ==0:
           game_over = True
    
    for bullet in bullets:
        if bullet.y <0:
            bullets.remove(bullet)
        else:
            bullet.y -= 2

    if len(bugs) > 0 and (bugs[0].x <50 or  bugs[-1].x >WIDTH-50):
        move = True
        direction *= -1
             
    for b in bugs:
        
        b.x += 5* direction
        if move == True:
            b.y += 0.2
        if b.y > HEIGHT:
            bugs.remove(b)
        for bullet in bullets:
            if bullet.colliderect(b): 
                score += 10
                bullets.remove(bullet)
                bugs.remove(b)
                if len(bugs) ==0:
                    gameOver()
    
        if b.colliderect(spaceship):
            gameOver()

def displayScore():
    screen.draw.text(str(score), (50,30))

def draw():
    screen.fill("blue")

    for bug in bugs:
        bug.draw()

    spaceship.draw()

    for bullet in bullets:
        bullet.draw()

    displayScore()  

    if len(bugs) ==0:
           gameOver()

pgzrun.go()