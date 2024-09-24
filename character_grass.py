from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')


def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)

def run_circle():
    print('CIRCLE')

    r,cx,cy = 300,800//2,600//2
    cx = 800//2
    cy = 600//2
    
    for degree in range(0,360,3):

        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.01)
    

    pass ## 아무기능이 없는 빈 함수

def run_top():
    print('TOP')
    for x in range(0,750,10):
        draw_boy(x,550)
    pass
def run_right():
    print('RIGHT')
    for y in range(550,50,-10):
        draw_boy(750,y)
    pass
def run_bottom():
    print('BOTTOM')
    for x in range(750,50,-10):
        draw_boy(x,50)
    pass
def run_left():
    print('LEFT')
    for y in range(50,550,10):
        draw_boy(50,y)
    pass

def run_rectangle():
    print('RECTANGEL')
    run_top()
    run_right()
    run_bottom()
    run_left()

    
    pass

#file here

while True:
    run_circle()
    run_rectangle()
    break
    


close_canvas()
