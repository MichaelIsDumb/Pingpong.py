#Ping pong
from pygame import *
from pygame.sprite import *
from random import uniform
from random import *
# from time import *
# import time

window = display.set_mode((700, 500))
display.set_caption('Maze')

blue = (0, 191, 255)
black = (0, 0, 0)

#Set background
background = transform.scale(image.load('kurzgesagt.jpeg'), (700, 500))

#score
A_point = 0
B_point = 0

#Class
class GameSprite(sprite.Sprite):
    def __init__(self, object_image, object_width, object_height, object_x, object_y, object_speed, other_speed):
        super().__init__()
        self.image = transform.scale(image.load(object_image), (object_width, object_height))
        self.rect = self.image.get_rect()
        self.rect.x = object_x
        self.rect.y = object_y
        self.speed = object_speed
        self.otherspeed = other_speed
        self.direction = "down"
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(GameSprite):
    def control_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

class Player_2(GameSprite):
    def control_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

class Ball(GameSprite):
    def movement(self):
        self.rect.x += self.speed
        self.rect.y += self.otherspeed
        # random_number = randint(1,2)
        # if self.rect.y >= 0:
        #     self.rect.y += 3
        # if self.rect.y == 225:
        #     if random_number == 1:
        #         self.direction = "left"
        #     elif random_number == 2:
        #         self.direction = "right"
        # if self.direction == "left":
        #     self.rect.x -= self.speed
        # if self.direction == "right":
        #     self.rect.x += self.speed
    def collide(self, Player):
        if sprite.collide_rect(Player, Pingball):
            self.speed = self.speed*-1*uniform(1, 1.05)
            self.otherspeed = self.otherspeed*uniform(1, 1.05)
    def collide_wall(self):
        if self.rect.y >= 500 or self.rect.y <= 0:
            self.speed = self.speed*uniform(1, 1.05)
            self.otherspeed = self.otherspeed*-1*uniform(1, 1.05)
    def reset_1(self):
        global B_point 
        if self.rect.x <= 0:
            self.rect.x = 325
            self.rect.y = 0
            self.speed = 3
            self.otherspeed = 3
            B_point += 1
    def reset_2(self):
        global A_point
        if self.rect.x >= 700:
            self.rect.x = 325
            self.rect.y = 0
            self.speed = 3
            self.otherspeed = 3
            A_point += 1


#Create players
Sprite_1 = Player_1('duck1.png', 90, 90, 1, 205, 5, None)
Sprite_2 = Player_2('duck2.png', 90, 90, 610, 205, 5, None)
Pingball = Ball('pingball.png', 40, 40, 325, 0, 3, 3)

#font
font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)

your_display = font1.render('You', True, (255, 255, 255))
opponent_display = font1.render('Opponent', True, (255, 255, 255))
play_again = font1.render('Press [R] to play again', True, (255, 255, 255))
quit_game = font1.render('Press [X] to close the window', True, (255, 255, 255))

win = font2.render('YOU WIN', True, (255, 0, 0))
lose = font2.render('YOU LOSE', True, (255, 0, 0))
drawing = font2.render('DRAW!', True, (255, 255, 255))

#Music
mixer.init()
mixer.music.load('technology.mp3')
mixer.music.play()

def function():
    window.blit(background, (0, 0))

    #set up
    Sprite_1.show()
    Sprite_1.control_1()
    Sprite_2.show()
    Sprite_2.control_2()
    Pingball.show()

    #controls
    Pingball.movement()
    Pingball.collide(Sprite_1)
    Pingball.collide(Sprite_2)
    Pingball.collide_wall()
    Pingball.reset_1()
    Pingball.reset_2()




count = 0
game_status = True
clock = time.Clock()
finish = False 

while game_status:
    for e in event.get():
        if e.type == QUIT:
            game_status = False


    player_1 = font1.render(str(A_point), True, (255, 255, 255))
    player_2 = font1.render(str(B_point), True, (255, 255, 255))
    
    if finish != True:
        function()

    #winning condition
    if A_point == 2 and B_point < A_point:
        # window.fill(black)
        window.blit(win, (250, 235))
        # mixer.music.stop()
        window.blit(play_again, (250, 200))
        finish = True
        
    keys = key.get_pressed()
        
    if keys[K_r]:
        function()
        A_point = 0
        B_point = 0
            
    window.blit(your_display, (20, 5))
    window.blit(opponent_display, (590, 5))
    window.blit(player_1, (45, 40))
    window.blit(player_2, (655, 40))

    display.update()
    clock.tick(60)
