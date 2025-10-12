import pgzrun
from random import randint

TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600

Accelaration = 2000

class Circle():
    def __init__(self, x_pos, y_pos, color):
        self.radius = 30
        self.x = x_pos
        self.y = y_pos
        self.vx = 200
        self.vy = 200 
        self.color = color
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

V = Circle(0,0,"red")
def draw():
    screen.clear()
    V.draw()
    
def update(dt):
    uy = V.vy
    V.vy = uy + Accelaration * dt
    V.y = V.y + (uy + V.vy)*0.5*dt
    V.x = V.x + (V.vx*dt)         
    if V.y > HEIGHT:
        V.y = HEIGHT
        V.vy = -V.vy*0.9
    if V.x > WIDTH or V.x <0:
        V.vx = -V.vx*0.9

def on_key_down(key):
    if key == keys.SPACE:
        V.vy = -500

pgzrun.go()