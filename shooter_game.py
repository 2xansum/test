from pygame import *
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y, size_x, size_y,player_speed):
        suprite.Sprite.__init__(self)
        self.image= transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5 :
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed 
    
    def fire(self):
        pass

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Шутер мопс')
backround = transform.scale(image.load('galaxy.jpg'),(700, 500))
#window.blit(backround, (0,0))

player = Player('rocket.png', 5,win_height-100,80,100,10)

run = True
finish = False
while run:
    for e in event.get()
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(backround, (0,0))
        player.update()
        player.reset()
        display.update()
    time.delay(50)






