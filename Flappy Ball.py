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

Vihaan = Circle(0,0)
def draw():
    screen.clear()
    Vihaan.draw()
    
def update(dt):
    uy = Vihaan.vy
    Vihaan.vy = uy + Accelaration * dt
    Vihaan.y = Vihaan.y + (uy + Vihaan.vy)*0.5*dt
    Vihaan.x = Vihaan.x + (Vihaan.vx*dt)
    if Vihaan.y > HEIGHT:
        Vihaan.y = HEIGHT
        Vihaan.vy = -Vihaan.vy*0.9
    if Vihaan.x > WIDTH or Vihaan.x <0:
        Vihaan.vx = -Vihaan.vx*0.9

pgzrun.go()