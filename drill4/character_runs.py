from pico2d import *
open_canvas()
grass = load_image('grass.png')
character2 = load_image('animation_sheet.png')
character1 = load_image('run_animation.png')
x = 0

x = 0
frame = 0
boy=0
while(True):
    while boy == 0:
        clear_canvas()
        grass.draw(400, 30)
        character1.clip_draw(frame*100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame+1) % 8
        x += 5
        if(x > 800):
            boy = 1
        delay(0.05)
        get_events()
    while boy == 1:
        clear_canvas()
        grass.draw(400, 30)
        character2.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        if(x<0):
            boy=0
        delay(0.05)
        get_events()


close_canvas()

