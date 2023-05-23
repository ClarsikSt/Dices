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
        window.blit(self.image,(self.rect.x,self.rect.y))
    def newpos(self):
        if self.group == 0:
            self.rect.x,self.rect.y =  475,40
        elif self.group == 1:

            if ingr1 <= 4:
                if ingr1 == 1:
                    x =gr1.rect.x + 13
                else:
                    x =gr1.rect.x + ingr1*63 - 50
                y = gr1.rect.y + 13
                self.rect.x,self.rect.y =  x,y
            elif ingr1 > 4 and ingr1 <= 8:
                if ingr1 == 1:
                    x =gr1.rect.x + 13
                else:
                    x =gr1.rect.x + (ingr1-4)*63 - 50
                y = gr1.rect.y + 13 +13 +50
                self.rect.x,self.rect.y =  x,y
            elif ingr1 > 8 and ingr1 <= 12:
                if ingr1 == 1:
                    x =gr1.rect.x + 13
                else:
                    x =gr1.rect.x + (ingr1-8)*63 - 50
                y = gr1.rect.y + 13 +13 +50 +13 +50
                self.rect.x,self.rect.y =  x,y
        elif self.group == 2:
            if ingr2 <= 4:
                if ingr2 == 1:
                    x =gr2.rect.x + 13
                else:
                    x =gr2.rect.x + ingr2*63 - 50
                y = gr2.rect.y + 13
                self.rect.x,self.rect.y =  x,y
            elif ingr2 > 4 and ingr2 <= 8:
                if ingr2 == 1:
                    x =gr2.rect.x + 13
                else:
                    x =gr2.rect.x + (ingr2-4)*63 - 50
                y = gr2.rect.y + 13 +13 +50
                self.rect.x,self.rect.y =  x,y
            elif ingr2 > 8 and ingr2 <= 12:
                if ingr2 == 1:
                    x =gr2.rect.x + 13
                else:
                    x =gr2.rect.x + (ingr2-8)*63 - 50
                y = gr2.rect.y + 13 +13 +50 +13 +50
                self.rect.x,self.rect.y =  x,y
        elif self.group == 3:
            if ingr3 <= 4:
                if ingr3 == 1:
                    x =gr3.rect.x + 13
                else:
                    x =gr3.rect.x + ingr3*63 - 50
                y = gr3.rect.y + 13
                self.rect.x,self.rect.y =  x,y
            elif ingr3 > 4 and ingr3 <= 8:
                if ingr3 == 1:
                    x =gr3.rect.x + 13
                else:
                    x =gr3.rect.x + (ingr3-4)*63 - 50
                y = gr3.rect.y + 13 +13 +50
                self.rect.x,self.rect.y =  x,y
            elif ingr3 > 8 and ingr3 <= 12:
                if ingr3 == 1:
                    x =gr3.rect.x + 13
                else:
                    x =gr3.rect.x + (ingr3-8)*63 - 50
                y = gr3.rect.y + 13 +13 +50 +13 +50
                self.rect.x,self.rect.y =  x,y
dices = pygame.sprite.Group()
    
pygame.mouse.set_visible(False)
height = 500
weight = 1000
i = 0
cursor = GameSprite('cure.gif',0,0,0,(12,24))


rastoanie = 34
weightmore = 26
gr1 = GameSprite('backs.png', rastoanie, 170, 0, (270,200))
gr2 = GameSprite('backs.png', gr1.rect.x + rastoanie+weightmore+270, 170, 0, (270,200))
gr3 = GameSprite('backs.png', gr2.rect.x + rastoanie+weightmore+270, 170, 0, (270,200))
decor1 = image.load('<.png')
decor2 = image.load('<.png')



ingr1f = 0
ingr2f = 0
ingr3f = 0

scoregr1 = 3
scoregr2 = 5
scoregr3 = 10

ingr1 = 1
ingr2 = 1
ingr3 = 2

d = Dice('dice3.png',(weight-50)/2,40,0,(50,50),1,1)
d.newpos()
dices.add(d)
d = Dice('dice5.png',(weight-50)/2,40,0,(50,50),5,2)
d.newpos()
dices.add(d)
d = Dice('dice6.png',gr3.rect.x + 13,gr3.rect.y + 13,0,(50,50),6,3)
dices.add(d)
d = Dice('dice4.png',(weight-50)/2,40,0,(50,50),4,3)
d.newpos()
dices.add(d)



back = GameSprite('back.png', 0, 0, 0, (weight,height))


r = randint(1,6)
dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)
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
                    if ingr1 <12:
                        dice.group =  1
                        ingr1 += 1
                        dice.newpos()
                        scoregr1 += dice.nomber
                        d = dice
                        dices.add(d)
                        i += 1
                        r = randint(1,6)
                        dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)
                        putm.play()
                elif event.key == pygame.K_2:
                    if ingr2 <12:
                        dice.group =  2
                        ingr2 += 1
                        dice.newpos()
                        scoregr2 += dice.nomber
                        d = dice
                        dices.add(d)
                        i += 1
                        r = randint(1,6)
                        dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)
                        putm.play()
                elif event.key == pygame.K_3:
                    if ingr3 <12:
                        dice.group =  3
                        ingr3 += 1
                        dice.newpos()
                        scoregr3 += dice.nomber
                        d = dice
                        dices.add(d)
                        i += 1
                        r = randint(1,6)
                        dice = Dice('dice'+str(r)+'.png',(weight-50)/2,40,0,(50,50),r)
                        putm.play()

        if scoregr1<scoregr2<scoregr3 and ingr1 + ingr2 + ingr3 >= 36:
            window.blit(win,(weight/2-50,height/2-50))
            game = False
            finish = True
        elif (scoregr1<scoregr2<scoregr3) == False:
            window.blit(lose,(weight/2-50,height/2-50))
            game = False
            finish = True


        clock.tick(FPS)
        display.update()
        
        back.reset()
        window.blit(decor1,(gr1.rect.x +5+ 265+weightmore/2,100 + gr1.rect.y - 10))
        window.blit(decor2,(gr2.rect.x +5+ 265+weightmore/2,100 + gr2.rect.y - 10))
        gr1.reset()
        gr2.reset()
        gr3.reset()

    pos = pygame.mouse.get_pos()
    dice.reset()

    csoretxt1 = font2.render(str(scoregr1), True, (20, 20, 20))
    csoretxt2 = font2.render(str(scoregr2), True, (20, 20, 20))
    csoretxt3 = font2.render(str(scoregr3), True, (20, 20, 20))

    window.blit(csoretxt1,(gr1.rect.centerx,270+ gr1.rect.y))
    window.blit(csoretxt2,(gr2.rect.centerx,270+ gr2.rect.y))
    window.blit(csoretxt3,(gr3.rect.centerx,270+ gr3.rect.y))

    dices.draw(window)
    dices.update()
    if pos[0] > 0 and pos[1] > 0 and pos[1] < height- 1 and pos[0] < weight- 1:
        window.blit(cursor.image,pos)
finish = False
while not finish:
    for event in pygame.event.get():
            if event.type == QUIT:
                finish = True
    if pos[0] > 0 and pos[1] > 0 and pos[1] < height- 1 and pos[0] < weight- 1:
        window.blit(cursor.image,pos)

    
    
