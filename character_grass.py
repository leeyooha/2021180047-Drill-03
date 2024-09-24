from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_circle():
    print('CIRCLE')

    clear_canvas_now()
    boy.draw_now(400,300)
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
