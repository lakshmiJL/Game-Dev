import pgzrun

WIDTH = 799
HEIGHT = 599


#making the spaceship
spaceship = Actor("spaceship")
spaceship.x = WIDTH/2
spaceship.y = HEIGHT - 100

bullets = []

#making aliens
aliens = []
direction = 1
#score
score = 0
ship_dead = False
for i in range(5):
    for j in range(5):
        alien = Actor("alien")
        alien.x = 250 +  i * 50
        alien.y = 50 + j * 50
        aliens.append(alien)

def draw():
    
    screen.fill("sky blue")
    if ship_dead == False:
        spaceship.draw()
        for bullet in bullets:
            bullet.draw() 
    else:
        screen.draw.text("Ship is dead, You Lost",center=(WIDTH/2,HEIGHT/2))
        screen.draw.text(f"Final score: {score}",center=(WIDTH/2,HEIGHT/2+50),color = "white", fontsize=30)
    for alien in aliens:
        alien.draw()
    screen.draw.text(f"score: {score}",(50,50),color = "white", fontsize=30)
    if len(aliens) == 0:
        game_over()
"""
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = spaceship.x
        bullet.y = spaceship.y - 20
        bullets.append(bullet)
"""
def on_mouse_down(pos):
    bullet = Actor("bullet")
    bullet.x = spaceship.x
    bullet.y = spaceship.y - 20
    bullets.append(bullet)

def update():
    global direction, score, ship_dead
    move = False
    if keyboard.a:
        spaceship.x -= 5
    if keyboard.d:
        spaceship.x += 5
    if keyboard.w:
        spaceship.y -= 5
    if keyboard.s:
        spaceship.y += 5

    for bullet in bullets:
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    #to change the x direction of the alien
    if len(aliens) > 0 and (aliens[0].x < 50 or aliens[-1].x > WIDTH-50):
        move = True
        direction = direction * -1
    #make the alien move and check for collision
    for alien in aliens:
        alien.x += 1 * direction
        if move == True:
            alien.y += 1
        for bullet in bullets:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 1
                if len(aliens) == 0:
                    game_over()
        if alien.colliderect(spaceship):
            game_over()
            ship_dead = True

def game_over():
    screen.draw.text("GAME OVER", (250,300))      

pgzrun.go()