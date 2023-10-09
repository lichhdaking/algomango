from pygame import *
from random import randint

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Ping pong')
display.set_caption('Jumper')
game = True

FPS = 60
clock = time.Clock()

game = True

fon = transform.scale(image.load('maxer.jpg'), (700, 500))

fon = transform.scale(image.load('fon_1.jpg'), (700, 500))

fon_game_over = transform.scale(image.load('fon_2.jpg'), (700, 500))

font.init()
font1 = font.SysFont('Arial', 50)
win = font1.render("Игра окончена!", True, (200, 10, 50))
amount_proiden = 0


mixer.init()
mixer.music.load('fon_music.mp3')
mixer.music.load('Breathe.mp3')
mixer.music.play()
#otbev = mixer.Sound('otbev.mp3')
otbev = mixer.Sound('otbev.ogg')



font.init()
font1 = font.SysFont('Arial', 30)
score_proiden = font1.render(f'Ваш счёт: '+ str(amount_proiden), True, (100, 100, 100))
font2 = font.SysFont('Arial', 50)
game_over = font2.render('Игра окончена', True, (200, 100, 100))
game_over_score = font2.render('Ваш счёт:' + str(amount_proiden), True, (150, 100, 100))

amount_jump = 0
jump = False

class Platform (sprite.Sprite):
    def init(self, color_1, color_2, color_3, width, height, rect_x, rect_y, speed):
        super().init()
        self.color_1 = color_1
        self.color_3 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed


    def update(self):
        self.rect.y += 1
        if self.rect.y >= 490:
            self.rect.y = randint(0, 100)
            self.rect.x = randint(10, 690)
    # window.blit(self.image, (self.rect.x, self.rect.y))
    def fall(self):
        self.rect.y += self.speed

    # def reset(self):
    # self.rect.y -= 5




class GameSprite (sprite.Sprite):
    def init(self, player_image, player_x, player_y, size_x, size_y , player_speed_x, player_speed_y):
        super().init()
@@ -45,33 +79,33 @@ def reset(self):

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def jump(self):
        global amount_jump, jump
        if amount_jump <= 100:
            amount_jump += 1
            self.rect.y -= 2
        else:
            jump = False
            amount_jump = 0



player = GameSprite('ball_stal.png', 50, 400, 50, 30, 3, 3)



class Wall (sprite.Sprite):
    def init(self, color_1, color_2, color_3, width, height, rect_x, rect_y, speed):
        super().init()
        self.color_1 = color_1
        self.color_3 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




platforms = sprite.Group()
fall_platforms = sprite.Group()

platform = Platform(100, 80, 0, 100, 10, 50, 450, 0)
platforms.add(platform)
for i in range(5):
    platform = Platform(100, 80, 0, 100, 10, randint(0,700), randint(150,450), 0)
    platforms.add(platform)
for i in range(2):
    fall_platform = Platform(100, 80, 0, 100, 10, randint(0,700), 0, 0)
    fall_platforms.add(fall_platform)



@@ -80,85 +114,84 @@ def draw_wall(self):



finish = False


while game:
    keys = key.get_pressed()

platform_1 = Wall(100, 60, 30, 10, 100, 50, 50, 5)
platform_2 = Wall(100, 90, 90, 10, 100, 650, 350, 5)
    for e in event.get():
        if e.type == QUIT:
            game = False

ball = GameSprite('ball_stal.png', 350, 250, 30, 30, 3, 3)
    if finish == False:

        window.blit(fon, (0, 0))
        platforms.draw(windo
