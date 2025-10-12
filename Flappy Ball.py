import pgzrun
from random import randint

TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600

Accelaration = 2000

class Circle():
    def __init__(self, x_pos, y_pos):
        self.radius = 30
        self.x = x_pos
        self.y = y_pos
        self.vx = 200
        self.vy = 200 
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, "blue")

class Circle_2():
    def __init__(self, x_pos, y_pos):
        self.radius = 30
        self.x = x_pos
        self.y = y_pos
        self.vx = 200
        self.vy = 200
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, "red")

V = Circle(0,0)
G = Circle_2(50,50)
def draw():
    screen.clear()
    V.draw()
    G.draw()
    
def update(dt):
    uy = V.vy
    uy = G.vy
    V.vy = uy + Accelaration * dt
    G.vy = uy + Accelaration * dt
    V.y = V.y + (uy + V.vy)*0.5*dt
    G.y = G.y + (uy + G.vy)*0.5*dt
    V.x = V.x + (V.vx*dt)
    G.x = G.x + (V.vx*dt)
    if V.y > HEIGHT:
        V.y = HEIGHT
        V.vy = -V.vy*0.9
    if G.y > HEIGHT:
        G.y = HEIGHT
        G.vy = -V.vy*0.9
    if V.x > WIDTH or V.x <0:
        V.vx = -V.vx*0.9
    if G.x > WIDTH or G.x <0:
        G.vx = -G.vx*0.9


pgzrun.go()