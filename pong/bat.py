from config import *
import pygame
class Bat:
    def __init__(self):
        self.x=BAT_OFFSET
        self.y=(SCREEN_HEIGHT-BAT_HEIGHT)//2
        self.speed_y=0
        self.x2=SCREEN_WIDTH-BAT_2_OFFSET-BAT_2_WIDTH
        self.y2=(SCREEN_HEIGHT-BAT_2_HEIGHT)//2
        self.speed_y2=0
        self.speed_x2=0
    def update(self):
        self.y+=self.speed_y
        self.y2+=self.speed_y2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed_y+=-1
        elif keys[pygame.K_s]:
            self.speed_y += 1
        else:
            self.speed_y=0
        if self.y<=0:
            self.y = 0
        if self.y >= SCREEN_HEIGHT - BAT_HEIGHT:
            self.y = SCREEN_HEIGHT - BAT_HEIGHT
        if keys[pygame.K_UP]:
            self.speed_y2+=-1
        elif keys[pygame.K_DOWN]:
            self.speed_y2 += 1
        else:
            self.speed_y2=0
        if self.y2<=0:
            self.y2 = 0
        if self.y2 >= SCREEN_HEIGHT - BAT_2_HEIGHT:
            self.y2 = SCREEN_HEIGHT - BAT_2_HEIGHT
        
