from ursina import *
from random import randint

class pipe(Entity):
    def __init__(self, x, y, img):
        super().__init__()
        self.model = 'quad'
        self.scale = (1, 7)
        self.color = color.green
        self.x = x
        self.y = y
        self.texture = img
        self.collider = 'box'
        self.score_tag = True

def update():
    global offset, run, n_frame
    if run:
        offset += time.dt * .3
        setattr(bg, "texture_offset", (offset, 0))
        
        for m in range(num):
            pipes_top[m].x -= time.dt * 1.8
            pipes_bottom[m].x -= time.dt * 1.8
            
            if pipes_bottom[m].x < -8:
                pipes_bottom[m].x += 4 * num
                pipes_top[m].x = pipes_top[m-1].x + 4
                y = -7 + randint(0, 50)/10
                pipes_bottom[m].y = y
                pipes_top[m].y = y + 9
                pipes_bottom[m].score_tag = True

def input(key):
    if key=="up arrow" or key=="up arrow hold":
        bird.y += 0.5
    elif key=="down arrow" or key=="down arrow hold":
        bird.y -= 0.5

app = Ursina()

offset = 0
run = True
n_frame = 0
num = 5
x = 6

bg = Entity(model='quad', texture='assets/bg', scale=(20,10), z=.1)
bird = Animation("assets/bird", collider="box", scale=(1.3, .8), y=1.5)

pipes_bottom = [None] * num
pipes_bottom[0] = pipe(x, -4, "assets/pipe_bottom")
pipes_top = [ None] * num
pipes_top[0] = pipe(x, -4+9, "assets/pipe_top")

for m in range(1, num):
    x += 4
    y = -7 + randint(0, 50)/10
    pipes_bottom[m] = pipe(x, y, "assets/pipe_bottom")
    pipes_top[m] = pipe(x, y+9, "assets/pipe_top")

app.run()
