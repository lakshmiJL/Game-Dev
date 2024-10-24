import pygame, random
pygame.init()

clock = pygame.time.Clock()

WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Flappy Bird")

background = pygame.image.load("/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/bg.png")
ground = pygame.image.load("/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/ground.png")

flying = False
game_over = False
FPS = 60
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() #importing constructor of the super class (all properties)
        self.images = []
        self.index = 1
        self.counter = 0

        for i in range(1, 4):
            img = pygame.image.load(f"/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.click = False

    def update(self):
        if flying == True:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)

        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False

            self.counter += 1
            flap = 5
            if self.counter > flap:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 1
                self.image = self.images[self.index]
                self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)

        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__()
        self.image = pygame.image.load("/Users/Kuttimma/Documents/Official/JetLearn/Game Dev 2/Lesson9/img/pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if pos == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]
    
    def update(self):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

group1 = pygame.sprite.Group()
bird = Bird(100, int(HEIGHT / 2))
group1.add(bird)

group2 = pygame.sprite.Group()

ground_scroll = 0
speed = 4

run = True
while run:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    screen.blit(ground, (ground_scroll, HEIGHT - 50))

    group1.draw(screen)
    group1.update()

    group2.draw(screen)

    if pygame.sprite.groupcollide(group1, group2, False, False) or bird.rect.top < 0:
        game_over = True
    if bird.rect.bottom >= 768:
        game_over = True
        flying = False

        
    if game_over == False and flying == True:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, -1)
            top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, 1)
            group2.add(bottom_pipe)
            group2.add(top_pipe)
            last_pipe = time_now
        ground_scroll -= speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        
        group2.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()