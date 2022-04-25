from pygame import * 
screen = display.set_mode((800,600))
display.set_caption('Ping pong')
screen.fill((20,70,40))
clock = time.Clock()
game = True
while game:
    clock.tick(90)
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
