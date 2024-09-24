from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

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
        delay(0.1)
    

    pass ## 아무기능이 없는 빈 함수

def run_rectangle():
    print('RECTANGEL')
    pass

#file here

while True:
    run_circle()
    run_rectangle()
    break
    


close_canvas()
