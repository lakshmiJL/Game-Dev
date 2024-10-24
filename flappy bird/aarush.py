import pygame
import random
pygame.init()
WIDTH = 700
HEIGHT = 500
pipe_gap = 150
pipe_freq = 1500
last_pipe = pygame.time.get_ticks()-pipe_freq
surface = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/bg.png")
background2 = pygame.transform.scale(background,(900,800))
ground = pygame.image.load("/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/ground.png")
ground2 = pygame.transform.scale(ground,(1000,168))
groundscroll = 0
scrollspeed = 4
game_over = False
flying = False
fps = 60
clock = pygame.time.Clock()
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 1
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f"/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.vel = 0
        self.clicked = False
    def update(self):
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            self.counter += 1
            cooldown = 5
            if self.counter > cooldown:
                self.counter = 0
                self.index +=1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index],self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)


bird_group = pygame.sprite.Group()
flappy = Bird(100,int(HEIGHT/2))
bird_group.add(flappy)

class Pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-int(pipe_gap/2)]
        if pos == -1:
            self.rect.topleft = [x,y+int(pipe_gap/2)]
    def update(self):
        self.rect.x -= scrollspeed
        if self.rect.right < 0:
            self.kill()

pipe_group = pygame.sprite.Group()

run = True
while run == True:
    clock.tick(fps)

    surface.blit(background2,(0,0))
    surface.blit(ground2,(groundscroll,HEIGHT - 50))

    bird_group.draw(surface)
    pipe_group.draw(surface)
    bird_group.update()
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True
    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False
    #generating new pipes
    if game_over == False and flying == True:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_freq:
            pipe_height = random.randint(-100,100)
            btm_pipe = Pipes(WIDTH,int(HEIGHT/2)+pipe_height,-1)
            top_pipe = Pipes(WIDTH,int(HEIGHT/2)+pipe_height,1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
        groundscroll -= scrollspeed
        if abs(groundscroll) > 30:
            groundscroll = 10
        pipe_group.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    pygame.display.update()

#make pipes class and make it move like ground


pygame.quit()