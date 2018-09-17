from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_point1():
   frame = 0
   count = 0
   x, y = 203, 535
   gotox=(132-203)/200
   gotoy=(243-535)/200
   while count<100:
       clear_canvas_now()
       grass.draw(400, 30)
       character.clip_draw(frame*100, 0, 100, 100, x, y)
       update_canvas()
       count+=1
       x+=gotox
       y+=gotoy
       frame=(frame+1)%8
       delay(0.05)


def move_point2():
    pass
def move_point3():
    pass
def move_point4():
    pass
def move_point5():
    pass
def move_point6():
    pass
def move_point7():
    pass
def move_point8():
    pass
def move_point9():
    pass
def move_point10():
    pass



while True:
    move_point1()
    move_point2()
    move_point3()
    move_point4()
    move_point5()
    move_point6()
    move_point7()
    move_point8()
    move_point9()
    move_point10()

close_canvas()
