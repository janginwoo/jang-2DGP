from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def quadrangle_move():
        x=400
        y=90
        r=0
        while(x<800):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x=x+2
                delay(0.01)
        while(y<=600):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y=y+2
                delay(0.01)
        while(x>0):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x=x-2
                delay(0.01)
        while(y>90):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y=y-2
                delay(0.01)
        while(0<=x<400):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x=x+2
                delay(0.01)
        while(100<=x<700):
                
                alpa=math.radians(2)
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x=x+(8*math.cos(r))
                y=y+(8*math.sin(r))
                r=r+alpa
                
                delay(0.01)
while(True):
        quadrangle_move()
        circle_move()
close_canvas()
