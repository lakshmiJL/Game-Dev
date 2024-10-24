import pgzrun
WIDTH=600
HEIGHT=600
score=0
ship=Actor("galaga")
ship.x=300
ship.y=400
bullets=[]
bugs=[]
level=1
for i in range(7):
    bug=Actor("bug")
    bug.x=70+(50*i)
    bug.y=200
    bugs.append(bug)
    
ship.dead=False
def draw():
    screen.fill("slate gray")
    if ship.dead==False:
        ship.draw()
    else:
        screen.draw.text("game over!",(300,300),color="red")

    for b in bullets:
        b.draw()
    for bug in bugs:
        bug.draw()
    screen.draw.text (str(score),(15,15),color=  "deep sky blue")
def gameOver():
    screen.draw.text("GAME OVER",(250,300))
def update():
    global score
    global level
    move=False
    for b in bullets:
        b.y=b.y-5
    if keyboard.w:
        ship.y-=10
    if keyboard.s:
        ship.y+=10
    if keyboard.d:
        if ship.x< WIDTH-100:
            ship.x+=10
    if keyboard.a:
        if ship.x> 100:
            ship.x-=10
    if keyboard.space:
        bullet=Actor("bullet")
        bullet.x=ship.x
        bullet.y=ship.y-150
        bullets.append(bullet)
    if len(bugs)>0:
        move=True
    for b in bugs:
        if move == True:
            b.y+=0.5
        if b.y> HEIGHT:
            bugs.remove(b)
        for bullet in bullets:
            if bullet.colliderect(b):
                bullets.remove(bullet)
                bugs.remove(b)
                score=score+1
                if len(bugs)==0:
                    gameOver()
                    """
                    level=level+1
                    for i in range(10):
                        bug=Actor("bug")
                        bug.x=100+(50*i)
                        bug.y=200
                        bugs.append(bug)

                    """
            if ship.colliderect(b):
                ship.dead=True
pgzrun.go()
# make for cat+fish game(fishes maybe start falling faster)



