import pygame
from pygame import *
from random import randint
from time import sleep
#pyinstaller in /home/ubuntu/.local/bin
pygame.init()
mixer.init()
putm = mixer.Sound('put.mp3')
putm.play()

font.init()
font1 = font.SysFont(None,80)
font2 = font.SysFont(None,36)
lose = font1.render("Loser", True, (100, 19, 19))
win = font1.render("Winer", True, (5+50, 20+100, 5+50))
lost = 0
score = 0

health = 5 

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,rectx,recty,speed,size):
        super().__init__()
        self.image = transform.scale(image.load(player_image),size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rectx
        self.rect.y = recty

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Dice(GameSprite):
    def __init__(self,player_image,rectx,recty,speed,size,ammo,group = 0):
        global ingr1,ingr2,ingr3,rastoanie,weightmore     
        super().__init__(player_image,rectx,recty,speed,size)
        self.nomber = ammo
        self.group = group
    def update(self):
        if self.group == 0:
            self.rect.x,self.rect.y =  475,40
        elif self.group == 1:
            if ingr1 == 1:
                    x =gr1.rect.x + ingr1*13
            if ingr1 <= 4:
                if ingr1 == 1:
                    x =gr1.rect.x + ingr1*13
                else:
                    x = ingr1*50 +13
                y = gr1.rect.y + 13
                self.rect.x,self.rect.y =  x,y
            elif ingr1 > 4 and ingr1 <= 8:
                if ingr1-4 == 1:
                    x =gr1.rect.x + 13
                    
                else:
                    x = (ingr1-4)*50 +13
                y = gr1.rect.y + 13 +13 +50
                self.rect.x,self.rect.y =  x,y
            elif ingr1 > 8 and ingr1 <= 12:
                if ingr1-4 == 1:
                    x =gr1.rect.x + 13 
                else:
                    x = (ingr1-8)*50 +13
                y = gr1.rect.y + 13 +13 +50 +13 +50
                self.rect.x,self.rect.y =  x,y
        

    
pygame.mouse.set_visible(False)
height = 500
weight = 1000
i = 0
cursor = GameSprite('cure.gif',0,0,0,(12,24))
r = randint(1,6)
dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)

rastoanie = 49
weightmore = 26
gr1 = GameSprite('backs.png', rastoanie, 170, 0, (250,200))
gr2 = GameSprite('backs.png', gr1.rect.x + rastoanie+weightmore+250, 170, 0, (250,200))
gr3 = GameSprite('backs.png', gr2.rect.x + rastoanie+weightmore+250, 170, 0, (250,200))
decor1 = image.load('<.png')
decor2 = image.load('<.png')
scoregr1 = 0
scoregr2 = 0
scoregr3 = 0
ingr1 = 0
ingr2 = 0
ingr3 = 0

dictgrs = dict()


back = GameSprite('back.png', 0, 0, 0, (weight,height))

dices = list()

dictgrs[str(i)] = dice
i += 1

clock = pygame.time.Clock()
display.set_caption('Кости','utf-8')
window = pygame.display.set_mode((weight,height))
finish = False
FPS = 120
lost_max = 3
score_max = 25
game = True
while not finish:
    

    if game:
        for event in pygame.event.get():
            if event.type == QUIT:
                finish = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    dice.group =  1
                    dictgrs[str(i)] = dice
                    i += 1
                    scoregr1 += dice.nomber
                    ingr1 += 1
                    r = randint(1,6)
                    dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)
                elif event.key == pygame.K_2:
                    dice.group =  2
                    scoregr2 += dice.nomber
                    dictgrs[str(i)] = dice
                    i += 1
                    ingr2 += 1
                    r = randint(1,6)
                    dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)
                elif event.key == pygame.K_3:
                    dice.group =  3
                    scoregr3 += dice.nomber
                    dictgrs[str(i)] = dice
                    i += 1
                    ingr3 += 1
                    r = randint(1,6)
                    dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)
                
        clock.tick(FPS)
        display.update()
        
        back.reset()
        window.blit(decor1,(gr1.rect.x + 265+weightmore/2,100 + gr1.rect.y - 10))
        window.blit(decor2,(gr2.rect.x + 265+weightmore/2,100 + gr2.rect.y - 10))
        gr1.reset()
        gr2.reset()
        gr3.reset()

    pos = pygame.mouse.get_pos()
    dice.reset()
    dice.update()
    for n in range(i+1):
        if str(n) in dictgrs:
            cl = dictgrs[str(n)]
            cl.reset()
            cl.update()
    if pos[0] > 0 and pos[1] > 0 and pos[1] < height- 1 and pos[0] < weight- 1:
        window.blit(cursor.image,pos)
    

    
    
