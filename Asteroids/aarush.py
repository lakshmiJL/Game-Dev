import pygame
import math
import random

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))

background = pygame.image.load("asteroidsPics/starbg.png")
large_asteroid = pygame.image.load("asteroidsPics/asteroid150.png")
small_asteroid = pygame.image.load("asteroidsPics/asteroid50.png")
Medium_asteroid = pygame.image.load("asteroidsPics/asteroid100.png")
ship = pygame.image.load("asteroidsPics/spaceRocket.png")
star = pygame.image.load("asteroidsPics/star.png")
alienImg = pygame.image.load("asteroidsPics/alienShip.png")

Large_bang = pygame.mixer.Sound("sounds/bangLarge.wav")
Small_bang = pygame.mixer.Sound("sounds/bangSmall.wav")
shot = pygame.mixer.Sound("sounds/shoot.wav")

shot.set_volume(.25)
Large_bang.set_volume(.25)
Small_bang.set_volume(.25)

pygame.display.set_caption("Alien Game")
clock = pygame.time.Clock()

gameover = False
lives = 3
score = 0
rapid_fire = False
rapid_fire_start = -1
highScore = 0
isSoundOn = True
class Player(object):
    def __init__(self):
        self.image = ship
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.angle = 0
        self.rotated_surf = pygame.transform.rotate(self.image,self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = self.x,self.y
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine*self.w//2, self.y-self.sine*self.h//2)
    def draw(self,screen):
        screen.blit(self.rotated_surf, self.rotated_rect)
    def turn_left(self):
        self.angle += 5
        self.rotated_surf = pygame.transform.rotate(self.image,self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = self.x,self.y
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine*self.w//2, self.y-self.sine*self.h//2)
    def turn_right(self):
        self.angle -= 5
        self.rotated_surf = pygame.transform.rotate(self.image,self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = self.x,self.y
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine*self.w//2, self.y-self.sine*self.h//2)
    def move_forward(self):
        self.x += self.cosine*6
        self.y -= self.sine*6
        self.rotated_surf = pygame.transform.rotate(self.image,self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = self.x,self.y
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine*self.w//2, self.y-self.sine*self.h//2)
    def update_location(self):
        if self.x > WIDTH+50:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH
        elif self.y > HEIGHT:
            self.y = 50
        elif self.y < 0:
            self.y = HEIGHT
class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x,self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10
    def move(self):
        self.x += self.xv
        self.y -= self.yv
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255), [self.x,self.y,self.w,self.h])
    def checkoffscreen(self):
        if self.x < -50 or self.x > WIDTH or self.y > HEIGHT or self.y < -50:
            return True
class Asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = small_asteroid
        elif self.rank == 2:
            self.image = Medium_asteroid
        else:
            self.image = large_asteroid
        self.w = 50 * rank
        self.h = 50 * rank
        self.ranPoint = random.choice([(random.randrange(0, WIDTH-self.w), random.choice([-1*self.h - 5, HEIGHT + 5])), (random.choice([-1*self.w - 5, WIDTH + 5]), random.randrange(0, HEIGHT - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < WIDTH//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < HEIGHT//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1,3)
        self.yv = self.ydir * random.randrange(1,3)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

class Star(object):
    def __init__(self):
        self.img = star
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, WIDTH-self.w), random.choice([-1*self.h - 5, HEIGHT + 5])), (random.choice([-1*self.w - 5, WIDTH + 5]), random.randrange(0, HEIGHT - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < WIDTH//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < HEIGHT//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

class Alien(object):
    def __init__(self):
        self.img = alienImg
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, WIDTH-self.w), random.choice([-1*self.h - 5, HEIGHT + 5])), (random.choice([-1*self.w - 5, WIDTH + 5]), random.randrange(0, HEIGHT - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < WIDTH//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < HEIGHT//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class AlienBullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.xv = self.dx * 5
        self.yv = self.dy * 5

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])




def draw_window():
    screen.blit(background,(0,0))

    font = pygame.font.SysFont('arial',30)
    livesText = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    playAgainText = font.render('Press Tab to Play Again', 1, (255,255,255))
    scoreText = font.render('Score: ' + str(score), 1, (255,255,255))
    highScoreText = font.render('High Score: ' + str(highScore), 1, (255, 255, 255))
    
    player.draw(screen)

    for b in player_bullets:
        b.draw(screen)
    for a in asteroids:
        a.draw(screen)
    
    for s in stars:
        s.draw(screen)
    for a in aliens:
        a.draw(screen)
    for b in alienBullets:
        b.draw(screen)
    if rapid_fire:
        pygame.draw.rect(screen, (0, 0, 0), [WIDTH//2 - 51, 19, 102, 22])
        pygame.draw.rect(screen, (255, 255, 255), [WIDTH//2 - 50, 20, 100 - 100*(count - rapid_fire_start)/500, 20])

    
    if gameover:
        screen.blit(playAgainText, (WIDTH//2-playAgainText.get_width()//2, HEIGHT//2 - playAgainText.get_height()//2))
    
    screen.blit(scoreText, (WIDTH- scoreText.get_width() - 25, 25))
    screen.blit(livesText, (25, 25))
    screen.blit(highScoreText, (WIDTH - highScoreText.get_width() -25, 35 + scoreText.get_height()))
    pygame.display.update()

player = Player()
player_bullets = []
count = 0
asteroids = []
count = 0
stars = []
aliens = []
alienBullets = []
run = True
while run:
    clock.tick(60)
    count+=1
    if not gameover:
        ran = random.choice([1,1,1,2,2,3])
        asteroids.append(Asteroid(ran))
        if count % 1000 == 0:
            stars.append(Star())
        if count % 750 == 0:
            aliens.append(Alien())
        for i, a in enumerate(aliens):
            a.x += a.xv
            a.y += a.yv
            if a.x > WIDTH + 150 or a.x + a.w < -100 or a.y > HEIGHT + 150 or a.y + a.h < -100:
                aliens.pop(i)
            if count % 60 == 0:
                alienBullets.append(AlienBullet(a.x + a.w//2, a.y + a.h//2))

            for b in player_bullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        aliens.pop(i)
                        if isSoundOn:
                            bangLargeSound.play()
                        score += 50
                        break

        for i, b in enumerate(alienBullets):
            b.x += b.xv
            b.y += b.yv
            if (b.x >= player.x - player.w//2 and b.x <= player.x + player.w//2) or b.x + b.w >= player.x - player.w//2 and b.x + b.w <= player.x + player.w//2:
                if (b.y >= player.y-player.h//2 and b.y <= player.y + player.h//2) or b.y + b.h >= player.y - player.h//2 and b.y + b.h <= player.y + player.h//2:
                    lives -= 1
                    alienBullets.pop(i)
                    break
        player.update_location()
        for b in player_bullets:
            b.move()
            if b.checkoffscreen():
                player_bullets.pop(player_bullets.index(b))
        if lives <= 0:
            gameover = True

        if rapid_fire_start != -1:
            if count - rapid_fire_start > 500:
                rapid_fire = False
                rapid_fire_start = -1        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turn_left()
        if keys[pygame.K_RIGHT]:
            player.turn_right()
        if keys[pygame.K_UP]:
            player.move_forward()
        if keys[pygame.K_SPACE]:
            if rapid_fire:
                print("FIRING")
                player_bullets.append(Bullet())
                if isSoundOn:
                    shot.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    if not rapid_fire:
                        player_bullets.append(Bullet())
                        if isSoundOn:
                            shot.play()
    draw_window()
    