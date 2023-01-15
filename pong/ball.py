from config import *
class Ball:
    def __init__(self):
        self.r = 20
        self.x = SCREEN_WIDTH//2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x=7
        self.speed_y=6
        self.left_score = 0
        self.right_score = 0
    def update(self):
        # передвигаем мяч по экарну
        self.x+=self.speed_x
        self.y+=self.speed_y
        #выход за левый кран экрана
        if self.x <= self.r:
            # летел налево - полетел направо
            self.x=SCREEN_WIDTH//2
            self.speed_x=-self.speed_x
            self.right_score+=1
            self.speed_x-=2
            self.speed_y-=2
        if self.x>= SCREEN_WIDTH - self.r:
            #летел направо - полетел налево
            self.x=SCREEN_WIDTH//2
            self.speed_x= -self.speed_x
            self.left_score+=1
            self.speed_x-=2
            self.speed_y-=2
            #выход за верхний край
        if self.y<=self.r:
            #летел наверх-полетел вниз
            self.speed_y=-self.speed_y
            #выход за нижний край
        if self.y>=SCREEN_HEIGHT - self.r:
            #летел вниз-полетел наверх
            self.speed_y=-self.speed_y
