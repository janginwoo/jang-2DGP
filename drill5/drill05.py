from pico2d import *
open_canvas()

grass = load_image('grass.png')
character1  = load_image('animation_sheet.png')
character2 = load_image('run_animation.png')


def move_point1():
   frame = 0
   count = 0
   x, y = 203, 535
   gotox=(132-203)/200
   gotoy=(243-535)/200
   while count<200:
       clear_canvas_now()
       grass.draw(400, 30)
       character1.clip_draw(frame*100, 0, 100, 100, x, y)
       update_canvas()
       count+=1
       x+=gotox
       y+=gotoy
       frame=(frame+1)%8
       delay(0.05)


def move_point2():
    frame = 0
    count = 0
    x, y = 132, 243
    gotox = (535 - 132) / 200
    gotoy = (470 - 243) / 200
    while count < 200:
        clear_canvas_now()
        grass.draw(400, 30)
        character2.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gotox
        y += gotoy
        frame = (frame + 1) % 8
        delay(0.05)


def move_point3():
    frame = 0
    count = 0
    x, y = 535, 470
    gotox = (477 - 535) / 200
    gotoy = (203 - 470) / 200
    while count < 200:
        clear_canvas_now()
        grass.draw(400, 30)
        character1.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gotox
        y += gotoy
        frame = (frame + 1) % 8
        delay(0.05)
def move_point4():
    frame = 0
    count = 0
    x, y = 477, 203
    gotox = (715 - 477) / 200
    gotoy = (136 - 203) / 200
    while count < 200:
        clear_canvas_now()
        grass.draw(400, 30)
        character2.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gotox
        y += gotoy
        frame = (frame + 1) % 8
        delay(0.05)
def move_point5():
    frame = 0
    count = 0
    x, y = 715, 136
    gotox = (316 - 715) / 200
    gotoy = (225 - 136) / 200
    while count < 200:
        clear_canvas_now()
        grass.draw(400, 30)
        character1.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gotox
        y += gotoy
        frame = (frame + 1) % 8
        delay(0.05)
def move_point6():
    frame = 0
    count = 0
    x, y = 316, 225
    gotox = (510 - 316) / 200
    gotoy = (92 - 225) / 200
    while count < 200:
        clear_canvas_now()
        grass.draw(400, 30)
        character2.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += gotox
        y += gotoy
        frame = (frame + 1) % 8
        delay(0.05)
def move_point7():
    pass
def move_point8():
    pass
def move_point9():
    pass
def move_point10():
    pass



while True:
    #move_point1()
    #move_point2()
    #move_point3()
    #move_point4()
    #move_point5()
    move_point6()
    move_point7()
    move_point8()
    move_point9()
    move_point10()

close_canvas()
